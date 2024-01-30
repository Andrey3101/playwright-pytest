import pytest     
from sql.clear_processing import ClearProcessing
from sql.clear_installment import ClearInstallment





@pytest.fixture
def clear_users(configs):
    phone_num = configs['Creditional']['Client']['msisdn']
    proc_conn = configs['db']['processing_conn_string']
    proc_repository = ClearProcessing(proc_conn)
    checks = proc_repository.clear_client(phone_num)
    proc_conn_instlament = configs['db']['installment_conn_string']
    proc_repository_instllment = ClearInstallment(proc_conn_instlament)
    chech_i = proc_repository_instllment.clear_client_installment(phone_num)
    clear = 'Чиста прошла успешно, ответы {0} и {1}'.format(checks, chech_i)
    yield clear