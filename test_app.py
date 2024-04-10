import unittest
from unittest.mock import patch
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_user_endpoint_with_valid_token(self):
        with patch('app.verify_token', return_value=True):
            response = self.app.get('/user', headers={'Authorization': 'valid_token'})
            self.assertEqual(response.status_code, 200)

    def test_user_endpoint_with_invalid_token(self):
        with patch('app.verify_token', return_value=False):
            response = self.app.get('/user', headers={'Authorization': 'invalid_token'})
            self.assertEqual(response.status_code, 401)

    def test_time_endpoint(self):
        response = self.app.get('/time')
        self.assertEqual(response.status_code, 200)
        self.assertIn('current_time', response.json)


if __name__ == '__main__':
    unittest.main()
