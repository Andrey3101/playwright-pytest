from playwright.sync_api import Page, expect
import random
from datetime import *


class paymentpage:

    def __init__(self, page: Page):
        self.page = page

    def go(self, url):
        self.page.goto(url, wait_until="networkidle")

    def input_login(self, login):
        self.page.get_by_placeholder('+7').fill(login)

    def text_error(self):
        self.page.wait_for_timeout(3000)
        return self.page.get_by_text("Код недействителен").is_visible()

    def repeat_code(self):
        self.page.get_by_text("Повторно отправить код").click()
    
    def click_continue(self):
        self.page.get_by_role("button", name="Получить код").click()

    def imput_code(self):
        self.page.get_by_placeholder("****").fill('1111') 

    def click_button_continue(self):
        self.page.get_by_role("button", name="Продолжить").click()

    def text_info_manualData(self):
        self.page.wait_for_timeout(5000)
        return self.page.get_by_text("Для оформления рассрочки необходимо предоставить свои персональные данные").is_visible()

    def check_buttn_cont(self):
        self.page.wait_for_timeout(4000)
        return self.page.get_by_role("button", name="Продолжить").is_visible()
    
    def check_esia(self):
        return self.page.get_by_role("button", name="Перейти на портал Госуслуги для предоставления данных").is_visible()
    
    def click_btn_esia(self):
        self.page.get_by_role("button", name="Перейти на портал Госуслуги для предоставления данных").click()

    def manul_data(self):
        self.page.get_by_role("button", name="Предоставить данные вручную").is_visible()

    def check_button_manual_data(self):
        # Левая колонка
        first = ''.join(random.choice('йцукенгшщзхъфывапролджэячсмитьбю') for i in range(10))
        name = ''.join(random.choice('йцукенгшщзхъфывапролджэячсмитьбю') for i in range(5))
        middle = ''.join(random.choice('йцукенгшщзхъфывапролджэячсмитьбю') for i in range(7))
        date = (datetime.strptime("12.07.2000","%d.%m.%Y") - timedelta(days=1)).strftime("%d.%m.%Y")
        self.page.locator(".input-el__inp-field").first.fill("А" +first)
        self.page.locator("div:nth-child(2) > .input-el > .input-el__inp > .input-el__inp-field").fill("Б" +name)
        self.page.locator("div:nth-child(3) > .input-el > .input-el__inp > .input-el__inp-field").first.fill("В" +middle)
        self.page.locator(".date-picker-el__picker-field").first.fill(date)
        # Правая колонка
        pasport_seria = ''.join(random.choice('1234567890') for i in range(4))
        pasport_number = ''.join(random.choice('1234567890') for i in range(6))
        pasport_seria_and_number = pasport_seria + ' ' + pasport_number
        data_date = (datetime.strptime("13.12.2018","%d.%m.%Y") - timedelta(days=4)).strftime("%d.%m.%Y")
        test_address = ''.join(random.choice('йцукенгшщзхъфывапролджэячсмитьбю') for i in range(20))
        self.page.locator("div:nth-child(2) > .personal-data__block > div > .input-el > .input-el__inp > .input-el__inp-field").first.fill(pasport_seria_and_number)
        self.page.locator("div:nth-child(2) > .date-picker-el > .date-picker-el__picker > .mx-datepicker > .mx-input-wrapper > .date-picker-el__picker-field").fill(data_date)
        self.page.locator("div:nth-child(2) > .personal-data__block > div:nth-child(3) > .input-el > .input-el__inp > .input-el__inp-field").fill('500-005')
        self.page.locator("textarea").fill(test_address)
        # Кнопка сохранить
        self.page.get_by_role("button", name="Сохранить").click()

    def button_manual_data(self):
        self.page.get_by_role("button", name="Предоставить данные вручную").click()
        
    def data_user_leftColumn(self):
        # Левая колонка
        first = ''.join(random.choice('йцукенгшщзхъфывапролджэячсмитьбю') for i in range(10))
        name = ''.join(random.choice('йцукенгшщзхъфывапролджэячсмитьбю') for i in range(5))
        middle = ''.join(random.choice('йцукенгшщзхъфывапролджэячсмитьбю') for i in range(7))
        date = (datetime.strptime("12.07.2000","%d.%m.%Y") - timedelta(days=1)).strftime("%d.%m.%Y")
        self.page.locator(".input-el__inp-field").first.fill("А" +first)
        self.page.locator("div:nth-child(2) > .input-el > .input-el__inp > .input-el__inp-field").fill("Б" +name)
        self.page.locator("div:nth-child(3) > .input-el > .input-el__inp > .input-el__inp-field").first.fill("В" +middle)
        self.page.locator(".date-picker-el__picker-field").first.fill(date)

    def date_user_rightColumn(self):
        # Правая колонка
        pasport_seria = ''.join(random.choice('1234567890') for i in range(4))
        pasport_number = ''.join(random.choice('1234567890') for i in range(7))
        pasport_seria_and_number = pasport_seria + ' ' + pasport_number
        data_date = (datetime.strptime("13.12.2018","%d.%m.%Y") - timedelta(days=4)).strftime("%d.%m.%Y")
        test_address = ''.join(random.choice('йцукенгшщзхъфывапролджэячсмитьбю') for i in range(20))
        self.page.locator("div:nth-child(2) > .personal-data__block > div > .input-el > .input-el__inp > .input-el__inp-field").first.fill(pasport_seria_and_number)
        self.page.locator("div:nth-child(2) > .date-picker-el > .date-picker-el__picker > .mx-datepicker > .mx-input-wrapper > .date-picker-el__picker-field").fill(data_date)
        self.page.locator("div:nth-child(2) > .personal-data__block > div:nth-child(3) > .input-el > .input-el__inp > .input-el__inp-field").fill('500-005')
        self.page.locator("textarea").fill(test_address)

    def button_save_data(self):
        self.page.get_by_role("button", name="Сохранить").click()

    def choose_conditions(self, condition):
        self.page.get_by_text(condition, exact=True).click()
    
    def click_choose_conditions(self, text):
        self.page.get_by_role("button", name="Выбрать условия").click()
        self.page.wait_for_load_state('domcontentloaded')
        payment_card = self.page.locator(".payment-card")
        expect(payment_card.first).to_contain_text(text)
        self.page.get_by_role("button", name="Далее").click()
    
    def choose_methods_pyament(self, paymentmethods):
        self.page.get_by_text(paymentmethods).click()

    def check_title(self):
        self.page.get_by_text("Добавить банковскую карту").is_visible()
    
    def click_send_pay_impl(self):
        self.page.get_by_role("button", name="Оплатить рассрочку").click()

    def text_installment_success(self):
        self.page.get_by_role("heading", name="Рассрочка успешно оформлена").is_visible()

    def text_notcorrect_data(self):
        return self.page.get_by_text("Возможно, введенные ранее данные некорректны. Пожалуйста, обновите информацию").is_visible()

    def update_pasport_data(self):
        pasport_seria = ''.join(random.choice('1234567890') for i in range(4))
        pasport_number = ''.join(random.choice('1234567890') for i in range(8))
        pasport_seria_and_number = pasport_seria + ' ' + pasport_number
        self.page.locator("div:nth-child(2) > .personal-data__block > div > .input-el > .input-el__inp > .input-el__inp-field").first.fill(pasport_seria_and_number)

    def clicl_saveData(self):
        self.page.get_by_role("button", name="Сохранить").click()

    def input_cards(self, number_card, exp, cvv):
        self.page.wait_for_timeout(5000)
        frame = self.page.frame_locator("#app iframe")
        card_number_filed = frame.get_by_placeholder("Номер карты")
        card_number_filed.type(number_card, delay=100)
        self.page.wait_for_timeout(3000)
        exp_field = frame.get_by_placeholder("ММ/ГГ")
        exp_field.type(exp, delay=100)
        self.page.wait_for_timeout(3000)
        cvv_field = frame.get_by_placeholder("CVC/CVV")
        cvv_field.type(cvv, delay=100)
        frame.get_by_role("button", name="Продолжить").click()
        

    def third_confirm_secure_button(self):
        self.page.get_by_text("Confirm 3-D Secure").click()

    def check_finally_screen(self, state):
        locator = self.page.locator(".success-installment__title")
        self.page.pause()
        expect(locator).to_contain_text(state)


    def success_message(self):
        self.page.get_by_role("heading", name="Рассрочка успешно оформлена").is_visible()

    def check_text(self):
        self.page.get_by_text("Детали рассрочки доступны в Вашем личном кабинете +7Pay.").is_visible()

    def click_button_lk(self):
        self.page.get_by_role("link", name="Открыть личный кабинет").click()

