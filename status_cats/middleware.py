"""
Allows your Django app to render HTTP status cat pics when it returns various
status codes.
"""

from django.shortcuts import render

from status_cats.constants import CAT_URLS, CAT_TEMPLATE, BASE_TEMPLATE

"""
TODO:

* add config options:
    * a list of status codes to modify only headers - should be named constants
      and should contain 200 by default
    * CAT_TEMPLATE, BASE_TEMPLATE should get from settings
      but have a default (content-block-name looks hard)
* add version info
* add README, including tested versions/dependencies and cat template override instructions
* add to pypi
* add proper credit to https://www.flickr.com/photos/girliemac/sets/72157628409467125/
* consider setting to handle only RFC compliant ones?
* deal with RFC-compliant codes not present in photo set
* fill in _render_with_header
* use _render_with_header for non-template get()

NEEDS TESTING:
* write function to capture response and render associated cat template
* write views that return each status code for testing
* write tests


DONE:

"""

class StatusCatMiddleware(object):

    def _render_with_cat(self, request, response):
        """
        This renders the specified CAT_TEMPLATE with context of cat_url
        (image URL for the relevant HTTP status cat) and status_code.
        """
        status_code = response.status_code
        cat_url = CAT_URLS[int(status_code)]
        return render(request, CAT_TEMPLATE,
            {'cat_url': cat_url,
             'base_template': BASE_TEMPLATE,
             'status_code': status_code})

    def _render_with_header(self, request, response):
        """
        This adds the image URL for the relevant status code to the
        HTTP headers, but does not otherwise change the HTTP response.
        """
        pass

    def process_exception(self, request, exception):
        # read up on django exception handling and determine if this should
        # ever throw anything other than 500
        pass

    def process_template_response(self, request, response):
        return self._render_with_cat(request, response)

    def process_response(self, request, response):
        return self._render_with_cat(request, response)
