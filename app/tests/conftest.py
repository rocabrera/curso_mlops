import pytest
from fastapi.testclient import TestClient
from src.main import app
from typing import Any

@pytest.fixture
def client():
    yield TestClient(app)
