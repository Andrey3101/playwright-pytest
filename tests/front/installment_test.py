
from pages.my_installment import InstallmentPage

class TestInstallment:

    def test_installment(self, autharization_fixture, purchase_fixture):
        #check = check_user()
        check_purchase = purchase_fixture
        auth_page = autharization_fixture
        installment_test = InstallmentPage(auth_page.page)
        # Нажатие на кнопку "Рассрочки" и проверка отображения текста "Мои рассрочки" и всего что под меню
        installment_test.click_payment()
        installment_test.check_my_payment()
        # Проверка чек-бокса закрытых рассрочек и сортировки
        installment_test.check_close()
        installment_test.element_UI_check()
        # нажатие на кнопку меню с сортировкой и проверка отображения элементов
        installment_test.page.wait_for_selector(".installments__sort-btn", timeout= 60000)
        installment_test.click_button_menu()
        installment_test.check_menu_sort()
        # нажатие на сортировку от новой
        installment_test.click_new_sort()
        # сортировка элементов
        installment_test.sort_copy_new()
        # нажатие на кнопки меню и выбор сортировки от старых
        installment_test.click_button_menu()
        installment_test.click_old_sort()
        installment_test.sort_copy_old()
        # нажатие на кнопку сортировки от менее срочных
        installment_test.click_button_menu()
        installment_test.click_less_urgent()
        # Сортировка элементов
        installment_test.sort_date_pursh_less()
        # Нажатие на кнопку сортировки от старых
        installment_test.click_button_menu()
        installment_test.click_more_urgent()
        # Нажатие на кнопку сортировки от более срочных
        installment_test.sort_date_pursh_more()

    def test_installment_choice(self, autharization_fixture, check_user, purchase_fixture, clear_users):
        clear = clear_users
        check = check_user
        check_pur = purchase_fixture
        auth_page = autharization_fixture
        installment_test = InstallmentPage(auth_page.page)
        # Нажатие на кнопку "Рассрочки" и проверка отображения текста "Мои рассрочки" и всего что под меню
        installment_test.click_payment()
        installment_test.check_my_payment()
        # Проверка чек-бокса закрытых рассрочек и сортировки
        installment_test.check_close()
        installment_test.element_UI_check()
        # Выбор рассрочки
        installment_test.click_installment_input()
        # выбор инструмента
        installment_test.click_icon()


    def test_installment_graf(self, autharization_fixture, check_user, purchase_fixture):
        check = check_user
        check_pur = purchase_fixture
        auth_page = autharization_fixture
        graf_test = InstallmentPage(auth_page.page)
        # Нажатие на кнопку "Рассрочки" и проверка отображения текста "Мои рассрочки" и всего что под меню
        graf_test.click_payment()
        graf_test.check_my_payment()
        # Нажатие на меню в блоке
        graf_test.check_menu_but()
        # Нажатие на кнопку "График платежей"
        graf_test.click_graf_pay()
        # Проверка отображения заголовка "График платежей"
        graf_test.check_graf_text()
        # Нажатие на инструменты
        graf_test.click_instPay()
        # Проверка отображения логотипа
        graf_test.check_datas()