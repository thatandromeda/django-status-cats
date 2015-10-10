# django-status-cats

The [HTTP Status Cats](https://www.flickr.com/photos/girliemac/albums/72157628409467125/with/6540643319/) are obviously among the best photo sets of all time. Don't you want to be able to return them as part of your Django app's HttpResponses?

_Now you can_.  Install this middleware and your Django project will be 100% more catful!

All `HttpResponse`s will get an added `X-Status-Cat` header linking to the appropriate cat photo. You may also render some or all of your `HttpResponse`s with status-code-appropriate cat pics. A simple configuration option lets you specify which status codes get which treatment.

The default settings will break your project (_but with cats!_), so you probably want change them (see below).

## Installation

`python setup.py install`

## Configuration

In your Django settings file:
* add `status_cats.middleware.StatusCatMiddleware` to `MIDDLEWARE_CLASSES`
* add `status_cats` to `INSTALLED_APPS` 
* make sure you have `django.template.loaders.eggs.Loader` in your `TEMPLATE_LOADERS`

Optionally, you may configure the following variables:

`STATUS_CATS_CAT_TEMPLATE`: The template to use when rendering a page with a status cat picture. This template will be rendered with the following context:
```
    {'cat_url': cat_url,
    # 'base.html' by default; else STATUS_CATS_BASE_TEMPLATE
    'base_template': BASE_TEMPLATE, 
    'status_code': status_code}
```

_Default value_: `status_cats/default.html` (provided by django-status-cats).

`STATUS_CATS_BASE_TEMPLATE`: The template (in your project) extended by `STATUS_CATS_CAT_TEMPLATE`.

_Default value_: `base.html`.

`STATUS_CATS_HEADER_ONLY` (list of integers): The HTTP status codes for which responses should have a cat-themed header added, but should _not_ be rendered with a cat-themed template.

_Default value_: `[200]`

That is, any of your pages which respond with `200 OK` will be rendered in the normal manner, but all other responses will be presented to the user as cat web pages.

`STATUS_CATS_HEADER_ONLY_ALL` (Boolean): If True, only apply HTTP `X-Status-Cat` headers to all responses; never render cat templates. If False, observe behavior of `STATUS_CATS_HEADER_OVERRIDE_ONLY` if specified, else defaults.

_Default value_: `False`

## Development and testing

Want to make changes? Download the project and go to town.

If you'd like to run the test suite,
`python test_project/manage.py test test_project.tests`

If you'd like to run the test app to see your changes in the browser,
`python test_projectanage.py runserver`. URLs of the form `/[status_code]` provoke HTTP responses of the appropriate status code.

## Dependencies
Just Django.

This has been tested on Django 1.8.5, but probably works at least as far back as Django 1.4. (Though if you're running anything < 1.7, if possible please  update to a supported version!)