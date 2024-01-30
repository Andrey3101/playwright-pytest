from pages.tool import ToolPage
from gen.gen_credit_card_number import generateCardNumber

class TestTool:

    def test_createTool(self, autharization_fixture, clear_users):
        clear = clear_users
        auth_page = autharization_fixture
        # запуск страницы
        tool_test = ToolPage(auth_page.page)
        # Нажатие на раздел  "Инструменты" в меню
        tool_test.click_toolMenu()
        # Проверка отображения кнопок и текста
        tool_test.check_text_toolPay()
        tool_test.check_text_priority()
        tool_test.check_button_createNew()
        # Нажатие на кнопку "Добавить новый"
        tool_test.click_button_createNew()
        # Проверка заголовка и отображения текста с кнопками
        tool_test.check_block_bankCard()
        tool_test.check_block_SBP()
        # Нажатие на кнопку "Добавить"
        tool_test.click_button_bankCard()
        # Генерация карты
        test_card = generateCardNumber('4100')
        # Ожидание и заполнение формы для добавления карты
        tool_test.page.wait_for_selector('.pm-form-card', timeout= 60000)
        tool_test.card_datas(test_card, '04/27', '123')
        # Проверка что привязка успешно оформлена
        tool_test.check_creating_bankCard()
        # Нажатие на кнопку "Вернуться в магазин"
        tool_test.return_InShop()
        card = test_card[:-4]
        tool_test.installments(card)

    def test_tool(self, autharization_fixture, clear_users):
        clear = clear_users
        auth_page = autharization_fixture
        # запуск страницы
        tools_test = ToolPage(auth_page.page)
        # Нажатие на раздел  "Инструменты" в меню
        tools_test.click_toolMenu()
        # Проверка отображения кнопок и текста
        tools_test.check_text_toolPay()
        tools_test.check_text_priority()
        tools_test.check_button_createNew()
        # Нажатие на кнопку "Добавить новый"
        tools_test.click_button_createNew()
        # Проверка заголовка и отображения текста с кнопками
        tools_test.check_block_bankCard()
        tools_test.check_block_SBP()
        # Нажатие на кнопку "Добавить"
        tools_test.click_button_bankCard()
        # Генерация карты
        test_card = generateCardNumber('4200')
        # Ожидание и заполнение формы для добавления карты
        tools_test.page.wait_for_selector('.pm-form-card', timeout= 60000)
        tools_test.card_datas(test_card, '04/27', '123')
        # Проверка отображения кнопки "подтвердить 3-D Secure"
        tools_test.check_button_3d()
        # Нажатие на кнопку "Подтвердить 3-D Secure"
        tools_test.click_button_3d()
        # Проверка что привязка успешно оформлена
        tools_test.check_creating_bankCard()
        # Нажатие на кнопку "Вернуться в магазин"
        tools_test.return_InShop()
        card = test_card[:-4]
        tools_test.installments(card)