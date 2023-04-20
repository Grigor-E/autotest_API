import allure
import requests
from utils.logger import Logger


# Список HTTP методов

class Http_methods():
    headers = {'Content-Type': 'application/json'} # Создание переменной заголовки с присвоением значения, что все заголовки будут передаваться в формате json
    cookie = ""

    @staticmethod
    def get(url):  # Создание метода, в который передаем url, т.е. адресную строку, к которой будем обращаться
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie) # Создание переменой с присвоением значения: обращение к библиотеке requests, методу get, который входит в библиотеку requests, создав кастомный метод get
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):  # Создание метода, в который передаем url и body
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)  # Создание переменой с присвоением значения: обращение к библиотеке requests, методу post, который входит в библиотеку requests, создав кастомный метод post
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):  # Создание метода, в который передаем url и body
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)  # Создание переменой с присвоением значения: обращение к библиотеке requests, методу put, который входит в библиотеку requests, создав кастомный метод put
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):  # Создание метода, в который передаем url и body
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)  # Создание переменой с присвоением значения: обращение к библиотеке requests, методу delete, который входит в библиотеку requests, создав кастомный метод delete
            Logger.add_response(result)
            return result
