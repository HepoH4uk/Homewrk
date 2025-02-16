from unittest.mock import patch, Mock
from src.external_api import amount_transactions


@patch("requests.request")
def test_amount_transactions_1(mock_get, rub=100):
    mock_respone = Mock()
    mock_respone.json.return_value = {"amount": {}, }
    mock_get.return_value = mock_respone
    assert rub == 100


@patch("requests.request")
def test_amount_transactions(mock_get):
    transaction = {"operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }}}
    mock_respone = Mock()
    mock_respone.status_code = 200
    mock_respone.json.return_value = {"result": 100}
    mock_get.return_value = mock_respone
    result = amount_transactions(transaction)
    assert amount_transactions(transaction) == result
