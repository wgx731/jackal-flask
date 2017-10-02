import os
import base64
import json
from datetime import date
import unittest
from app import app, db, default_db_path, default_db_uri
from app.models import User, Stock


def post_json(client, url, data):
    data = json.dumps(data)
    resp = client.post(
        url,
        headers={'Content-Type': 'application/json'},
        data=data
    )
    return resp, json.loads(resp.data)


class JackalFlaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
            app.config['SQLALCHEMY_DATABASE_URI'] = default_db_uri.replace(
                "local", "test"
            )
        with app.app_context():
            db.create_all()
        db.session.add(User(
            'wgx731',
            'wgx731@gmail.com',
            'hackme'
        ))
        db.session.add(Stock(
            date(1985, 11, 1),
            115.48,
            116.68,
            115.48,
            116.28,
            900900,
            'GOOGL'
        ))
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.drop_all()
        if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
            os.unlink(default_db_path.replace("local", "test"))

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        del self.app

    def test_basic_auth_wrong(self):
        result = self.app.get('/index')
        self.assertEqual(result.status_code, 401)
        result = self.app.get(
            '/index',
            headers={
                'Authorization': 'Basic ' +
                base64.b64encode(
                    bytes('wgx731:wrongpass', 'ascii')
                ).decode('ascii')
            }
        )
        self.assertEqual(result.status_code, 401)

    def test_jwt_auth_wrong(self):
        result = self.app.post(
            '/auth'
        )
        self.assertEqual(result.status_code, 400)
        result, jdata = post_json(
            self.app, '/auth', {'username': 'wgx731'}
        )
        self.assertEqual(result.status_code, 400)
        result, jdata = post_json(
            self.app, '/auth', {'password': 'hackme'}
        )
        self.assertEqual(result.status_code, 400)
        result, jdata = post_json(
            self.app, '/auth', {'username': 'wgx731', 'password': 'wrongpass'}
        )
        self.assertEqual(result.status_code, 401)
        result = self.app.get(
            '/index',
            headers={
                'Authorization': 'Bearer wrongtoken'
            }
        )
        self.assertEqual(result.status_code, 401)

    def test_index(self):
        """Assert that user successfully lands on index page"""
        result = self.app.get(
            '/index',
            headers={
                'Authorization': 'Basic ' +
                base64.b64encode(
                    bytes('wgx731:hackme', 'ascii')
                ).decode('ascii')
            }
        )
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'wgx731', result.data)

    def test_home(self):
        """Assert that user successfully lands on home page"""
        result = self.app.get(
            '/',
            headers={
                'Authorization': 'Basic ' +
                base64.b64encode(
                    bytes('wgx731:hackme', 'ascii')
                ).decode('ascii')
            }
        )
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Stocks Table', result.data)
        self.assertIn(b'GOOGL', result.data)

    def test_graph(self):
        """Assert that user successfully lands on graph page"""
        result = self.app.get(
            '/graph',
            headers={
                'Authorization': 'Basic ' +
                base64.b64encode(
                    bytes('wgx731:hackme', 'ascii')
                ).decode('ascii')
            }
        )
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Stocks Graph', result.data)

    def test_stocks_csv(self):
        """Assert that stock csv api returns csv result"""
        result = self.app.get('/api/stocks.csv')
        self.assertEqual(result.status_code, 200)
        self.assertIn('text/csv', result.headers['Content-Type'])
        self.assertIn(b'GOOGL', result.data)

    def test_stocks_txt(self):
        """Assert that stock txt api returns txt result"""
        result = self.app.get('/api/stocks.txt')
        self.assertEqual(result.status_code, 200)
        self.assertIn('text/plain', result.headers['Content-Type'])
        self.assertIn(b'GOOGL', result.data)

    def test_stocks_json(self):
        """Assert that stock json api returns json result"""
        result = self.app.get('/api/stocks.json')
        self.assertEqual(result.status_code, 200)
        self.assertIn('application/json', result.headers['Content-Type'])
        self.assertIn(b'GOOGL', result.data)

    def test_stocks(self):
        """Assert that stock json api returns json result"""
        user = User(
            'wgx731',
            'wgx731@gmail.com',
            'hackme'
        )
        self.assertIn('wgx731@gmail.com', str(user))
        esp, jdata = post_json(
            self.app, '/auth', {
                'username': user.username,
                'password': 'hackme'
            }
        )
        token = jdata['access_token']
        result = self.app.get('/api/stocks', headers={
            'Accept': 'text/csv',
            'Authorization': 'Bearer ' + token
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn('text/csv', result.headers['Content-Type'])
        result = self.app.get('/api/stocks', headers={
            'Accept': 'text/plain',
            'Authorization': 'Bearer ' + token
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn('text/plain', result.headers['Content-Type'])
        result = self.app.get('/api/stocks', headers={
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn('application/json', result.headers['Content-Type'])


if __name__ == '__main__':
    unittest.main()
