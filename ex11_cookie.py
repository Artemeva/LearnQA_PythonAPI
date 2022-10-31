import requests

class TestCookies:
    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        assert response.status_code == 200, "Wrong response code"

        cookie = response.cookies
        print(cookie.items())
        real_cookie = cookie.get("HomeWork")

        assert real_cookie == "hw_value", f"The cookie value is {real_cookie} instead of 'hw_value'"