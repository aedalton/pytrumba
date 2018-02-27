import pytest

from pytrumba import TrumbaClient

@pytest.fixture
def test_trumba_client():
    return TrumbaClient()

def test_get_feed(test_trumba_client):
    response = test_trumba_client.get()
    assert response != ""


def test_get_feed_with_dates(test_trumba_client):
    response = test_trumba_client.get()
    assert response != ""
