from backend.app.models.patient_analysis import PatientAnalysis

def test_patient_analysis():
    patient_data = {"name": "John Doe", "age": 40, "gender": "Male", "medical_history": "None"}
    analysis = PatientAnalysis(patient_data)
    report = analysis.analyze()
    assert report["health_score"] == 85
