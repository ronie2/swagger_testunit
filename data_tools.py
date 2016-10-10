class GeoData:
    def __init__(self, key):
        self.__key = key

        self.data_dict = {
            "city": ["Oswego"],
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


class TestData:
    def __init__(self, test_data):
        self.__test_data = test_data

    @property
    def test_data(self):
        return self.__test_data

    def get_test_data(self, operationId):
        return [test for test in self.test_data
                if test["operationId"] == operationId]
