import unittest
from unittest.mock import patch
from src.utilities.ping_website import ping_website

class TestPingWebsite(unittest.TestCase):

    def setUp(self) -> None:
        self._url = 'http://www.google.com'

    def tearDown(self) -> None:
        pass

    def test_ping_the_website(self) -> None:
        with patch('src.utilities.ping_website.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            self.assertEqual(ping_website(self._url), 'Up')

if __name__ == '__main__':
    unittest.main()
