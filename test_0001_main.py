import pytest

from swagger_tools import SwaggerSpec
from request_tools import SwaggerTestRequests

from test_data_conf import test_data_geo_service, swagger_link

swagger_spec = SwaggerSpec(swagger_link)
requests = SwaggerTestRequests(swagger_spec.all_endpoints,
                               test_data_geo_service)


@pytest.fixture(params=requests)
def data(request):
    import requests
    result = requests.request(method=request.param["method"],
                              url=request.param["url"])
    to_return = {"result": result, "request": request.param}
    return to_return


def test_001_start_line(data):
    print(data["request"]["url"])
    assert data["result"].status_code == 200


def test_002_header(data):
    # data["result"].headers["Content-Type"] == data["request"]
    pytest.skip(msg="Not Implemented Headder Fields")


def test_003_body_valid_serialization(data):
    if data["result"].headers["Content-Type"] == "application/json":
        import json
        print(data["request"]["url"])
        try:
            json.loads(data["result"].content.decode())
        except Exception as e:
            print(e)
            assert False
        else:
            assert True
    else:
        pytest.skip(msg="Not Implemented nonJSON Serializer")


def test_004_body_valid_parameters_keys(data):
    if data["result"].headers["Content-Type"] == "application/json":
        import json
        obj = json.loads(data["result"].content.decode())
        print(data["request"]["url"])
        if data["request"]["responses"][0] == "object":
            assert data["request"]["responses"][1][
                       "properties"].keys() == obj.keys()
        elif data["request"]["responses"][0] == "array":
            for item in obj:
                assert data["request"]["responses"][1][
                           "properties"].keys() == item.keys()
    else:
        pytest.skip(msg="Not Implemented nonJSON Parameter Keys")


def test_005_body_valid_parameters_types(data):
    if data["result"].headers["Content-Type"] == "application/json":
        import json
        obj = json.loads(data["result"].content.decode())
        print(data["request"]["url"])
        if data["request"]["responses"][0] == "object":
            for parameter in obj.values():
                print(data["request"]["url"])
                pytest.skip(msg="Not Implemented JSON Parameter Types")
        elif data["request"]["responses"][0] == "array":
            for item in obj:
                pytest.skip(msg="Not Implemented JSON Parameter Types")
    else:
        pytest.skip(msg="Not Implemented nonJSON Parameter Types")


def test_006_body_valid_parameters_values(data):
    pytest.skip(msg="Not Implemented Valid Parameters Values")


def test_007_response_time(data):
    max_delay = 100000
    assert data["result"].elapsed.microseconds <= max_delay


def test_008_response_content_lenght(data):
    print(data["request"]["url"])
    if ("Transfer-Encoding" in data["result"].headers) and \
            (data["result"].headers["Transfer-Encoding"] != "chunked"):
        print(data["request"]["url"])
        assert int(data["result"].headers["Content-Length"]) >= 2
    else:
        pytest.skip(msg="Not Implemented for Chunked Content")


def test_009_response_body(data):
    print(data["request"]["url"])
    er_resp_body = data["request"]["test_data"][0]["er"]["body"]
    ar_resp_body = data["result"].text
    assert er_resp_body == ar_resp_body


pytest.main("-vv --html=report.html --junitxml=report_xml.xml")
