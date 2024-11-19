import pytest

from sqlalchemy import insert, select, text
from models import User

# test db connection
def test_db_connection(db_session):
    # Use db_session to interact with the database
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

# test to insert a user
# you can count this as one of your 5 test cases :)
def test_insert_user(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(FirstName="Calista").first()

    assert selected_user is not None
    assert selected_user.LastName == "Phippen"

def test_login(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(FirstName="Calista").first()

    assert selected_user is not None
    assert selected_user.LastName == "Phippen"

def test_sample_data(sample_data):
    assert sample_data["name"] == "Rian"
    assert sample_data["age"] == 18
    assert sample_data["email"] == "rian@rian.com"

def test_failure(sample_data):
    assert sample_data["name"] == "Rain"

def test_success(sample_data):
    assert sample_data["email"] == "rian@rian.com"

def test_database_connection(database_connection):
    pass