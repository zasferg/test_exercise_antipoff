from .testlib.api_requests import set_query
from .testlib.api_requests import get_history
from .testlib.api_requests import get_ping
from .testlib.api_requests import get_result

import datetime
from datetime import date ,time, timezone
import pytz


def get_test_time():

    testtime = datetime.datetime.combine(
        date.today(), time(12, 34), tzinfo=timezone.utc
    )
    return testtime.isoformat()


def test_query(
    postgre_fixture,
    postgre_fixture_external
    ):
    """Данный тест проверяет правильность ввода кадастровых данных"""
    test_time = get_test_time()
    data = {
        "id":1,
        "cadastral_number": "123456789",
        "latitude": 50.456,
        "longitude": 30.523,
        # "result": True,
        "query_time": test_time
    }

    result = set_query(data=data)
    assert result.status_code == 200





def test_ping():
    """Тест проверки ответа от сервера"""
    response_from_db = get_ping()
    print(response_from_db)
    assert response_from_db['status'] == 'Сервер работает'


def test_response(
        postgre_fixture,
        add_query
    ):
    """Этот тест проверяет наличие конеретной кадастровой записи в базе данных"""

    expected_cadastral_number = "123456789"
    response_from_db = get_result(cadastral_number=expected_cadastral_number)
    cadastral_number_from_db = response_from_db[0]["cadastral_number"]

    assert  cadastral_number_from_db == expected_cadastral_number

def test_history(
        postgre_fixture,
        add_history):
    """ В этом тесте в бд создается несколько записей данных об обращении к кадастровой информации."""

    result = get_history(cadastral_number="123456789:130")
    assert len(result) == 2



