from unittest.mock import patch
from src.utils import list_transactions


@patch("os.path.isfile")
def test_list_transactions(mock_func):
    mock_func.return_vlue = False
    result = list_transactions("not_file.json")
    assert result == []
