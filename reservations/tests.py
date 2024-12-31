from django.test import TestCase
from rest_framework.reverse import reverse as api_reverse

# Create your tests here.
class HotelTest(TestCase):
	def setUp(self):
		pass

	def test_hotel_list(self):
		hotel_list_url = api_reverse("hotel-list")
		response = self.client.get(hotel_list_url)
		print(response.data.get("message"))
		# self.assertEqual(response.status_code, 200)