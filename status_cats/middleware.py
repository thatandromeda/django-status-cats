"""
Allows your Django app to render HTTP status cat pics when it returns various
status codes.
"""

from django.shortcuts import render

from status_cats.constants import CAT_URLS
from status_cats.settings import (CAT_TEMPLATE,
                                  BASE_TEMPLATE,
                                  HEADER_OVERRIDE_ONLY,
                                  HEADER_OVERRIDE_ALL)

"""
TODO:

* add to pypi
* push git version tag

"""

class StatusCatMiddleware(object):

    def _render_with_cat(self, request, status_code, cat_url):
        """
        This renders the specified CAT_TEMPLATE with context of cat_url
        (image URL for the relevant HTTP status cat) and status_code.
        """
        return render(request, CAT_TEMPLATE,
            {'cat_url': cat_url,
             'base_template': BASE_TEMPLATE,
             'status_code': status_code},
             status=status_code)


    def _add_header(self, response, cat_url):
        """
        This adds the image URL for the relevant status code to the
        HTTP headers, but does not otherwise change the HTTP response.

        Use this for HttpResponses that do not render templates (e.g.
        fetching favicons, stylesheets, images, etc.), or when users actually
        want to render their app's template and not cats. (There's no accounting
        for tastes.)
        """
        response['X-Status-Cat'] = cat_url
        return response


    def _inner_process(self, request, response):
        status_code = int(response.status_code)
        cat_url = CAT_URLS[status_code]

        if HEADER_OVERRIDE_ALL or (status_code in HEADER_OVERRIDE_ONLY):
            return self._add_header(response, cat_url)
        else:
            # It's important to render the response first and add the header
            # second, as the render process will overwrite the headers.
            response = self._render_with_cat(request, status_code, cat_url)
            return self._add_header(response, cat_url)


    def process_template_response(self, request, response):
        return self._inner_process(request, response)


    def process_response(self, request, response):
        return self._inner_process(request, response)
