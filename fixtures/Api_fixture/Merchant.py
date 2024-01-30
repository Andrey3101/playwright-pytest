import pytest
import datetime
import json
from APIs.SevenPayMerchantApi import Merchant
from uuid import uuid4

@pytest.fixture
def request_merchant(configs):
    api = Merchant(configs['API_endpoints']['clientapi'])
    data_invoice =  {
                    "merchantInvoiceId": "",
                    "expireDate": "2024-12-23T14:45:15.005Z",
                    "returnUrl": "https://google.com",
                    "merchantDate": "2022-12-23T14:45:15.005Z",
                    "productName": "Тестовая шабашка",
                    "amount": 123,
                    "merchantId": 1,
                    "withDelivery": False,
                    "merchantDeliveryAmount": 0,
                    "clientDeliveryAmount": 0
                }
    data_invoice['merchantInvoiceId'] = str(uuid4())
    data_invoice['expireDate'] = datetime.datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    data_invoice['merchantDate'] = datetime.datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    # Отправка запроса
    api_key = configs['Creditional']['merchant']['apikey']
    req = api.create_invoice(api_key, post_data = json.dumps(data_invoice))
    assert req.status_code == 200
    resp = json.loads(req.text)
    assert resp['code'] == 0 and resp['message'] == "delivered" or resp['message'] == "processing"
    ref = resp['refId']
    return ref