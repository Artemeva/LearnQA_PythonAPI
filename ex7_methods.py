import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("Запрос /compare_query_type без указания метода возвращает ответ с кодом ",response.status_code,"и текстом",response.text,"\n")

response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"HEAD"})
print("Запрос /compare_query_type с типом HEAD, не входящим в список допустимых, возвращает ответ с кодом ",response.status_code,"\n")

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type",params={"method":"GET"})
print("Запрос /compare_query_type с верными параметрами возвращает ответ с кодом ",response.status_code,"и текстом",response.text,"\n")

type = ["POST", "GET", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH", "TRACE", "CONNECT"]
i = 0
l = len(type)

while i < l:
    tp = type[i]
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type",params={"method":tp})
    if tp == "GET" and response.text != '{"success":"!"}':
        print("Запрос GET с параметром",tp,"дает ложноотрицательный результат ")
    if tp != "GET" and response.text == '{"success":"!"}':
        print("Запрос GET с параметром", tp, "дает ложноположительный результат ")

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",data={"method":tp})
    if tp == "POST" and response.text != '{"success":"!"}':
        print("Запрос POST с параметром",tp,"дает ложноотрицательный результат ")
    if tp != "POST" and response.text == '{"success":"!"}':
        print("Запрос POST с параметром", tp, "дает ложноположительный результат ")

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type",data={"method":tp})
    if tp == "PUT" and response.text != '{"success":"!"}':
        print("Запрос PUT с параметром",tp,"дает ложноотрицательный результат ")
    if tp != "PUT" and response.text == '{"success":"!"}':
        print("Запрос PUT с параметром", tp, "дает ложноположительный результат ")

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type",data={"method":tp})
    if tp == "DELETE" and response.text != '{"success":"!"}':
        print("Запрос DELETE с параметром",tp,"дает ложноотрицательный результат ")
    if tp != "DELETE" and response.text == '{"success":"!"}':
        print("Запрос DELETE с параметром", tp, "дает ложноположительный результат ")

    i = i + 1
