from unittest.mock import patch, mock_open
import pandas as pd
from src.data_reader import read_file_excel, read_file_csv


@patch('pandas.read_excel')
def test_get_data_from_excel_csv(mock_read):
    mock_data = pd.DataFrame({"id": ["1", "2", "3"], "amount": ["554", "323", "111"]})
    mock_read.return_value = mock_data

    result = read_file_excel("fake")
    expected = [
        {"id": "1", "amount": "554"},
        {"id": "2", "amount": "323"},
        {"id": "3", "amount": "111"},
    ]
    assert result == expected


def test_get_data_from_csv():
    assert read_file_csv("../src/test") == []
