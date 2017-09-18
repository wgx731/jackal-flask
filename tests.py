from app import app
from flask import url_for
import unittest

class JackalFlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        del self.app

    def test_home(self):
        """Assert that user successfully lands on home page"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b'Hello World.')

    def test_welcome(self):
        """Assert that user successfully lands on welcome page"""
        result = self.app.get('/welcome')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Jackal Flask Setup', result.data)


if __name__ == '__main__':
    unittest.main()
