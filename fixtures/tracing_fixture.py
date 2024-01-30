import pytest
from playwright.sync_api import Browser

from fixtures.conftest import phase_report_key


@pytest.fixture(scope="function")
def tracing_fixture(request, browser: Browser):
    context = browser.new_context(locale="ru-Ru")
    page = context.new_page()
    context.tracing.start(name="trace_%s" % request.node.name, screenshots=True, snapshots=True, sources=True)
    try:
        yield page
    finally:
        report = request.node.stash[phase_report_key]
        if report["setup"].failed:
            print("setting up a test failed or skipped", request.node.nodeid)
        elif ("call" not in report) or report["call"].failed:
            context.tracing.stop(path='./traces/%s_traces.zip' % request.node.name)
        else:
            print('all tests successfull')
            context.tracing.stop(path='./traces/skip.zip')
        context.close()
