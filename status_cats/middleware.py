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
    * consider a few options for your settings API:
        https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/settings.py
        https://stackoverflow.com/questions/16953293/what-is-the-equivalent-to-django-conf-global-settings-for-third-party-apps
        https://github.com/pinax/django-stripe-payments/blob/master/payments/settings.py
            ^^^ probably this last
* add README, including tested versions/dependencies and cat template override instructions
* add to pypi
* add proper credit to https://www.flickr.com/photos/girliemac/sets/72157628409467125/
* consider setting to handle only RFC compliant ones?
* deal with RFC-compliant codes not present in photo set

NEEDS TESTING:
* write tests


DONE:
* add version info
* write function to capture response and render associated cat template
* write views that return each status code for testing
* fill in _render_with_header
* use _render_with_header for non-template get() <- actually this is on the webserver side


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
             'status_code': status_code},
             status=status_code)


    def _add_header(self, response):
        """
        This adds the image URL for the relevant status code to the
        HTTP headers, but does not otherwise change the HTTP response.

        Use this for HttpResponses that do not render templates (e.g.
        fetching favicons, stylesheets, images, etc.), or when users actually
        want to render their app's template and not cats. (There's no accounting
        for tastes.)
        """
        status_code = response.status_code
        cat_url = CAT_URLS[int(status_code)]
        response['X-Status-Cat'] = cat_url
        return response


    def _inner_process(self, request, response):
        # It's important to render the response first and add the header
        # second, as the render process will overwrite the headers.
        response = self._render_with_cat(request, response)
        return self._add_header(response)


    def process_template_response(self, request, response):
        self._inner_process(request, response)


    def process_response(self, request, response):
        self._inner_process(request, response)
