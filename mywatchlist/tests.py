from django.test import TestCase

# Create your tests here.

# from django.test import SimpleTestCase

class WatchlistUrlTest(TestCase):
    def test_html_page(self):
        response = self.client.get('/mywatchlist/html',follow=True)
        self.assertEqual(response.status_code, 200)
    def test_json_page(self):
        response = self.client.get('/mywatchlist/json',follow=True)
        self.assertEqual(response.status_code, 200)
    def test_xml_page(self):
        response = self.client.get('/mywatchlist/xml',follow=True)
        self.assertEqual(response.status_code, 200)

    