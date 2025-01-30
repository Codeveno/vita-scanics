from backend.app.routes.telemedicine import start_consultation

def test_telemedicine():
    response = start_consultation(1)
    assert response["message"] == "Telemedicine session started for patient 1"
