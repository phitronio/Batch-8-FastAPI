from test.test_main import client 
from main import app
from fastapi import status
from router.auth import get_current_user
from database import SessionLocal
from models import Todos

def override_get_current_user():
    return {
        'id': 1,
        'username': 'testuser'
    }


def test_todo():

    db = SessionLocal()

    # remove old test data if its exist
    db.query(Todos).filter(Todos.id == 99).delete()

    todo = Todos(
        id = 99,
        title = 'Testing',
        description = 'Testing',
        priority = 5,
        completed = True,
        owner_id = 1
    )

    db.add(todo)
    db.commit()


app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_todos():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK


def test_read_specific_todos():
    response = client.get('/todo/99')
    assert response.status_code == status.HTTP_200_OK


def test_create_todo():

    db = SessionLocal()
    # remove old test data if its exist
    db.query(Todos).filter(Todos.id == 0).delete()
    db.commit()

    request_data = {
        "id": 0,
        "title": "string",
        "description": "string",
        "priority": 1,
        "completed": True
    }
    response = client.post('/create/', json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {'message' : 'To do created successfully'}


def test_update_todo():

    request_data = {
        "title": "Updated"
    }
    response = client.put('/edit/99', json=request_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message' : 'To do updated successfully'}


def test_delete_todo():

    response = client.delete('/delete/99')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message' : 'To do deleted successfully'}