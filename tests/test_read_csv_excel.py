from unittest.mock import patch
import pandas as pd
from src.data_reader import read_file_excel


@patch('pandas.read_excel')
def test_get_data_from_excel(mock_read_excel):
    mock_data = pd.DataFrame({"id": ["1", "2", "3"], "amount": ["554", "323", "111"]})
    mock_read_excel.return_value = mock_data

    result = read_file_excel("fake")
    expected = [
        {"id": "1", "amount": "554"},
        {"id": "2", "amount": "323"},
        {"id": "3", "amount": "111"},
    ]
    assert result == expected
