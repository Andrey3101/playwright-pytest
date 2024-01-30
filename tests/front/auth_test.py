from pages.auth import authPage

class TestAuth:

    '''def test_auth(self, login_fixture, configs, portal_url, check_user, clear_users):
        clear = clear_users
        check = check_user
        l_page = login_fixture
        log_page = portal_url


        log_test = authPage(l_page.page)
        log_test.go(log_page)
        #  указание номера и нажатие на кнопку
        log_test.input_login(configs['Creditional']['Client']['msisdn'][1:])
        log_test.click_continue()
        # ввод кода и нажатие на кнопку
        log_test.input_code()
        # проверка отображения элементов главной страницы
        log_test.logo()
        log_test.user_info()'''

    def test_negative_auth(self, login_fixture, configs, portal_url, check_user, clear_users):
        clear = clear_users
        check = check_user
        log__page = login_fixture
        loging_page = portal_url

        l_test = authPage(log__page.page)
        l_test.go(loging_page)
        # Указание номера и нажатие на кнопку
        l_test.input_login(configs['Creditional']['Client']['msisdn'][1:])
        l_test.click_continue()
        # Ввод кода и нажатие на кнопку
        l_test.n_input_code()
        if l_test.butn_cont():
            l_test.butn_cont_click()
        l_test.page.wait_for_selector('.login__code-resend', timeout= 60000)
        l_test.text_response()

    def test_resend_code(self, login_fixture, configs, portal_url, check_user, clear_users):
        clear = clear_users
        check = check_user
        login_page = login_fixture
        loging_page = portal_url

        login_test = authPage(login_page.page)
        login_test.go(loging_page)

        login_test.input_login(configs['Creditional']['Client']['msisdn'][1:])
        login_test.click_continue()
        # Ввод неправильного кода и нажатие на кнопку
        login_test.n_input_code()
        if login_test.butn_cont():
            login_test.butn_cont_click()
        login_test.text_response()

        # нажатие на кнопку "Повторно отправить код"
        login_test.page.wait_for_selector('.login__code-resend', timeout= 60000)
        login_test.buttun_code_click()

        # Указание верного кода и нажатие на кнопку "Продолжить"
        login_test.input_code()
        if login_test.butn_cont():
            login_test.butn_cont_click()

    def test_three_attempts_code(self, login_fixture, configs, portal_url,check_user, clear_users):
        clear = clear_users
        check = check_user
        login_page = login_fixture
        loging_page = portal_url

        login_test = authPage(login_page.page)
        login_test.go(loging_page)

        # Ввод номера телефона и нажатие на кнопку "Продолжить"
        login_test.input_login(configs['Creditional']['Client']['msisdn'][1:])
        login_test.click_continue()

        # Ввод неправильного кода и проверка текста
        login_test.n_input_code()
        if login_test.butn_cont():
            login_test.butn_cont_click()
        login_test.text_response()

        # ожидание кнопки и нажатие на кнопку "Повторно отправить код"
        login_test.page.wait_for_selector('.login__code-resend', timeout= 60000)
        login_test.buttun_code_click()

        # вторая попытка указания неверного кода и проверка отображения текста с ошибкой
        login_test.n_input_code()
        if login_test.butn_cont():
            login_test.butn_cont_click()
        login_test.text_response()

        # ожидание кнопки и нажатие на кнопку "Повторно отправить код"
        login_test.page.wait_for_selector('.login__code-resend', timeout= 180000)
        login_test.buttun_code_click()
        # Указание неправильного кода
        login_test.n_input_code()
        if login_test.butn_cont():
            login_test.butn_cont_click()
        login_test.text_response()
        login_test.page.wait_for_selector('.login__code-resend', timeout= 185000)

        login_test.text_response()