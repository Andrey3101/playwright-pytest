from pages.profile import ProfilePage


class TestProfile:

    '''def test_profile(self, autharization_fixture, check_user):
        check = check_user
        auth_page = autharization_fixture
        # запуск страницы
        auth_test = ProfilePage(auth_page.page)
        # нажатие на кнопку "Профиль"
        auth_test.menu_profile()
        # Проверка отображения элементов
        auth_test.my_data()
        auth_test.my_notification()
        auth_test.my_support()
        auth_test.logo_seven()
        auth_test.my_first_name()
        auth_test.my_name()
        auth_test.my_middle_name()
        auth_test.my_pasport()
        # Нажатие на кнопку "Редактировать"
        auth_test.button_edit_click()
        # Внесение изменений в поля
        auth_test.edit_first_name()
        auth_test.edit_name()
        auth_test.edit_middle_name()
        auth_test.edit_serial_number()
        auth_test.edit_code_pasport()
        auth_test.edit_address()
        auth_test.edit_date_birth()
        auth_test.edit_date_issue()
        # Сохранение внесенных изменений
        auth_test.button_save()
        # Проверка получения сообщения об успехе внесенных изменений
        auth_test.message_success()

    def test_negative_profile(self, autharization_fixture, check_user):
        check = check_user
        auth_page = autharization_fixture
        # запуск страницы
        auth_test = ProfilePage(auth_page.page)
        # нажатие на кнопку "Профиль"
        auth_test.menu_profile()
        # Проверка отображения элементов
        auth_test.my_data()
        auth_test.my_notification()
        auth_test.my_support()
        auth_test.logo_seven()
        auth_test.my_first_name()
        auth_test.my_name()
        auth_test.my_middle_name()
        auth_test.my_pasport()
        # Нажатие на кнопку "Редактировать"
        auth_test.button_edit_click()
        # Изменить паспортные данные на некорректные числа (без пробела)
        auth_test.edit_negative_serNum()
        # Нажатие на кнопку "Сохранить"
        auth_test.button_save()
        # Проверка отображения сообщения об ошибке
        # Проверки ниже закомментил, связано с тем что данное поведение не правильно
        auth_test.message_error()
        # Проверка текста и кнопок в появившемся окне
        auth_test.window_error()
        auth_test.window_error_text()
        auth_test.window_error_button_edit()
        auth_test.window_error_button_GU()
        auth_test.window_error_button_cancel()

    def test_field_negatve(self, autharization_fixture, check_user):
        check = check_user
        auth_page = autharization_fixture
        # запуск страницы
        auth_test = ProfilePage(auth_page.page)
        # нажатие на кнопку "Профиль"
        auth_test.menu_profile()
        # Проверка отображения элементов
        auth_test.my_data()
        auth_test.my_notification()
        auth_test.my_support()
        auth_test.logo_seven()
        auth_test.my_first_name()
        auth_test.my_name()
        auth_test.my_middle_name()
        auth_test.my_pasport()
        # Нажатие на кнопку "Редактировать"
        auth_test.button_edit_click()
        # Ввод текста более 50 символов и проверка отображения текста
        auth_test.edit_negative_fname()
        auth_test.text_error_message_fname()
        auth_test.edit_negative_name()
        auth_test.text_error_message_name()
        auth_test.edit_negative_mname()
        auth_test.text_error_message_mname()'''

    def test_email(self,autharization_fixture, check_user):
        check = check_user
        auth_page = autharization_fixture
        # запуск страницы
        auth_test = ProfilePage(auth_page.page)
        # нажатие на кнопку "Профиль"
        auth_test.menu_profile()
        # нажатие на кнопку "Профиль"
        auth_test.menu_profile()
        # Проверка отображения элементов
        auth_test.my_data()
        auth_test.my_notification()
        auth_test.my_support()
        auth_test.logo_seven()
        auth_test.my_first_name()
        auth_test.my_name()
        auth_test.my_middle_name()
        auth_test.my_pasport()
        # Нажатие на кнопку "Редактировать"
        auth_test.button_edit_email()
        # Внесение данных в поле email
        auth_test.check_text_email()
        auth_test.edit_email()
        # Нажатие на кнопку "Сохранить"
        auth_test.button_save_email()
        # Проверка отображения иконок, текста и кнопки "Отправить повторно"
        auth_test.text_email()
        auth_test.icons()
        auth_test.email_response()