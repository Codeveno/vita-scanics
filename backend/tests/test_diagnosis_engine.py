from backend.app.models.diagnosis_engine import DiagnosisEngine

def test_diagnosis_engine():
    engine = DiagnosisEngine()
    diagnosis = engine.predict("test_image_bytes")
    assert diagnosis == "Condition Detected"
