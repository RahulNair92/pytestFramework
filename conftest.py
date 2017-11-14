import pytest

@pytest.fixture()
def SetUp():
    print("test start")
    yield
    print("test stop")

@pytest.fixture(scope="module")
def onetime(browser):
    if browser == "chrome":
        print("chrome selected")
    print("before module")
    yield
    print("after module")

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
