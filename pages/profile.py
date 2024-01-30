from playwright.sync_api import Page
import re
import random
from datetime import datetime, timedelta

class ProfilePage():

    def __init__(self, page: Page):
        self.page = page

    def menu_profile(self):
        self.page.get_by_role("link", name="Профиль").click()

    def button_edit_click(self):
        self.page.locator(".personal-data__btn").first.click()

    def my_data(self):
        self.page.get_by_role("link", name="Мои данные").is_visible()

    def my_notification(self):
        self.page.get_by_role("link", name="Нотификации").is_visible()

    def my_support(self):
        self.page.get_by_role("link", name="Поддержка").is_visible()
    
    def logo_seven(self):
        self.page.locator(".header__logo").is_visible()

    def my_first_name(self):
        self.page.get_by_text("Фамилия*").is_visible()

    def my_name(self):
        self.page.get_by_text("Имя*").is_visible()

    def my_middle_name(self):
        self.page.get_by_text("Отчество").is_visible()

    def my_pasport(self):
        self.page.get_by_text("Паспорт").is_visible()

    def my_email(self):
        self.page.get_by_text("E-mail")

    def edit_first_name(self):
        names = ''.join(random.choice('йцукеннгшщзфывапролджэячсмитьбю') for i in range(5))
        self.page.locator(".input-el__inp-field").first.fill(names)

    def edit_name(self):
        names = ''.join(random.choice('йцукеннгшщзфывапролджэячсмитьбю') for i in range(3))
        self.page.locator("div:nth-child(2) > .input-el > .input-el__inp > .input-el__inp-field").first.fill(names)

    def edit_middle_name(self):
        names = ''.join(random.choice('йцукеннгшщзфывапролджэячсмитьбю') for i in range(2))
        self.page.locator("div:nth-child(3) > .input-el > .input-el__inp > .input-el__inp-field").fill(names)

    def edit_email_neg(self):
        name = ''.join(random.choice('qwertyuipoasdfghjklzxcvbnm') for i in range(10))
        e_mail = name + "@gmail.com"
        self.page.get_by_text("E-mail").fill(e_mail)

    def edit_email(self):
        self.page.get_by_role("textbox").fill('test.qa.alta@gmail.com')

    def check_text_email(self):
        self.page.get_by_text("E-mail").is_visible()
    def edit_serial_number(self):
        test_ser = ''.join(random.choice('1234567890') for i in range(2))
        test_serial = ''.join(random.choice('1234567890') for i in range (2))
        test_number = ''.join(random.choice('1234567890') for i in range(6))
        pasport_data = test_ser + ' ' + test_serial + ' ' + test_number
        self.page.locator("div:nth-child(2) > .personal-data__block > div:nth-child(2) > .input-el > .input-el__inp > .input-el__inp-field").fill(pasport_data)

    def edit_negative_serNum(self):
        test_number = ''.join(random.choice('1234567890') for i in range(12))
        self.page.locator("div:nth-child(2) > .personal-data__block > div:nth-child(2) > .input-el > .input-el__inp > .input-el__inp-field").fill(test_number)

    def edit_code_pasport(self):
        self.page.locator("div:nth-child(4) > .input-el > .input-el__inp > .input-el__inp-field").fill('123-456')

    def edit_address(self):
        self.page.locator("textarea").fill('test address')

    def edit_date_issue(self):
        date = datetime.now() - timedelta(days=1)
        dateti = date.strftime("%d.%m.%Y")
        self.page.locator("div:nth-child(3) > .date-picker-el > .date-picker-el__picker > .mx-datepicker > .mx-input-wrapper > .date-picker-el__picker-field").fill(dateti)

    def edit_date_birth(self):
        current_date = datetime.now() - timedelta(days= 365 * 18)
        date_birthday = current_date.strftime("%d.%m.%Y")
        self.page.locator(".date-picker-el__picker-field").first.fill(date_birthday)

    def edit_negative_fname(self):
        name = ''.join(random.choice('qwertyuipoasdfghjklzxcvbnm') for i in range(51))
        self.page.locator(".input-el__inp-field").first.fill(name)

    def edit_negative_name(self):
        name = ''.join(random.choice('qwertyuipoasdfghjklzxcvbnm') for i in range(10))
        self.page.locator("div:nth-child(2) > .input-el > .input-el__inp > .input-el__inp-field").first.fill(name)

    def edit_negative_mname(self):
        name = ''.join(random.choice('qwertyuipoasdfghjklzxcvbnm') for i in range(10))
        self.page.locator("div:nth-child(3) > .input-el > .input-el__inp > .input-el__inp-field").fill(name)

    def button_save(self):
        self.page.get_by_role("button").click()

    def my_address(self):
        self.page.get_by_text("Адрес*").is_visible()

    def button_cancel(self):
        self.page.locator(".personal-data__headline-block > div").click()

    def message_success(self):
        self.page.get_by_text("Данные успешно сохранены").is_visible()

    def message_error(self):
        self.page.locator("div").filter(has_text=re.compile(r"^Произошла ошибка при сохранении персональных данных$")).nth(2)

    def window_error(self):
        self.page.get_by_text("Проверьте введенные данные").is_visible()

    def window_error_text(self):
        self.page.get_by_text("Возможно, данные указаны некорректно").is_visible()

    def window_error_button_GU(self):
        self.page.get_by_role("button", name="Идентификация через Госуслуги").is_visible()

    def window_error_button_cancel(self):
        self.page.get_by_role("button", name="Отменить").is_visible()

    def window_error_button_edit(self):
        self.page.get_by_role("button", name="Вернуться к редактированию").is_visible()

    def button_edit_email(self):
        self.page.locator(".personal-data__email-icons > .personal-data__btn").click()

    def button_save_email(self):
        self.page.locator(".personal-data__email-icons > div").first.click()

    def text_email(self):
        self.page.get_by_text("Вам отправлено письмо для подтверждения адреса электронной почты. Подтвердите по").is_visible()
    
    def icons(self):
        self.page.locator(".personal-data__email-icons").is_visible()

    def email_response(self):
        self.page.get_by_text("Отправить повторно").is_visible()

    def text_error_message_fname(self):
        self.page.get_by_text("Введено больше 50 символов").is_visible()

    def text_error_message_name(self):
        self.page.get_by_text("Введено больше 50 символов").nth(1).is_visible()

    def text_error_message_mname(self):
        self.page.get_by_text("Введено больше 50 символов").nth(2).is_visible()