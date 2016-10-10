from urllib.parse import urlparse
from copy import deepcopy
import requests


class SwaggerSpec:
    def __init__(self, url):
        self.__swagger_spec = requests.get(url).json()
        self.url = url

    @property
    def swagger_spec(self):
        return self.__swagger_spec

    @property
    def paths(self):
        return self.__swagger_spec["paths"]

    @property
    def host(self):
        try:
            return self.__swagger_spec["host"]
        except:
            parsed_url = self.get_host_from_url()
            return parsed_url

    def get_host_from_url(self):
        url_to_parse = deepcopy(self.url)
        url = urlparse(url_to_parse)
        return url.hostname + ":" + str(url.port)

    @property
    def schemes(self):
        return self.__swagger_spec["schemes"]

    @property
    def version(self):
        return self.__swagger_spec["swagger"]

    @property
    def info(self):
        return self.__swagger_spec["info"]

    @property
    def basePath(self):
        if ("basePath" in self.__swagger_spec.keys() and
                len(self.__swagger_spec["basePath"])):
            return self.__swagger_spec["basePath"]
        else:
            return ""

    @property
    def tags(self):
        return self.__swagger_spec["tags"]

    @property
    def definitions(self):
        return self.__swagger_spec["definitions"]

    @property
    def authority(self):
        return [schema + "://" + self.host + self.basePath
                for schema in self.schemes]

    @property
    def all_endpoints(self):
        return [{"url": auth + path_key,
                 "method": method,
                 "parameters": self._get_path_method_parameters(
                     path_value[method]),
                 "consumes": self._get_path_method_consumes(
                     path_value[method]),
                 "produces": self._get_path_method_produces(
                     path_value[method]),
                 "responses": self._get_responses(response),
                 "operationId": self._get_path_method_operationId(
                     path_value[method])}
                for auth in self.authority
                for path_key, path_value in self.paths.items()
                for method in path_value.keys()
                for response in path_value[method]["responses"].values()
                ]

    def _get_path_method_operationId(self, path_method_obj):
        return self._get_path_metod_data(path_method_obj, "operationId")

    def _get_path_method_consumes(self, path_method_obj):
        return self._get_path_metod_data(path_method_obj, "consumes")

    def _get_path_method_parameters(self, path_method_obj):
        return self._get_path_metod_data(path_method_obj, "parameters")

    def _get_path_method_produces(self, path_method_obj):
        return self._get_path_metod_data(path_method_obj, "produces")

    def _get_path_metod_data(self, path_method_obj, key):
        if key in path_method_obj.keys():
            return path_method_obj[key]
        else:
            return None

    def _parameters_name_set(self):
        return set(parameter["name"]
                   for uri in self.all_endpoints
                   for parameter in uri["parameters"])

    def _get_response_schema(self, resp_obj):
        if isinstance(resp_obj["schema"], dict):
            if "items" in resp_obj["schema"].keys():
                def_name = resp_obj["schema"]["items"]["$ref"].split("/")[-1]
                try:
                    return resp_obj["schema"]["type"], self.definitions[
                        def_name]
                except KeyError:
                    return None, self.definitions[def_name]

            elif "$ref" in resp_obj["schema"].keys():
                def_name = resp_obj["schema"]["$ref"].split("/")[-1]
                try:
                    return resp_obj["schema"]["type"], self.definitions[
                        def_name]
                except KeyError:
                    return None, self.definitions[def_name]

    def _get_responses(self, resp_obj):
        if "schema" in resp_obj.keys():
            return self._get_response_schema(resp_obj)
        else:
            return None
