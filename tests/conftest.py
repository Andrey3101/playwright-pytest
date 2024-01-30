import pytest
from fixtures.login_fixture import login_fixture
from fixtures.login_fixture import autharization_fixture
from fixtures.middleware_fixture import middleware_fixture
from fixtures.tracing_fixture import tracing_fixture
from fixtures.conftest import pytest_runtest_makereport
from fixtures.conftest import configs
from fixtures.Api_fixture.API import api
#from fixtures.purchase_fixture import check_purchase_fixture
from fixtures.Api_fixture.API import api_auth
from fixtures.Api_fixture.Auth import login_conf_api
from fixtures.purchase_fixture import purchase_fixture
from fixtures.Api_fixture.API import check_user
from fixtures.Api_fixture.API import get_user_enabled
from fixtures.Api_fixture.API import portal_url
from fixtures.clear_fixture import clear_users

def pytest_addoption(parser):
    """PyTest method for adding custom parameters."""

    parser.addoption("--stage", 
                     action="store", 
                     default='test', 
                     type=str,
                     required=False,
                     help="Set stage: '--stage=test' -> /configs/appsetings.test.json")
    
@pytest.fixture(scope="session")
def stage(request):
    """Handler for --additional_value parameter."""

    return request.config.getoption("--stage")