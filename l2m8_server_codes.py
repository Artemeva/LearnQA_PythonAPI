import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
print(response.status_code)

response_500 = requests.get("https://playground.learnqa.ru/api/get_500")
print(response_500.status_code)

response_404 = requests.get("https://playground.learnqa.ru/api/404")
print(response_404.status_code)
print(response_404.text)

response_301 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response_301.status_code)
print(response_301.text)

response_301_ = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response_301_.history[0]
second_response = response_301_
print(first_response.url)
print(second_response.url)

