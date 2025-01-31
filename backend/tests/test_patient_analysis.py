import unittest
from backend.app import create_app, db
from backend.app.models.patient_analysis import PatientAnalysis

class TestPatientAnalysis(unittest.TestCase):
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

    def test_add_patient_data(self):
        response = self.client.post('/patient/add', json={
            'patient_id': 1,
            'symptoms': 'Cough, Fever',
            'medical_history': 'None',
            'lab_results': 'Normal'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()