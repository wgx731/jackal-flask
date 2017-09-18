from app import app
from flask import url_for
import unittest

class JackalFlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        del self.app

    def test_index(self):
        """Assert that user successfully lands on index page"""
        result = self.app.get('/index')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'wgx731', result.data)

    def test_home(self):
        """Assert that user successfully lands on home page"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'GOOGL', result.data)
        self.assertIn(b'AAPL', result.data)

    def test_stocks_csv(self):
        """Assert that stock csv api returns csv result"""
        result = self.app.get('/api/stocks.csv')
        self.assertEqual(result.status_code, 200)
        self.assertIn('text/csv', result.headers['Content-Type'])
        self.assertIn(b'GOOGL', result.data)
        self.assertIn(b'AAPL', result.data)

    def test_stocks_txt(self):
        """Assert that stock txt api returns txt result"""
        result = self.app.get('/api/stocks.txt')
        self.assertEqual(result.status_code, 200)
        self.assertIn('text/plain', result.headers['Content-Type'])
        self.assertIn(b'GOOGL', result.data)
        self.assertIn(b'AAPL', result.data)

    def test_stocks_json(self):
        """Assert that stock json api returns json result"""
        result = self.app.get('/api/stocks.json')
        self.assertEqual(result.status_code, 200)
        self.assertIn('application/json', result.headers['Content-Type'])
        self.assertIn(b'GOOGL', result.data)
        self.assertIn(b'AAPL', result.data)

    def test_stocks(self):
        """Assert that stock json api returns json result"""
        result = self.app.get('/api/stocks', headers={'Accept': 'text/csv'})
        self.assertEqual(result.status_code, 200)
        self.assertIn('text/csv', result.headers['Content-Type'])
        result = self.app.get('/api/stocks', headers={'Accept': 'text/plain'})
        self.assertEqual(result.status_code, 200)
        self.assertIn('text/plain', result.headers['Content-Type'])
        result = self.app.get('/api/stocks', headers={'Accept': 'application/json'})
        self.assertEqual(result.status_code, 200)
        self.assertIn('application/json', result.headers['Content-Type'])

if __name__ == '__main__':
    unittest.main()

