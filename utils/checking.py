import json

# Методы для проверки ответов запросов

class Checking():

    # Метод для проверки статус кода

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Успешно!!! Статус код = " + str(result.status_code))

    # Метод для проверки наличия обязательных полей в ответе запроса

    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    # Метод для проверки значений обязательных полей в ответе запроса

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " Верен!!!")

    # Метод для проверки значений обязательных полей в ответе запроса по заданному слову

    @staticmethod
    def check_json_search_word_in_check_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f'слово {search_word} присутствует!!!')

    # Метод для получения значений заданного поля в ответе запроса

    @staticmethod
    def check_json_value_text(result, field_name):
        check = result.json()
        check_info = check.get(field_name)
        print(check_info)


