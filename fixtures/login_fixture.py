import pytest

from pages.auth import authPage

@pytest.fixture
def login_fixture(middleware_fixture):
    page = middleware_fixture[0]
    login_page = authPage(page)
    login_page.page = page
    yield login_page


@pytest.fixture
def autharization_fixture(middleware_fixture, portal_url, configs):
    page = middleware_fixture[0] 
    login_page = authPage(page)
    login_page.page = page
    login_page.go(portal_url)
    login_page.input_login(configs['Creditional']['Client']['msisdn'][1:])
    login_page.click_continue()
    login_page.input_code()
    if login_page.text_response():
        login_page.buttun_code_click()
        login_page.input_code()
    if login_page.butn_cont():
        login_page.butn_cont_click()
    # проверка отображения элементов главной страницы
    login_page.logo()
    login_page.user_info()
    yield login_page