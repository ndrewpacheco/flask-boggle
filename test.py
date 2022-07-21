from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def test_show_board(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Boggle</h1>', html)
            self.assertIsInstance(session['board'], list)

    def test_check_word(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [['B', 'L', 'U', 'E', 'E'], ['B', 'L', 'U', 'E', 'E'], [
                    'B', 'L', 'U', 'E', 'E'], ['b', 'l', 'u', 'e', 'E'], ['B', 'L', 'U', 'E', 'E'], ]

            resp = client.post(
                '/check-word', json={'guess': 'blue'}, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('ok', html)

    def test_games_played(self):
        with app.test_client() as client:
            resp = client.post("/games-played", json={'games_played': '10'})

            self.assertEqual(resp.status_code, 200)
            self.assertIn("10", resp.json['games_played'])
