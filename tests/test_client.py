import pytest

from pytrumba import TrumbaClient

@pytest.fixture
def test_trumba_client():
    tc = TrumbaClient()
    tc.params.start_date = "20180227"
    tc.params.end_date = "20180228"
    return tc

def test_get_feed(test_trumba_client):
    response = test_trumba_client.get()
    assert response != ""


def test_get_feed_with_dates(test_trumba_client):
    response = test_trumba_client.get()
    assert response != ""
