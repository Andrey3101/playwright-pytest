from playwright.sync_api import Page

class ToolPage:

    def __init__(self, page: Page):
        self.page = page

    def click_toolMenu(self):
        self.page.get_by_role("link", name="Инструменты").click()

    def check_text_toolPay(self):
        self.page.get_by_role("heading", name="Инструменты оплаты").is_visible()

    def check_button_createNew(self):
        self.page.get_by_role("button", name="Добавить новый").is_visible()

    def check_text_priority(self):
        self.page.get_by_text("Приоритетный").first.is_visible()

    def click_button_createNew(self):
        self.page.get_by_role("button", name="Добавить новый").click()

    def check_text_toolPay(self):
        self.page.get_by_role("heading", name="Выберите инструмент оплаты").is_visible()

    def check_block_bankCard(self):
        self.page.get_by_text("Банковская картаДобавить").is_visible()

    def check_block_SBP(self):
        self.page.get_by_text("Система быстрых платежейДобавить").is_visible()

    def click_button_bankCard(self):
        self.page.get_by_text("Добавить").first.click()

    def card_datas(self, card_number, exp, cvc):
        self.page.wait_for_selector('.pm-input-flex').is_checked
        self.page.get_by_placeholder("Номер карты").fill(card_number)
        self.page.get_by_placeholder("ММ / ГГ").fill(exp)
        self.page.get_by_placeholder("CVV / CVC").fill(cvc)
        self.page.get_by_role("button", name="Продолжить").click()

    def check_creating_bankCard(self):
        self.page.locator("div").filter(has_text="Привязка успешно оформлена").nth(3).is_visible

    def return_InShop(self):
        self.page.get_by_role("button", name="Вернуться в магазин").click()

    def installments(self, card_number):
        self.page.locator('.payment-tool-card__pan-masked').get_by_text(card_number)

    def check_button_3d(self):
        self.page.wait_for_selector('.pm-button-confirm', timeout= 60000)

    def click_button_3d(self):
        self.page.get_by_text("Подтвердить 3-D Secure").click()