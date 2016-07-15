class SwaggerSpec:
    def __init__(self, url):
        from aiohttp import ClientSession
        import asyncio
        loop = asyncio.get_event_loop()
        with ClientSession(loop=loop) as session:
            self.__swagger_spec = loop.run_until_complete(SwaggerSpec.request(session, url))

    async def request(session, url):
        async with session.request("get", url) as resp:
            return await resp.json()

    @property
    def swagger_spec(self):
        from collections import defaultdict
        return self.__swagger_spec

    @property
    def paths(self):
        from collections import defaultdict
        return self.__swagger_spec["paths"]

    @property
    def host(self):
        return self.__swagger_spec["host"]

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
        return ""
        # return self.__swagger_spec["basePath"]

    @property
    def tags(self):
        return self.__swagger_spec["tags"]

    @property
    def definitions(self):
        return self.__swagger_spec["definitions"]

    @property
    def authority(self):
        return [schema + "://" + self.host + self.basePath for schema in self.schemes]

    @property
    def uri(self):
        return [{"url": auth + path[0],
                 "method": method,
                 "parameters": path[1][method]["parameters"],
                 #"consumes": path[1][method]["consumes"],
                 "produces": path[1][method]["produces"],
                 # "responses": path[1][method]["responses"],
                 "responses": self.swagger_responses(response)}
                for auth in self.authority
                for path in self.paths.items()
                for method in path[1].keys()
                for response in path[1][method]["responses"].values()
                ]

    def parameters_name_set(self):
        # print("uri:")
        # print(self.uri)
        return set(parameter["name"]
                   for uri in self.uri
                   for parameter in uri["parameters"])

    def swagger_responses(self, res_obj):
        if "schema" in res_obj.keys():
            if isinstance(res_obj["schema"], dict):
                if "items" in res_obj["schema"].keys():
                    def_name = res_obj["schema"]["items"]["$ref"].split("/")[-1]
                    try:
                        return res_obj["schema"]["type"], self.definitions[def_name]
                    except KeyError:
                        return None, self.definitions[def_name]

                elif "$ref" in res_obj["schema"].keys():
                    def_name = res_obj["schema"]["$ref"].split("/")[-1]
                    try:
                        return res_obj["schema"]["type"], self.definitions[def_name]
                    except KeyError:
                        return None, self.definitions[def_name]
        else:
            return None


class GeoData:
    def __init__(self, key):
        self.__key = key

        self.data_dict = {
            "city": ["New York", "London", "Chicago"],
            "country": ["USA", "Ukraine"],
            "zip": ["90210", "10000"],
            "phoneNumber": ["+1 305-757-7708", "+1 305-757-7708"],
            "state": ["Texas", "CA"],
            "ip": ["8.8.8.8", "217.69.139.202"],
            "name": ["Roman", "Igor"]
        }

    def get_random_data(self):
        from random import choice
        return choice(self.get_data_by_key(self.__key))

    def get_data_by_key(self, key):
        return self.data_dict[key]


class Request:
    def __init__(self, swag_uri_obj):
        from copy import deepcopy
        self.__modified = deepcopy(swag_uri_obj)

    def generate_uri(self):
        for uri in self.modified:
            for parameter in uri["parameters"]:
                if parameter["in"] == "path":
                    self.generate_in_path(uri, parameter["name"])
                if parameter["in"] == "query":
                    self.generate_in_query(uri, parameter["name"])

        return self.modified

    @property
    def modified(self):
        return self.__modified

    def generate_in_query(self, request, key):
        if request["url"][-1] != "?":
            request["url"] = request["url"] + "?" + key + "=" + GeoData(key).get_random_data()
        else:
            request["url"] = request["url"] + "&" + key + "=" + GeoData(key).get_random_data()

    def generate_in_path(self, request, key):
        path = request["url"].split("/")
        for element in path:
            if element == "{" + key + "}":
                request["url"] = request["url"].replace("{" + key + "}", GeoData(key).get_random_data())


a = SwaggerSpec("http://ks-inf-geo1.t2.tenet:8080/swagger.json")
aa = Request(a.uri)
aaa = aa.generate_uri()
print(aaa)
pass
