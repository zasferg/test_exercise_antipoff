from contextlib import contextmanager
import pytest 
from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy import delete
from sqlalchemy import MetaData
from .testlib.data_classes import DataModel
from datetime import datetime



@pytest.fixture(scope="function")
def postgre_fixture():
    database_uri = "postgresql://dbuser:dbpass@localhost:5432/dbname"

    engine = create_engine(database_uri)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    yield engine

    with engine.begin() as connection:
        for table in metadata.tables.values():
            if table.name.startswith("service_"):
                connection.execute(table.delete())


@contextmanager
def add_entity_to_base(postgre_fixture, data):

    metadata = MetaData()
    metadata.reflect(bind=postgre_fixture)

    with postgre_fixture.begin() as conn:
        values = data.model_dump()
        sql_insert = insert(metadata.tables["service_queryhistory"]).values(**values)
        conn.execute(sql_insert)
    yield data


@pytest.fixture
def add_query(postgre_fixture):
        
    data = DataModel(
        id=1,
        cadastral_number="123456789",
        latitude=50.4501,
        longitude=30.5234,
        result=True,
        query_time=datetime.now()
    )

    with add_entity_to_base(postgre_fixture=postgre_fixture,data=data) as entity:
        yield entity

    
