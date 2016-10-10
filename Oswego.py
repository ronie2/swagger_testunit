import pytest
import requests
from swagger_tools import SwaggerSpec
from request_tools import SwaggerTestRequests
from pprint import pprint
from test_data_conf import test_data_geo_service, swagger_link
import json

swagger_spec = SwaggerSpec(swagger_link)
endpoints = swagger_spec.all_endpoints
req = SwaggerTestRequests(swagger_spec.all_endpoints,
                          test_data_geo_service)
print("hallo")
print("hallo")
urls = []
for endpoint in endpoints:
    if "{city}" in endpoint["url"]:
        try:
            urls.append(endpoint["url"].format(city="Oswego", country="USA"))
        except Exception:
            try:
                urls.append(endpoint["url"].format(city="Oswego"))
            except Exception:
                urls.append(
                    endpoint["url"].format(city="Oswego", state="Kansas"))

resp = []
for url in urls:
    resp.append({"url": url,
                 "response": json.loads(requests.get(url).text)})

pprint(resp)
# @pytest.fixture(params=requests)
# def data(request):
#     import requests
#     result = requests.request(method=request.param["method"],
#                               url=request.param["url"])
#     to_return = {"result": result, "request": request.param}
#     return to_return
#
#
# def test_001_start_line(data):
#     print
