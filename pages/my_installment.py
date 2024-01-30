from playwright.sync_api import Page

class InstallmentPage:

    def __init__(self, page: Page):
        self.page = page

    def click_payment(self):
        self.page.get_by_role("link", name="Рассрочки").click()

    def check_my_payment(self):
        self.page.get_by_role("heading", name="Мои рассрочки").is_visible()

    def click_installment_input(self):
        self.page.locator("div:nth-child(6) > .select-payment-tools > .v-popper > .select-payment-tools__selected").first.click()

    def click_icon(self):
        self.page.locator(".select-payment-tools__choice-item-icon > img").first.click()

    def check_close(self):
        self.page.locator("label").is_visible()

    def element_UI_check(self):
        self.page.locator(".installments__sort-btn").is_visible()

    def click_button_menu(self):
        self.page.locator(".installments__sort-btn").click()

    def check_menu_sort(self):
        self.page.get_by_text("По дате создания").is_visible()
        self.page.get_by_text("от новых").is_visible()
        self.page.get_by_text("от старых").is_visible()
        self.page.get_by_text("По дате платежа").is_visible()
        self.page.get_by_text("от более срочных").is_visible()
        self.page.get_by_text("от менее срочных").is_visible()

    def click_new_sort(self):
        self.page.get_by_text("от новых").click()

    def click_less_urgent(self):
        self.page.get_by_text("от менее срочных").click()

    def click_more_urgent(self):
        self.page.get_by_text("от более срочных").click()

    def click_old_sort(self):
        self.page.get_by_text("от старых").click()

    def check_invoice(self, text):
        self.page.get_by_text(text).is_visible()

    def sort_copy_new(self):
        elements = self.page.query_selector_all('.installment-card__col installment-card__col--desktop.installment-card__scheduled-date')
        elements_dict = {}
        for element in elements:
            date = element.inner_text().split('\n')
            if len(date) > 1:
                date = date[1].strip()
                elements_dict[' '.join(date)] = element
        sorted_elements = [elements_dict[date] for date in sorted(elements_dict.keys(), reverse= True)]
        for i in range(len(sorted_elements)-1):
            current_date = sorted_elements[i].inner_text().split('\n')[1].strip()
            next_date = sorted_elements[i+1].inner_text().split('\n')[1].strip()
            assert current_date >= next_date, "Элементы не найдены"

    def sort_copy_old(self):
        elements = self.page.query_selector_all('.installment-card__col installment-card__col--desktop.installment-card__scheduled-date')
        elements_dict = {}
        for element in elements:
            date = element.inner_text().split('\n')
            if len(date) > 1:
                date = date[1].strip()
                elements_dict[' '.join(date)] = element
        sorted_elements = [elements_dict[date] for date in sorted(elements_dict.keys(), reverse= True)]
        for i in range(len(sorted_elements)-1):
            current_date = sorted_elements[i].inner_text().split('\n')[1].strip()
            next_date = sorted_elements[i+1].inner_text().split('\n')[1].strip()
            assert current_date >= next_date, "Элементы не найдены"

    def sort_date_pursh_less(self):
        elements = self.page.query_selector_all('.installment-card__col installment-card__col--desktop.installment-card__scheduled-date')
        elements_dict = {}
        for element in elements:
            date = element.inner_text().split('\n')
            if len(date) > 1:
                date = date[1].strip()
                elements_dict[' '.join(date)] = element
        sorted_elements = [elements_dict[date] for date in sorted(elements_dict.keys(), reverse= True)]
        for i in range(len(sorted_elements)-1):
            current_date = sorted_elements[i].inner_text().split('\n')[1].strip()
            next_date = sorted_elements[i+1].inner_text().split('\n')[1].strip()
            assert current_date >= next_date, "Элементы не найдены"

    def sort_date_pursh_more(self):
        elements = self.page.query_selector_all('.installment-card__col installment-card__col--desktop.installment-card__scheduled-date')
        elements_dict = {}
        for element in elements:
            date = element.inner_text().split('\n')
            if len(date) > 1:
                date = date[1].strip()
                elements_dict[' '.join(date)] = element
        sorted_elements = [elements_dict[date] for date in sorted(elements_dict.keys(), reverse= True)]
        for i in range(len(sorted_elements)-1):
            current_date = sorted_elements[i].inner_text().split('\n')[1].strip()
            next_date = sorted_elements[i-1].inner_text().split('\n')[1].strip()
            assert current_date >= next_date, "Элементы не найдены"


    def new_installment(self):
        self.page.get_by_text("Создать новый инструмент")

    def choice_installment(self):
        self.page.get_by_text("Создать новый инструмент").click()
    
    def click_button_dot(self):
        self.page.locator(".installment-card__dots-btn > .svg-icon").first.click()
    
    def check_menu_but(self):
        self.page.get_by_text("График платежей").is_visible()
        self.page.get_by_text("Погасить досрочно").is_visible()
        self.page.get_by_text("Договор поручения").is_visible()

    def click_graf_pay(self):
        self.page.get_by_text("График платежей").click()

    def check_graf_text(self):
        self.page.get_by_role("heading", name="График платежей").is_visible()

    def click_instPay(self):
        self.page.locator(".select-payment-tools__selected")

    def check_datas(self):
        self.page.locator(".header__logo").is_visible()