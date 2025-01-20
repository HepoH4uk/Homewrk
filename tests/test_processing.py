import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture()
def data_test():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_data_test(data_test):
    assert filter_by_state([
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]) == data_test


@pytest.mark.parametrize(
    "input_data, data_result",
    [
        ([{"id": 1, "state": "EXECUTED"}], ["EXECUTED"]),
        ([{"id": 1, "state": "CANCELED"}], []),
        ([
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "EXECUTED"},
            {"id": 3, "state": "CANCELED"}
            ],["EXECUTED", "EXECUTED"]),
            ([], [])
    ])

def test_filter_by_state(input_data, data_result):
    result = filter_by_state(input_data)
    assert len(result) == len(data_result)
    for item in result:
        assert item['state'] in data_result


@pytest.mark.parametrize(
    "input_data, descending, expected_result",
    [(
                [{"date": "2025-07-03T18:35:29.5123"},
                {"date": "2024-07-03T18:35:29.5123"},
                {"date": "2023-07-03T18:35:29.5123"}],
                True,
                ["2025-07-03T18:35:29.5123", "2024-07-03T18:35:29.5123", "2023-07-03T18:35:29.5123"]),
    ([
                {"date": "2025-07-03T18:35:29.5123"},
                {"date": "2024-07-03T18:35:29.5123"},
                {"date": "2023-07-03T18:35:29.5123"}],
                False,
                ["2023-07-03T18:35:29.5123", "2024-07-03T18:35:29.5123", "2025-07-03T18:35:29.5123"]),

    ([
                {"date": "2023-07-03T18:35:29.5123"},
                {"date": "2023-07-03T18:35:29.5123"},
                {"date": "2023-07-03T18:35:29.5123"}],
                True,
                ["2023-07-03T18:35:29.5123", "2023-07-03T18:35:29.5123", "2023-07-03T18:35:29.5123"])])
def test_sort_by_date(input_data, descending, expected_result):
    result = sort_by_date(input_data, descending)
    actual_dates = [item['date'] for item in result]
    assert actual_dates == expected_result








