from pages.notification import NotificationPage

class TestNotification:

    def test_notification(self, autharization_fixture):
        # Фикструра с авторизацией по номеру телефона
        login_page = autharization_fixture
        # запуск страницы
        auth_test = NotificationPage(login_page.page)
        # Переход на страницу "Профиль"
        auth_test.menu_profile()
        # Проверка меню
        auth_test.my_first_name()
        auth_test.my_name()
        auth_test.my_middle_name()
        auth_test.my_address()
        # Переход в раздел "Нотификации"
        auth_test.notification()
        # Проверка отображения чек-боксов
        auth_test.checkbox_email()
        auth_test.checkbox_push()
        auth_test.checkbox_sms_service()
        auth_test.checkboxing_advertising()
        # Проверка активности чек-бокса
        auth_test.checkbox_sms_status()