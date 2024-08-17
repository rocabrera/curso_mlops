from typing import Any
from unittest.mock import patch
from src.loader import InMemoryModelStorage

@patch("src.main.pickle")
def test_prediction(mock_pickle, client):


    with patch("src.main.storage", InMemoryModelStorage()):

        upload_response = client.post(
            "/model/upload",
            files={"file": ("model.pkl", open("tests/models/fake_model.txt", "rb"))}
        )

        key = upload_response.json()["key"]

        response = client.post(
            "/model/predict",
            json={"id":key, "features":[0.1,0.2,0.07,0.14]}
        )
        expected_response = {"storage_used": "InMemoryModelStorage", "data": {"model_answer": 1}}

        assert response.json() == expected_response