import json

from utils.api import Swapi_star_wars_api
from utils.checking import Checking

# Получение информации о персонажах фильма "Звездные войны"
def test_star_wars_people():

    print("Метод GET Luke Skywalker")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_luke_skywalker()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    # token = json.loads(result_get.text)  # Создание переменной для получения текста списка полей
    # print(list(token)) # Печать списка полей
    Checking.check_json_token(result_get,['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Luke Skywalker')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET C-3PO")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_c_3po()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'C-3PO')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET R2-D2")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_r2_d2()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'R2-D2')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET Darth Vader")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_darth_vader()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Darth Vader')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET Leia Organa")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_leia_organa()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Leia Organa')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET Owen Lars")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_owen_lars()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Owen Lars')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET Beru Whitesun lars")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_beru_whitesun_lars()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get,['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Beru Whitesun lars')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET R5-D4")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_r5_d4()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get,['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'R5-D4')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/'])

    print("Метод GET Biggs Darklighter")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_biggs_darklighter()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Biggs Darklighter')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/'])

    print("Метод GET Obi-Wan Kenobi")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_obi_wan_kenobi()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Obi-Wan Kenobi')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET Anakin Skywalker")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_anakin_skywalker()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Anakin Skywalker')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'])

    print("Метод GET Wilhuff Tarkin")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_wilhuff_tarkin()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Wilhuff Tarkin')
    Checking.check_json_value_text(result_get, 'films')
    Checking.check_json_value(result_get, 'films', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/6/'])


# Получение информации о частях фильма "Звездные войны"
def test_star_wars_film():

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

    print("Метод GET film 4")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_film_4()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_value_text(result_get, 'characters')

    print("Метод GET film 5")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_film_5()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_value_text(result_get, 'characters')

    print("Метод GET film 6")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_film_6()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_value_text(result_get, 'characters')

# Получение информации о планетах фильма "Звездные войны"
def test_star_wars_planets():

    print("Метод GET planet 1")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_planet_1()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain', 'surface_water', 'population', 'residents', 'films', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Tatooine')
    Checking.check_json_value_text(result_get, 'rotation_period')
    Checking.check_json_value(result_get, 'rotation_period', '23')
    Checking.check_json_value_text(result_get, 'orbital_period')
    Checking.check_json_value(result_get, 'orbital_period', '304')

    print("Метод GET planet 2")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_planet_2()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain', 'surface_water', 'population', 'residents', 'films', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Alderaan')
    Checking.check_json_value_text(result_get, 'diameter')
    Checking.check_json_value(result_get, 'diameter', '12500')

    print("Метод GET planet 3")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_planet_3()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain', 'surface_water', 'population', 'residents', 'films', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Yavin IV')
    Checking.check_json_value_text(result_get, 'climate')
    Checking.check_json_value(result_get, 'climate', 'temperate, tropical')

    print("Метод GET planet 4")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_planet_4()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain', 'surface_water', 'population', 'residents', 'films', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Hoth')
    Checking.check_json_value_text(result_get, 'gravity')
    Checking.check_json_value(result_get, 'gravity', '1.1 standard')

    print("Метод GET planet 5")  # Печать маркера для информированности
    result_get = Swapi_star_wars_api.get_planet_5()  # Создание переменной со значением вызова метода
    Checking.check_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['name', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain', 'surface_water', 'population', 'residents', 'films', 'created', 'edited', 'url'])
    Checking.check_json_value(result_get, 'name', 'Dagobah')
    Checking.check_json_value_text(result_get, 'terrain')
    Checking.check_json_value(result_get, 'terrain', 'swamp, jungles')






