import pytest
from fixture.application import Applicatin


@pytest.fixture()
def app():
    fixture_create = Applicatin()
    yield fixture_create
    Applicatin.district(fixture_create)
