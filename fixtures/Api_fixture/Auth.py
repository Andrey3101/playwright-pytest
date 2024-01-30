from APIs.SevenPayAuthApi import AuthApi

import pytest
import json


@pytest.fixture
def authorization_api(configs):
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
    accessToken = resp['result']['accessToken']
    refresh_token = resp['result']['refreshToken']
    return accessToken, refresh_token

@pytest.fixture
def login_conf_api(configs):
    api = AuthApi(configs['API_endpoints']['clientapi'])
    return api