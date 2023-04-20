import json

from utils.api import Swapi_star_wars_api
from utils.checking import Checking

# Проверка новой локации

def test_star_wars_people():

    print("Метод GET Darth Vader")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_darth_vader()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    # token = json.loads(result_get.text)  # Создание переменной для получения текста списка полей
    # print(list(token)) # Печать списка полей
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Darth Vader')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET film 1")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_film_1()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_value_text(result_get, 'characters')

    print("Метод GET film 2")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_film_2()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_value_text(result_get, 'characters')

    print("Метод GET film 3")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_film_3()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_value_text(result_get, 'characters')

    print("Метод GET film 6")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_film_6()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_value_text(result_get, 'characters')




