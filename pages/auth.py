from playwright.sync_api import Page


class authPage:

    def __init__(self, page: Page):
        self.page = page
        self.button = page.get_by_text("Повторно отправить код")

    def go(self, portal_url):
        self.page.goto(portal_url, wait_until="networkidle")

    def input_login(self, my_login):
        self.page.get_by_placeholder('+7').fill(my_login)

    def login(self):
        self.page.get_by_placeholder('Введите номер телефона')
        return self
    
    def click_continue(self):
        self.page.get_by_role("button", name="Получить код").click()

    def butn_cont(self):
        return self.page.get_by_role("button", name="Продолжить").is_visible()

    def butn_cont_click(self):
        if self.butn_cont():
            self.page.get_by_role("button", name="Продолжить").click()

    def input_code(self):
        self.page.get_by_placeholder("****").fill('1111')

    def n_input_code(self):
        self.page.get_by_placeholder("****").fill('1112')

    def text_response(self):
        self.page.get_by_text("Код введен неверно").is_visible()

    def buttun_code_click(self):
        self.page.get_by_text("Повторно отправить код").click()

    def visible_button_purshCode(self):
        self.page.get_by_text("Повторно отправить код").is_visible()

    def user_info(self):
        self.page.get_by_role("link", name="Главная").is_visible

    def logo(self):
        self.page.locator(".header__logo").is_visible

    def click_installment(self):
        self.page.get_by_role("link", name="Рассрочки")

    def check_installments(self):
        self.page.locator('.grid__c grid__c--l-1-2 grid__c--s-pd-16-16 grid__c--l-pd-24-24')
