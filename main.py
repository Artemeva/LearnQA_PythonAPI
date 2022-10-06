import requests

response = requests.get("https://playground.learnqa.ru/api/hello?name=from%20Tatiana.")
print(response.text)