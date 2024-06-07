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
    postgre_fixture
    ):

    test_time = get_test_time()
    data = {
        "id":1,
        "cadastral_number": "123456789",
        "latitude": 50.456,
        "longitude": 30.523,
        "result": True,
        "query_time": test_time
    }

    result = set_query(data=data)
    assert result.status_code == 200


def test_response(
        postgre_fixture,
        add_query
    ):
    response_from_db = get_result(id = add_query.id)
    result_returned_drom_db = response_from_db["result_field"]

    assert result_returned_drom_db == add_query.result


def test_ping():
    
    response_from_db = get_ping()
    assert response_from_db['status'] == 'Сервер работает'


def test_history(
        postgre_fixture,
        add_query
    ):
    response_from_db = get_history(carastral_id=add_query.cadastral_number)
    cadastral_number_from_db = response_from_db[0]["cadastral_number"]

    assert  cadastral_number_from_db == add_query.cadastral_number
    


