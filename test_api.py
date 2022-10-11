#test_api.py
"""
Employee class tests.
"""
import unittest
import requests
from api import api_instagram
from cookies import HEADERS,COOKIES

cookies=COOKIES
headers=HEADERS

class TestInstagram(unittest.TestCase):
    """Test the compute_payout method of the Employee class."""

    def setUp(self):
        """Set up test fixtures."""
        CUENTA='inkabet'
        self.ig = api_instagram(cuenta=CUENTA)

    # def test_api_instagram(self):
    #     """Whether payout is correctly computed in case of no commission and 10 hours worked."""
    #     #self.cuenta = 10.0
    #     self.assertAlmostEqual(self.ig.user_profile(), 1)

    # async def test_response(self):
    #     events.append("test_response")
    #     response = await self._async_connection.get("https://example.com")
    #     self.assertEqual(response.status_code, 200)
    #     self.addAsyncCleanup(self.on_cleanup) 

    def test_user_profile(self):
        self.assertEqual(200, self.ig.user_profile().status_code) #self.assertEqual(200,response.status_code)

    def test_query_post(self):
        params = {
            "query_hash": "69cba40317214236af40e7efa697781d",
            "variables": '{"id":"468542719", "first":12,"after":"" }'
        }
        self.assertEqual(200, self.ig.query_post(params).status_code) #self.assertEqual(200,response.status_code)

     

if __name__ == "__main__":
    unittest.main()