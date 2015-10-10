from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from status_cats.constants import CAT_URLS

class StatusCatTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cat_ubiquity(self):
        for cat_url in CAT_URLS:
            url = reverse('status_code_response', args=(cat_url,))
            response = self.client.get(url)

            self.assertEqual(int(response.status_code), int(cat_url))
            self.assertEqual(response['X-Status-Cat'], CAT_URLS[cat_url])

            if cat_url not in settings.STATUS_CATS_HEADER_ONLY:
                self.assertEqual(CAT_URLS[cat_url], response.context['cat_url'])
