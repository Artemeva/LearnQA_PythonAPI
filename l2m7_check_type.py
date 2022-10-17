import requests

response1 = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1":"value1"})
print(response1.text)

response2 = requests.post("https://playground.learnqa.ru/api/check_type", params={"param1":"value1"})
print(response2.text)

response3 = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
print(response2.text)