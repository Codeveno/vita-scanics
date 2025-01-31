import unittest
from backend.app import create_app, db
from backend.app.models.diagnosis_engine import Diagnosis

class TestDiagnosisEngine(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_diagnosis(self):
        response = self.client.post('/diagnose', json={
            'patient_id': 1,
            'condition': 'Pneumonia',
            'confidence_level': 0.95
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()