import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

redirect_count = len(response.history)
final_url = response.url

print("Число редиректов: ", redirect_count)
print("Конечный URL: ",final_url)
