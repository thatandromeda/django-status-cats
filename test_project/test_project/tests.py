from django.test import TestCase, RequestFactory
from django.test.client import Client

from status_cats.constants import CAT_URLS
from status_cats.middleware import StatusCatMiddleware

class StatusCatTestCase(TestCase):
    def setUp(self):
        self.middleware = StatusCatMiddleware()
        self.request = RequestFactory()
        self.client = Client()

    def test_render_with_cats(self):
        for cat_url in CAT_URLS:
            response = self.client.get('status_code_response', args=(cat_url,))
            self.assertEqual(response.status_code, cat_url)
            self.assertIn(CAT_URLS[cat_url], response.context)

    def test_render_headers(self):
        # need to test expected behavior when we decide what it is
        assert False
