from playwright.sync_api import Page
import re


class NotificationPage:

    def __init__(self, page: Page):
        self.page = page

    def menu_profile(self):
        self.page.get_by_role("link", name="Профиль").click()

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

    def my_address(self):
        self.page.get_by_text("Адрес*").is_visible()

    def text_service_push(self):
        self.page.get_by_role("heading", name="Сервисные уведомления").is_visible()

    def text_advertising(self):
        self.page.get_by_role("heading", name="Рекламные уведомления").is_visible()

    def checkboxing_advertising(self):
        self.page.get_by_text("SMSPushE-mail", exact=True).is_visible()

    def checkbox_sms_service(self):
        self.page.locator(".checkbox-el__group").first.is_visible()

    def checkbox_push(self):
        self.page.locator("div:nth-child(2) > .checkbox-el > .checkbox-el__group").first.is_visible()

    def checkbox_email(self):
        self.page.locator("div").filter(has_text=re.compile(r"^E-mail$")).first.is_visible()

    def click_checkbox_sms_servie(self):
        self.page.locator(".checkbox-el__check").first.click()

    def notification(self):
        self.page.get_by_role("link", name="Нотификации").click()

    def checkbox_sms_status(self):
        self.page.locator(".checkbox-el__check").first.is_checked() is True

    def checkbox_sms_rec(self):
        self.page.locator("div:nth-child(2) > .notifications__checkboxes > div > .checkbox-el > .checkbox-el__group > .checkbox-el__check").first.click()

    def checkbox_sms_rec_active(self):
        self.page.locator("div").filter(has_text=re.compile(r"^SMSPushE-mail$")).get_by_role("img").is_visible()

    def checkbox_sms_activate_service(self):
        self.page.get_by_role("img").nth(1)