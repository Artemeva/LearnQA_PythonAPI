from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase
import allure


@allure.epic("User deletion cases")
class TestUserDelete(BaseCase):
    @allure.description("Try to delete user that can't be deleted")
    def test_delete_user_id_2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        Assertions.assert_status_code(response1, 200)

        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, 'user_id')

        response2 = MyRequests.delete(
            f"/user/{user_id_from_auth_method}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        Assertions.assert_status_code(response2, 400)
        Assertions.assert_response_text(response2,"Please, do not edit test users with ID 1, 2, 3, 4 or 5.")

    @allure.description("Try to delete just created user")
    def test_delete_created_user(self):
        #create user
        reg_data = self.prepare_registration_data()

        email = reg_data["email"]
        password = reg_data["password"]

        response1 = MyRequests.post("/user/", data=reg_data)
        print(response1.status_code)
        print(response1.content)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        login_data = {
            "email": email,
            "password": password
        }

        #user login
        response2 = MyRequests.post("/user/login", data=login_data)
        print(response2.status_code)
        print(response2.content)

        #get auth data
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response2, 'user_id')

        #delete user using auth data
        response3 = MyRequests.delete(
            f"/user/{user_id_from_auth_method}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        print(response3.status_code)
        print(response3.content)

