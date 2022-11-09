from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase
import allure


@allure.epic("User deletion cases")
class TestUserDelete(BaseCase):

    @allure.description("Try to delete just created user")
    def test_delete_created_user_by_user2(self):
        # create user 1
        reg_data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=reg_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        #get user 1 id
        new_user_id = self.get_json_value(response1, 'id')
        print(new_user_id)

        # create user 2 and authorize
        reg_data2 = self.prepare_registration_data()

        response2 = MyRequests.post("/user/", data=reg_data2)

        Assertions.assert_status_code(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email = reg_data2["email"]
        password = reg_data2["password"]

        login_data = {
            "email": email,
            "password": password
        }

        response3 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_status_code(response3, 200)

        auth_sid = self.get_cookie(response3, 'auth_sid')
        token = self.get_header(response3, 'x-csrf-token')

        #try to delete user 1 with auth data of user 2
        response4 = MyRequests.delete(
            f"/user/{new_user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        print(response4.status_code)
        print(response4.text)