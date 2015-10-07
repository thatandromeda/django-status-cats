from django.views.generic import View
from django.http import HttpResponse

from status_cats.constants import CAT_URLS

class StatusCodeView(View):
    """
    This view returns responses with the HTTP status codes specified in
    the URL in order to test the status_cats app.

    As it's solely for testing that property, it doesn't attempt to handle HTTP
    responses correctly.
    """
    def get(self, request, *args, **kwargs):
        code = kwargs['status_code']
        assert int(code) in CAT_URLS.keys()

        response = HttpResponse()
        response.status_code = code
        return response
