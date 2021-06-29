import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app():
    fixture_create = Application()
    yield fixture_create
    Application.district(fixture_create)
