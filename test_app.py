import unittest
from app import app

class TestApp(unittest.TestCase):
    # Test for the home route
    def test_home(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Sleep Apnea Detection", response.data)

    # Test for login route
    def test_login(self):
        response = app.test_client().get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login with Google", response.data)

if __name__ == '__main__':
    unittest.main()
