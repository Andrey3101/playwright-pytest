import json
import pytest
import datetime

from uuid import uuid4
from pages.paymentpage import paymentpage
from gen.gen_credit_card_number import generateCardNumber
from collections import namedtuple
import random

# Переменные для сценария pytest
Task = namedtuple('Task', ['card', 'paymentmethods', 'condition'])
variable_for_tests = (Task('4100', 'Новая карта', 'Test'),
                    Task('4200', 'Новая карта', 'Test2'),
                    Task('4300', 'Новая карта', 'Test3'))
task_ids = ['Task({0},{1},{2})'.format(generateCardNumber(t.card), t.paymentmethods, t.condition)
                for t in variable_for_tests]
@pytest.mark.parametrize('task', variable_for_tests, ids=task_ids)


class TestMerchantInvoice:

    def test_invoice(self, api, configs, middleware_fixture, task, clear_users):
        clear = clear_users
        # Создание тела запроса инвойса рассрочки
        data_invoice =  {
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
        data_invoice["orderId"] = str(uuid4())
        current_date = datetime.datetime.utcnow()
        expire_date = current_date + datetime.timedelta(days=365)
        data_invoice["expireDate"] = str(expire_date.strftime("%Y-%m-%d"))
        data_invoice["merchantDate"] = str(datetime.datetime.utcnow().strftime("%Y-%m-%d"))

        # Отправка запроса инвойса, получение ответа парсинг и проверки статуса и содержание paymentUrl
        api_key = configs['Creditional']['merchant']['apikey']
        request_create_invoice = api.create_invoice(api_key, post=json.dumps(data_invoice))
        assert request_create_invoice.status_code == 200
        response = json.loads(request_create_invoice.text)
        assert response['status'] == "Created" and response['paymentUrl'] != None

        # Открытие браузера для перехода по ссылке ответа создания инвойса (paymentUrl)
        first = middleware_fixture[0]
        test_page = paymentpage(first)

        # Переход по ссылке
        test_page.go(response['paymentUrl'])

        # Заполнение логина на странице платежа
        test_page.input_login(configs['Creditional']['Client']['msisdn'][1:])
        test_page.click_continue() # Нажатие кнопки "Продолжить"
        test_page.imput_code()
        if test_page.text_error():
            test_page.repeat_code()
            test_page.imput_code()
        # Нажатие на кнопку "Продолжить"
        if test_page.check_buttn_cont():
            test_page.click_button_continue()
        # Проверка что данные профиля заполнены
        if test_page.text_info_manualData():
            test_page.button_manual_data()
            test_page.data_user_leftColumn()
            test_page.date_user_rightColumn()
            test_page.button_save_data()
        # Выбор рассрочки, проверка содержания описания рассрочки, нажатие далее
        test = ["Пилот 6 недель", "Пилот 3 дня", "Пилот 4 месяца", "Пилот 6 месяцев"]
        test_random = ''.join(random.choice(test))
        if test_page.check_buttn_cont():
            test_page.click_button_continue()
        test_page.choose_conditions(test_random)
        test_page.click_choose_conditions(test_random)
        # Выбор инструмента и ввод кода, отправить в рассрочку
        test_page.page.wait_for_selector('.pay-method__masked-name', timeout= 60000)
        test_page.choose_methods_pyament('Новая карта')
        test_page.click_send_pay_impl()
        # Генерация номера карты, заполнение формы, нажатие кнопки pay формы
        testing_card = generateCardNumber('4100')
        test_page.page.wait_for_selector('.popup-add-card', timeout= 60000)
        test_page.check_title()
        test_page.input_cards(testing_card, '12/25', '111')
        # Проверка сообщений об успехе оформления рассрочки
        test_page.success_message()
        test_page.check_text()
        # Клик на кнопку "Открыть личный кабинет"
        test_page.click_button_lk()

        '''# Выбор рассрочки, проверка содержания описания рассрочки, нажатие далее
        test_page.choose_conditions(task.condition)
        test_page.click_choose_conditions(task.condition)

        # Выбор инструмента и ввод кода, отправить в рассрочку
        test_page.choose_methods_pyament(task.paymentmethods)
        test_page.imput_code()
        test_page.click_send_pay_impl()

        # Генерация номера карты, заполнение формы, нажатие кнопки pay формы
        # number_card = generateCardNumber(task.cardprefix)
        # print('Сгенерирован номер карты: {0}'.format(number_card))
        test_page.input_cards(task.card, '12/25', '111')

        # Исходя из префикса, финальный экран будет отличатся или потребует доп.действий
        if task.cardprefix[:4] in ['4100','4200']:
            if task.cardprefix[:4] == '4200': # Для данного префикса требуется 3d верификация
                test_page.third_confirm_secure_button()
            test_page.check_finally_screen('Рассрочка успешно оформлена') # Проверка успешной надписи
        elif task.cardprefix[:4] == '4300':
            test_page.check_finally_screen('fail') # Проверка НЕ успешной надписи (не работает, приходит успех)'''