import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    bad_data = [
        ({"password": "123", "username": "learnqa", "firstName": "learanqa", "lastName": "learnqa", "email": "wrongemailexample.com"}, ("Invalid email format")),
        ({"username": "learnqa", "firstName": "learanqa", "lastName": "learnqa", "email": "email45example.com"}, ("The following required params are missed: password")),
        ({"password": "123", "firstName": "learanqa", "lastName": "learnqa", "email": "email45example.com"}, ("The following required params are missed: username")),
        ({"password": "123", "username": "learnqa", "lastName": "learnqa", "email": "email45example.com"}, ("The following required params are missed: firstName")),
        ({"password": "123", "username": "learnqa", "firstName": "learanqa", "email": "email45example.com"}, ("The following required params are missed: lastName")),
        ({"password": "123", "username": "learnqa", "firstName": "learanqa", "lastName": "learnqa"}, ("The following required params are missed: email")),
        ({"password": "123", "username": "q", "firstName": "learanqa", "lastName": "learnqa", "email": "email@45example.com"}, ("The value of 'username' field is too short")),
        ({"password": "123", "username": "y"*251, "firstName": "learanqa", "lastName": "learnqa", "email": "email45@example.com"}, ("The value of 'username' field is too long"))
    ]

    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response,"id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content '{response.content}"

    @pytest.mark.parametrize('bad_data', bad_data)
    def test_create_user_validation_errors(self, bad_data):
        data_set = bad_data[0]

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data_set)

        Assertions.assert_status_code(response, 400)
        assert response.text == bad_data[1]
