from data_tools import GeoData, TestData


class SwaggerTestRequests:
    def __init__(self, all_endpoints, test_data):
        from copy import deepcopy
        self.__modified_endpoints = deepcopy(all_endpoints)
        self.test_data = test_data
        self.generate_test_requests()

    def __iter__(self):
        return (request for request in self.modified_endpoints)

    def __getitem__(self, item):
        return self.modified_endpoints[item]

    # def generate_requests(self):
    #     from copy import deepcopy
    #
    #     for endpoint in self.modified_endpoints:
    #         temp_request_list = []
    #         test_data = TestData().get_test_data(endpoint["operationId"])
    #         if len(test_data) == 1:
    #             endpoint["test_data"] = test_data
    #             self._generate_parameters_data(endpoint)
    #         if len(test_data) > 1:
    #             for item in range(len(test_data)):
    #                 temp_request = deepcopy(endpoint)
    #                 temp_request["test_data"] = test_data[item]
    #                 temp_request_list.append(temp_request)
    #     self.modified_endpoints.extend(temp_request_list)

    def _get_test_data(self, endpoint):
        return TestData(self.test_data).get_test_data(endpoint["operationId"])

    def generate_test_requests(self):
        from copy import deepcopy
        original_endpoints = deepcopy(self.modified_endpoints)

        for endpoint in original_endpoints:
            test_data = self._get_test_data(endpoint)
            num_of_test_cases = len(test_data)
            if num_of_test_cases == 1:
                self._generate_params_data(endpoint, test_data)
            if num_of_test_cases > 1:
                self._extend_endpoints(endpoint, num_of_test_cases)
                self._generate_params_data(endpoint, test_data)
        return self.modified_endpoints

    def _extend_endpoints(self, endpoint, num_of_test_cases):
        for item in range(1, num_of_test_cases):
            self.modified_endpoints.append(endpoint)

    def _generate_params_data(self, endpoint, test_data):
        operationId = endpoint["operationId"]
        for request in self.modified_endpoints:
            if request["operationId"] == operationId:
                request["test_data"] = [test_data.pop()]
                self._parse_params_data(request)

    def _parse_params_data(self, endpoint):
        for parameter in endpoint["parameters"]:
            if self._is_query_parameter(parameter):
                self._generate_in_query_parameters(endpoint,
                                                   parameter["name"])
            if self._is_header_parameter(parameter):
                self._generate_in_header_parameters(endpoint,
                                                    parameter["name"])
            if self._is_path_parameter(parameter):
                self._generate_in_path_parameters(endpoint,
                                                  parameter["name"])
            if self._is_form_parameter(parameter):
                self._generate_in_form_parameters(endpoint,
                                                  parameter["name"])
            if self._is_cookie_parameter(parameter):
                self._generate_in_cookie_parameters(endpoint,
                                                    parameter["name"])

    @property
    def modified_endpoints(self):
        return self.__modified_endpoints

    def _is_query_parameter(self, parameter):
        return parameter["in"] == "query"

    def _is_header_parameter(self, parameter):
        return parameter["in"] == "header"

    def _is_path_parameter(self, parameter):
        return parameter["in"] == "path"

    def _is_form_parameter(self, parameter):
        return parameter["in"] == "formData"

    def _is_cookie_parameter(self, parameter):
        return parameter["in"] == "cookie"

    # def _generate_in_query_parameters(self, request, key):
    #     query_delimiter = "?"
    #     var_delimiter = "&"
    #
    #     if query_delimiter not in request["url"]:
    #         request["url"] = request["url"] + query_delimiter + \
    #                          key + "=" + GeoData(key).get_random_data()
    #     else:
    #         request["url"] = request["url"] + var_delimiter + \
    #                          key + "=" + GeoData(key).get_random_data()

    def _generate_in_query_parameters(self, endpoint, key):
        query_delimiter = "?"
        var_delimiter = "&"

        test_value = endpoint["test_data"][0]["parameters"][key]

        if query_delimiter not in endpoint["url"]:
            endpoint["url"] = endpoint["url"] + query_delimiter + \
                              key + "=" + test_value
        else:
            endpoint["url"] = endpoint["url"] + var_delimiter + \
                              key + "=" + test_value

    def _generate_in_header_parameters(self, request, key):
        raise NotImplemented

    def _generate_in_path_parameters(self, endpoint, key):
        path = endpoint["url"].split("/")
        test_value = endpoint["test_data"][0]["parameters"][key]
        for element in path:
            if element == "{" + key + "}":
                endpoint["url"] = endpoint["url"].replace(
                    "{" + key + "}", test_value)

    def _generate_in_form_parameters(self, request, key):
        raise NotImplemented

    def _generate_in_cookie_parameters(self, request, key):
        raise NotImplemented
