import json
import pytest
import os

from typing import Dict

phase_report_key = pytest.StashKey[Dict[str, pytest.CollectReport]]()


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    rep = yield

    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep

    return rep

@pytest.fixture
def configs(stage):
    configfile = './configs/appsetings.{0}.json'.format(stage)
    assert os.path.exists(configfile)
    configuration = json.load(open(configfile,mode="r", encoding="utf-8"))
    return configuration