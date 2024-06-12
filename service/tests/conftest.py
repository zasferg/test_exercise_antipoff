from contextlib import contextmanager
import pytest 
from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy import delete
from sqlalchemy import MetaData
from .testlib.data_classes import DataModel
from .testlib.data_classes import QueryHistory
from datetime import datetime


from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import insert
from contextlib import contextmanager
from datetime import datetime
from typing import Generator, List
from sqlalchemy.engine.base import Engine
from pytest import FixtureRequest

@pytest.fixture(scope="function")
def postgre_fixture() -> Generator[Engine, None, None]:
    database_uri = "postgresql://dbuser:dbpass@localhost:5432/dbname"

    engine = create_engine(database_uri)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    yield engine

    with engine.begin() as connection:
        for table in metadata.tables.values():
            if table.name.startswith("service_"):
                connection.execute(table.delete())

@pytest.fixture(scope="function")
def postgre_fixture_external() -> Generator[Engine, None, None]:
    database_uri = "postgresql://dbuser:dbpass@localhost:5433/dbname"

    engine = create_engine(database_uri)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    yield engine

    with engine.begin() as connection:
        for table in metadata.tables.values():
            if table.name.startswith("external_"):
                connection.execute(table.delete())

@contextmanager
def add_query_to_base(postgre_fixture: Engine, data: List[DataModel]) -> Generator[List[DataModel], None, None]:

    metadata = MetaData()
    metadata.reflect(bind=postgre_fixture)

    with postgre_fixture.begin() as conn:
        for item in data:
            values = item.model_dump()
            sql_insert = insert(metadata.tables["service_cadastral"]).values(**values)
            conn.execute(sql_insert)
    yield data

@contextmanager
def add_history_to_base(postgre_fixture: Engine, data: List[DataModel]) -> Generator[List[DataModel], None, None]:

    metadata = MetaData()
    metadata.reflect(bind=postgre_fixture)

    with postgre_fixture.begin() as conn:
        for item in data:
            values = item.model_dump()
            sql_insert = insert(metadata.tables["service_queryhistory"]).values(**values)
            conn.execute(sql_insert)
    yield data

@pytest.fixture()
def add_query(postgre_fixture: FixtureRequest) -> Generator[List[DataModel], None, None]:
        
    data = [
        DataModel(
        id=1,
        cadastral_number="123456789",
        latitude=50.4501,
        longitude=30.5234,
        result=True,
        query_time=datetime.now()
    ),
        DataModel(
        id=2,
        cadastral_number="987654321",
        latitude=11.1111,
        longitude=22.222,
        result=False,
        query_time=datetime.now()
        )
    ]

    with add_query_to_base(postgre_fixture=postgre_fixture,data=data) as entity:
        yield entity

@pytest.fixture()
def add_history(postgre_fixture:FixtureRequest)-> Generator[List[DataModel], None, None]:
    data = [
        QueryHistory(
        cadastral_number="123456789:130",
        query_date=datetime.now(),
        response_status= 201,
        result = True,
        
        ),
        QueryHistory(
        cadastral_number="123456789:130",
        query_date=datetime.now(),
        response_status= 500,
        result= False,
        ),
        QueryHistory(
        cadastral_number="123456789:131",
        query_date=datetime.now(),
        response_status= 201,
        result= True, 
        )
    ]
    with add_history_to_base(postgre_fixture=postgre_fixture,data=data) as entity:
        yield entity