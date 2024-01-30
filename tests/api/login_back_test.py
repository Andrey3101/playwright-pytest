import json
import random

class TestApiLogin:

    # Положительный сценарий авторизации
    def test_authorization(self, api_auth, configs):
        # Создание тела запроса для авторизации
        auth_data = {
            "msisdn": 0,
            "captchaToken": "string"
        }
        auth_data["msisdn"] = configs['Creditional']['Client']['msisdn']
        # Отправка успешного запроса
        request_auth = api_auth.post_login(post_data=json.dumps(auth_data))
        assert request_auth.status_code == 200
        resp = json.loads(request_auth.text)
        assert resp['result']['confirmationRequestId'] != "00000000000000000000000000000000" and resp['success'] == True and resp['errorMessage'] == None
        req_id = resp['result']['confirmationRequestId']
        return req_id
    
    # Негативный сценарий, отправки запроса на авторизацию с неправильным номером
    def test_auth_negative(self, api_auth):
        # Создание тела запроса для отправки запроса авторизации
        authData = {
            "msisdn": 0,
            "captchaToken": "string"
        }
        negative_number = ''.join(random.choice('1234567890') for i in range(13))
        authData['msisdn'] = negative_number
        # Отправка запроса
        request_auth = api_auth.post_login(post_data= json.dumps(authData))
        # Проверка полученного статуса
        assert request_auth.status_code == 200
        # Парсинг ответа и проверка данных
        resp = json.loads(request_auth.text)
        assert resp['success'] == False and resp['result']['confirmationRequestId'] == "00000000000000000000000000000000"