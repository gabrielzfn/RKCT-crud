import pytest 
import requests


BASE_URL = "http//127.0.0.1:5000"
tasks = []

def test_create():
    data_task = {
        "title": "Nova tarefa",
        "description": "Descrição da tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=data_task)
    assert response.status_code == 200