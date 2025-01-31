import unittest
from backend.app import create_app, db
from backend.app.models.recommendation_engine import Recommendation

class TestRecommendations(unittest.TestCase):
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

    def test_add_recommendation(self):
        response = self.client.post('/recommendations/add', json={
            'patient_id': 1,
            'treatment_plan': 'Rest and fluids',
            'medication': 'Paracetamol',
            'warnings': 'None'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()