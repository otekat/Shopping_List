from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
    # Ensure that flask was set up properly
    def test_home(self):
        home_test = app.test_user(self)
        response = home_test.get('/home', content_type)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        login_test = app.test_user(self)
        response = login_test.get('/login', content_type)
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        signup_test = app.test.user(self)
        response = signup_test.get('/signup', content_type)
        self.assertEqual(response.status_code, 200)



