import pytest
from APIs.SevenPayMerchantApi import Merchant
from APIs.SevenPayAuthApi import AuthApi
from sql.processing import ProcessingSql

@pytest.fixture
def api(configs):
    api = Merchant(configs['API_endpoints']['merchantsapi'], configs['Creditional']['merchant']['apikey'])
    return api

@pytest.fixture
def portal_url(configs):
    portal_url = configs['portals']['client_portal'] + '\login'
    return portal_url


@pytest.fixture
def api_auth(configs):
    auth = AuthApi(configs['API_endpoints']['clientapi'])
    return auth

@pytest.fixture
def check_user(configs):
    phone = configs['Creditional']['Client']['msisdn']
    proc_conn = configs['db']['processing_conn_string']
    proc_repository = ProcessingSql(proc_conn)
    check = proc_repository.update_client(phone)
    return check


@pytest.fixture
def get_user_enabled(configs):
    phone = configs['Creditional']['Client']['msisdn']
    proc_conn = configs['db']['processing_conn_string']
    proc_repository = ProcessingSql(proc_conn)
    check = proc_repository.get_client(phone)
    return check
