import json
from APIs.SevenPayAuthApi import AuthApi
from sql.processing import ProcessingSql
from time import sleep



class TestApiAuth:

    # Прохождение успешного кейса
    def test_login_confirmation(self, login_conf_api, check_user, configs):
        check = check_user
        api = AuthApi(configs['API_endpoints']['clientapi'])
        data = {
            "msisdn": 0,
            "captchaToken": "string"
        }
        data["msisdn"] = configs['Creditional']['Client']['msisdn']
        # Отправка успешного запроса
        request_auth = api.post_login(post_data=json.dumps(data))
        assert request_auth.status_code == 200
        resp = json.loads(request_auth.text)
        assert resp['errorMessage'] == None and resp['success'] == True
        req_id = resp['result']['confirmationRequestId']
#        req_id = authtorization_api
        print(req_id)
        # Формирование запроса
        data = {
            "requestId": "string",
            "token": "string"
        }
        data['requestId'] = req_id
        data['token'] = "1111"
        # Отправка успешного запроса
        request_api = login_conf_api.post_login_confirmation(post_data=json.dumps(data))
        assert request_api.status_code == 200
        resp = json.loads(request_api.text)
        assert resp['success'] == True and resp['errorMessage'] == None and resp['result']['errorMessage'] == None and resp['result']['errorType'] == None
        # Подключение к БД, сделано на случай отсутствия номера в БД (можно было сделать try except или сделать кейс положительным, но решил что так будет правильней, т.к. при первом прохождении мы смотрим в БД после выполнения запроса)
        phone = configs['Creditional']['Client']['msisdn']
        proc_conn = configs['db']['processing_conn_string']
        proc_repository = ProcessingSql(proc_conn)
        check = proc_repository.get_client(phone)
        # Проверка данных в БД (активности, кол-ва отправленных запросов и т.д.)
        client_id = check[0][0]
        # Подключение и выполнение скрипта в БД и таблице client_confirmation
        proc_conn = configs['db']['processing_conn_string']
        proc_repository = ProcessingSql(proc_conn)
        check_user = proc_repository.client_confirmation(client_id)
        # Проверка полученных значений
        assert check_user[0] == 1 and check_user[1] == 0 and check_user[2] == True and check_user[3] == True
    
    # Прохождение негативного кейса
    def test_login_negative(self, login_conf_api, check_user, get_user_enabled, configs):
        check = check_user
        api = AuthApi(configs['API_endpoints']['clientapi'])
        data = {
            "msisdn": 0,
            "captchaToken": "string"
        }
        data["msisdn"] = configs['Creditional']['Client']['msisdn']
        # Отправка успешного запроса
        request_auth = api.post_login(post_data=json.dumps(data))
        assert request_auth.status_code == 200
        resp = json.loads(request_auth.text)
        assert resp['errorMessage'] == None and resp['success'] == True
        req_id = resp['result']['confirmationRequestId']
        # Формирование тела запроса
        data = {
            "requestId": "string",
            "token": "string"
        }
        data['requestId'] = req_id
        data['token'] = "1112"
        # Отправка негативного запроса
        request_api = login_conf_api.post_login_confirmation(post_data=json.dumps(data))
        assert request_api.status_code == 404
        resp = json.loads(request_api.text)
        assert resp['success'] == False and resp['result']['errorType'] == 1 and resp['result']['accessToken'] == None and resp['result']['refreshToken'] == None
        # Проверка данных в БД (активности, кол-ва отправленных запросов и т.д.)
        client_id = get_user_enabled[0][0]
        # Подключение и выполнение скрипта в БД и таблице client_confirmation
        proc_conn = configs['db']['processing_conn_string']
        proc_repository = ProcessingSql(proc_conn)
        check_user = proc_repository.client_confirmation(client_id)
        # Проверка полученных значений
        assert check_user[0] == 1 and check_user[1] == 0 and check_user[2] == False and check_user[3] == True

    def test_confirmation_negative(self, login_conf_api, check_user, get_user_enabled, configs):
        check = check_user
        api = AuthApi(configs['API_endpoints']['clientapi'])
        data = {
            "msisdn": 0,
            "captchaToken": "string"
        }
        data["msisdn"] = configs['Creditional']['Client']['msisdn']
        # Отправка успешного запроса
        request_auth = api.post_login(post_data=json.dumps(data))
        assert request_auth.status_code == 200
        resp = json.loads(request_auth.text)
        assert resp['errorMessage'] == None and resp['success'] == True
        req_id = resp['result']['confirmationRequestId']
        # Формирование тела запроса
        data = {
            "requestId": "string",
            "token": "stirng"
        }
        data['requestId'] = req_id
        data['token'] = "1112"
        # отправка кода авторизации (негативная)
        requst_id = login_conf_api.post_login_confirmation(post_data=json.dumps(data))
        assert requst_id.status_code == 404
        resp = json.loads(requst_id.text)
        assert resp['success'] == False and resp['result']['errorType'] == 1
        # Проверка данных в БД (активности, кол-ва отправленных запросов и т.д.)
        client_id = get_user_enabled[0][0]
        # Подключение и выполнение скрипта в БД и таблице client_confirmation
        proc_conn = configs['db']['processing_conn_string']
        proc_repository = ProcessingSql(proc_conn)
        check_user = proc_repository.client_confirmation(client_id)
        # Проверка полученных значений
        assert check_user[0] == 1 and check_user[1] == 0 and check_user[2] == False and check_user[3] == True
        # Повторная отправка кода авторизации
        resend = login_conf_api.resend_login_conf(req_id)
        assert resend.status_code == 200
        # Формирование тела запроса
        post_d = data
        post_d['request_id'] = req_id
        post_d['token'] = "55555"
        # Повторная отправка кода (негативная)
        sleep(30)
        req = login_conf_api.post_login_confirmation(post_data = json.dumps(post_d))
        assert req.status_code == 404
        resp = json.loads(req.text)
        assert resp['success'] == False and resp['result']['errorType'] == 1
        # Проверка данных в БД (активности, кол-ва отправленных запросов и т.д.)
        client_id = get_user_enabled[0][0]
        # Подключение и выполнение скрипта в БД и таблице client_confirmation
        proc_conn = configs['db']['processing_conn_string']
        proc_repository = ProcessingSql(proc_conn)
        check_user = proc_repository.client_confirmation(client_id)
        assert check_user[0] == 1 and check_user[1] == 1 and check_user[2] == False and check_user[3] == True

    def test_threeRequest_negative(self, login_conf_api, check_user,get_user_enabled, configs):
        check = check_user
        api = AuthApi(configs['API_endpoints']['clientapi'])
        data = {
            "msisdn": 0,
            "captchaToken": "string"
        }
        data["msisdn"] = configs['Creditional']['Client']['msisdn']
        # Отправка успешного запроса
        request_auth = api.post_login(post_data=json.dumps(data))
        assert request_auth.status_code == 200
        resp = json.loads(request_auth.text)
        assert resp['errorMessage'] == None and resp['success'] == True
        req_id = resp['result']['confirmationRequestId']
        # Формирование тела запроса
        data = {
            "requestId": "string",
            "token": "stirng"
        }
        data['requestId'] = req_id
        data['token'] = "1234"
        # Отправка запроса запроса (негативная)
        req = login_conf_api.post_login_confirmation(post_data = json.dumps(data))
        assert req.status_code == 404
        resp = json.loads(req.text)
        assert resp['success'] == False and resp['result']['errorType'] == 1
        # Проверка данных в БД (активности, кол-ва отправленных запросов и т.д.)
        client_id = get_user_enabled[0][0]
        # Подключение и выполнение скрипта в БД и таблице client_confirmation
        proc_conn = configs['db']['processing_conn_string']
        proc_repository = ProcessingSql(proc_conn)
        check_user = proc_repository.client_confirmation(client_id)
        # Проверка полученных значений
        assert check_user[0] == 1 and check_user[1] == 0 and check_user[2] == False and check_user[3] == True
        # Повторная отправка кода авторизации
        resend = login_conf_api.resend_login_conf(req_id)
        assert resend.status_code == 200
        # Формирование тела запроса
        datas = data
        datas['requestId'] = req_id
        datas['token'] = "11223"
        # Отправка негативного запроса
        sleep(30)
        reqests = login_conf_api.post_login_confirmation(post_data = json.dumps(datas))
        assert reqests.status_code == 404
        resp = json.loads(reqests.text)
        assert resp['success'] == False and resp['result']['errorType'] == 1
        # Проверка данных в БД (активности, кол-ва отправленных запросов и т.д.)
        client_id = get_user_enabled[0][0]
        # Подключение и выполнение скрипта в БД и таблице client_confirmation 
        proc_conn = configs['db']['processing_conn_string']
        proc_repository = ProcessingSql(proc_conn)
        check_user = proc_repository.client_confirmation(client_id)
        # Проверка полученных значений
        assert check_user[0] == 1 and check_user[1] == 1 and check_user[2] == False and check_user[3] == True
        # Повторная отправка кода авторизации
        resend = login_conf_api.resend_login_conf(req_id)
        assert resend.status_code == 200
        # 3-я отправка запроса
        sleep(150)
        req = login_conf_api.post_login_confirmation(post_data = json.dumps(datas))
        assert req.status_code == 404
        resp = json.loads(req.text)
        assert resp['success'] == False and resp['result']['errorType'] == 2
        # Проверка данных в БД (активности, кол-ва отправленных запросов и т.д.)
        client_id = get_user_enabled[0][0]
        # Подключение и выполнение скрипта в БД и таблице client_confirmation
        proc_conn = configs['db']['processing_conn_string']
        proc_repository = ProcessingSql(proc_conn)
        check_user = proc_repository.client_confirmation(client_id)
        # Проверка полученных значений
        assert check_user[0] == 1 and check_user[1] == 2 and check_user[2] == False and check_user[3] == True
        resend = login_conf_api.resend_login_conf(req_id)
        assert resend.status_code == 200