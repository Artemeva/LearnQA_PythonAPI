import requests

class TestHeaders:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")

        assert response.status_code == 200, "Wrong response code"

        header = response.headers
        print(header)
        header_value = header.get("x-secret-homework-header")

        assert 'x-secret-homework-header' in header, "There is no x-secret-homework-header in headers"
        assert header_value == "Some secret value", "Wrong header value"