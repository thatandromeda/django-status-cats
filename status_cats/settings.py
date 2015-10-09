"""
Settings for the status_cats project.

These can be overridden in the user settings file:

STATUS_CATS = {
	'CAT_TEMPLATE': /path/to/user's/cat/template,
    'BASE_TEMPLATE': /path/to/user's/base/template
}
"""

from django.conf import settings

# HttpResponses whose status codes are in this list will have status cat headers
# added but will not be rendered with cat templates.
HEADER_ONLY_DEFAULT = [200]

CAT_TEMPLATE = getattr(
    settings,
    "STATUS_CATS_CAT_TEMPLATE",
    "status_cats/default.html"
)

BASE_TEMPLATE = getattr(
    settings,
    "STATUS_CATS_BASE_TEMPLATE",
    "base.html"
)

HEADER_OVERRIDE_ONLY = getattr(
    settings,
    "STATUS_CATS_HEADER_ONLY",
    HEADER_ONLY_DEFAULT
)

HEADER_OVERRIDE_ALL = getattr(
    settings,
    "STATUS_CATS_HEADER_ONLY_ALL",
    False
)
