from unittest.mock import Mock
from lib.time_error import TimeError

def test_calls_api_to_calulate_time_difference():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    timer_mock = Mock()
    timer_mock.time.return_value = 1700753721


    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {"unixtime":1700753720}

    time_error = TimeError(requester_mock, timer_mock)
    result = time_error.error()
    assert result == -1

    