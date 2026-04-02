from app import app
import json

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_get_todos():
    client = app.test_client()
    response = client.get('/todos')
    assert response.status_code == 200

def test_add_todo():
    client = app.test_client()
    response = client.post('/todos',
        data=json.dumps({"task": "Learn CI/CD"}),
        content_type='application/json')
    assert response.status_code == 201

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200