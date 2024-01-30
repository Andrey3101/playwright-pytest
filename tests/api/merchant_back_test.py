import json
import datetime
from uuid import uuid4
from sql.clear_processing import ClearProcessing
from sql.clear_installment import ClearInstallment


class TestMerchantApi:

    # Отправка запроса в мерчант, положительный кейс
    def test_request_merchant(self, api, configs):
        # Формирование тела запроса
        data = {
                "orderId": "",
                "expireDate": "2024-12-23T14:45:15.005Z",
                "returnUrl": "https://google.com",
                "merchantDate": "2022-12-23T14:45:15.005Z",
                "productName": "string",
                "amount": 123,
                "merchantId": 1,
                "dualMode": False,
                "merchantDeliveryAmount": 0,
                "clientDeliveryAmount": 0,
                "notificationUrl": "https://yandex.ru"
            }
        data['orderId'] = str(uuid4())
        data['expireDate'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        data['merchantDate'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        # Отправка запроса в merchant
        api_key = configs['Creditional']['merchant']['apikey']
        req_id = api.create_invoice(api_key ,post = json.dumps(data))
        assert req_id.status_code == 200
        resp = json.loads(req_id.text)
        assert resp['status'] == 'Created' and resp['message'] == None

    # Отправка запроса в мерчант, негативный кейс
    def test_merchant_negative(self, api, configs):
        data = {
                "orderId": "",
                "expireDate": "2024-12-23T14:45:15.005Z",
                "returnUrl": "https://google.com",
                "merchantDate": "2022-12-23T14:45:15.005Z",
                "productName": "string",
                "amount": 123,
                "merchantId": 1,
                "dualMode": False,
                "merchantDeliveryAmount": 0,
                "clientDeliveryAmount": 0,
                "notificationUrl": "https://yandex.ru"
            }
        data['expireDate'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        data['merchantDate'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        data['orderId'] = str(uuid4())
        data['merchantId'] = int(1234567890)
        # Отправка запроса
        api_key = configs['Creditional']['merchant']['apikey']
        req_id = api.create_invoice(api_key, post = json.dumps(data))
        assert req_id.status_code == 500
        resp = json.loads(req_id.text)
        assert resp['Status'] == 'Failed' and resp['Message'] == 'Internal Server Error'

    # отправка запроса в мерчант, негативный кейс
    def test_merchant_neg(self, api, configs, clear_users):
        clear = clear_users
        # Формирование тела запроса
        data = {
                "orderId": "",
                "expireDate": "2024-12-23T14:45:15.005Z",
                "returnUrl": "https://google.com",
                "merchantDate": "2022-12-23T14:45:15.005Z",
                "productName": "string",
                "amount": 123,
                "merchantId": 1,
                "dualMode": False,
                "merchantDeliveryAmount": 0,
                "clientDeliveryAmount": 0,
                "notificationUrl": "https://yandex.ru"
            }
        data['orderId'] = None
        data['expireDate'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        data['merchantDate'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        # Отправка тела запроса
        api_key = configs['Creditional']['merchant']['apikey']
        req_id = api.create_invoice(api_key, post = json.dumps(data))
        assert req_id.status_code == 400
        resp = json.loads(req_id.text)
        assert resp['status'] == 400 and resp['title'] == 'One or more validation errors occurred.'