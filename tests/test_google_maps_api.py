import json
import allure
from utils.api import Google_maps_api
from utils.checking import Checking

# Создание, изменение и удаление новой локации

@allure.description("Test create, update, delete place")
def test_create_new_place():
    print("Метод POST") # Печать маркера для информированности
    result_post = Google_maps_api.create_new_place() # Создание переменной со значением вызова метода
    check_post = result_post.json() # Создание переменной с присвоением значения обращения к переменной result_post с просьбой вернуть ответ в формате json
    place_id = check_post.get("place_id") # Создание переменной с присвоением значения обращения к переменной check_post и вызов метода get, который будет возвращать значение ключа place_id
    Checking.check_status_code(result_post, 200) # Сравнение HTTP status code
    # token = json.loads(result_post.text) # Создание переменной для получения текста списка полей
    # print(list(token)) # Печать списка полей
    Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
    Checking.check_json_value(result_post, 'status', 'OK')

    print("Метод GET POST")  # Печать маркера для информированности
    result_get = Google_maps_api.get_new_place(place_id)  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200) # Сравнение HTTP status code
    # token = json.loads(result_get.text)  # Создание переменной для получения текста списка полей
    # print(list(token)) # Печать списка полей
    Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
    Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

    print("Метод PUT")  # Печать маркера для информированности
    result_put = Google_maps_api.put_new_place(place_id)  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_put, 200) # Сравнение HTTP status code
    Checking.check_json_token(result_put, ['msg'])
    Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

    print("Метод GET PUT")  # Печать маркера для информированности
    result_get = Google_maps_api.get_new_place(place_id)  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200) # Сравнение HTTP status code
    # token = json.loads(result_get.text)  # Создание переменной для получения текста списка полей
    # print(list(token))  # Печать списка полей
    Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
    Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

    print("Метод DELETE")  # Печать маркера для информированности
    result_delete = Google_maps_api.delete_new_place(place_id)  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_delete, 200) # Сравнение HTTP status code
    Checking.check_json_token(result_delete, ['status'])
    Checking.check_json_value(result_delete, 'status', 'OK')

    print("Метод GET DELETE")  # Печать маркера для информированности
    result_get = Google_maps_api.get_new_place(place_id)  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 404) # Сравнение HTTP status code
    Checking.check_json_token(result_get, ['msg'])
    Checking.check_json_search_word_in_check_value(result_get, 'msg', 'failed')

    print("Тестирование создания, изменения и удаления новой локации прошло успешно!!!")

