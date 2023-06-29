from utils.http_methods import Http_methods

base_url_maps = "https://rahulshettyacademy.com" # Базовая URL
base_url_swapi = "https://swapi.dev/api/" # Базовая URL swapi
key = "?key=qaclick123" # Параметр для всех запросов


# Методы для тестирования Google maps api

class Google_maps_api():

    # Метод для создания новой локации
    @staticmethod
    def create_new_place():
        json_for_create_new_place = {              # Переменная для создания новой локации
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resource = "/maps/api/place/add/json" # Ресурс метода Post
        post_url = base_url_maps + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place) # Создание переменной с присвоением значения обращения к кастомному методу Post
        print(result_post.text) # Печать текста значения result_post
        return result_post

    # Метод для проверки новой локации
    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json" # Ресурс метода Get
        get_url = base_url_maps + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url) # Создание переменной с присвоением значения обращения к кастомному методу Get
        print(result_get.text) # Печать текста значения result_get
        return result_get

    # Метод для изменения новой локации
    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"  # Ресурс метода Put
        put_url = base_url_maps + put_resource + key
        print(put_url)
        json_for_update_new_location = {              # Переменная для изменения новой локации
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = Http_methods.put(put_url, json_for_update_new_location)  # Создание переменной с присвоением значения обращения к кастомному методу Put
        print(result_put.text)  # Печать текста значения result_put
        return result_put

    # Метод для удаления новой локации
    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"  # Ресурс метода Delete
        delete_url = base_url_maps + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {                 # Переменная для изменения новой локации
            "place_id": place_id
        }
        result_delete = Http_methods.delete(delete_url, json_for_delete_new_location)  # Создание переменной с присвоением значения обращения к кастомному методу Delete
        print(result_delete.text)  # Печать текста значения result_delete
        return result_delete

# Методы для тестирования Swapi Star Wars api

class Swapi_star_wars_api():

    # Метод для проверки персонажа 1
    @staticmethod
    def get_luke_skywalker():
        get_resource = "people/1/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки персонажа 2
    @staticmethod
    def get_c_3po():
        get_resource = "people/2/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        # print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки персонажа 3
    @staticmethod
    def get_r2_d2():
        get_resource = "people/3/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        # print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки персонажа 4
    @staticmethod
    def get_darth_vader():
        get_resource = "people/4/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        # print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки персонажа 5
    @staticmethod
    def get_leia_organa():
        get_resource = "people/5/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        # print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки персонажа 6
    @staticmethod
    def get_owen_lars():
        get_resource = "people/6/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        # print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки фильма 1
    @staticmethod
    def get_film_1():
        get_resource = "films/1/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки фильма 2
    @staticmethod
    def get_film_2():
        get_resource = "films/2/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки фильма 3
    @staticmethod
    def get_film_3():
        get_resource = "films/3/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки фильма 4
    @staticmethod
    def get_film_4():
        get_resource = "films/4/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки фильма 5
    @staticmethod
    def get_film_5():
        get_resource = "films/5/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        print(result_get.text)  # Печать текста значения result_get
        return result_get

    # Метод для проверки фильма 6
    @staticmethod
    def get_film_6():
        get_resource = "films/6/"  # Ресурс метода Get
        get_url = base_url_swapi + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)  # Создание переменной с присвоением значения обращения к кастомному методу Get
        print(result_get.text)  # Печать текста значения result_get
        return result_get

