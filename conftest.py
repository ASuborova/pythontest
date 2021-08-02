import pytest
from fixture.application import Application
import json
import os.path
import importlib
import jsonpickle

fixture_create = None
target = None


@pytest.fixture
def app(request):
    global fixture_create
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture_create is None or not fixture_create.is_valid():
        fixture_create = Application(browser=browser, BUrl=target['BUrl'])
    fixture_create.ses_h.is_login(loginname=target['username'], password=target['password'])
    return fixture_create


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture_create.ses_h.is_logout()
        fixture_create.district()
    # yield fixture_create
    request.addfinalizer(fin)
    return fixture_create


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as file_json:
        return jsonpickle.decode(file_json.read())
