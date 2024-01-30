import string

import pytest
from playwright.sync_api import Page


@pytest.fixture
def middleware_fixture(tracing_fixture):
    print('\nmiddleware_fixture entered')
    req = []
    resp = []
    page = tracing_fixture
    page.on("request", lambda request: req.append((request.method, request.url)) if '/api' in request.url else None)
    # if '/api' in request.url
    # req.append((request.method, request.url))
    page.on("response", lambda response: resp.append(response) if '/api' in response.url else None)
    yield page, req, resp
    print('\nmiddleware_fixture exited')
    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))
