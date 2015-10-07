## Installation

`python setup.py install`

## Configuration

In your Django settings file:
* add `status_cats.middleware.StatusCatMiddleware` to `MIDDLEWARE_CLASSES`
* add `status_cats` to `INSTALLED_APPS` 
* make sure you have `django.template.loaders.eggs.Loader` in your `TEMPLATE_LOADERS`

## Development and testing

Want to make changes? Download the project and go to town.

If you'd like to run the test suite,
`python test_project/manage.py test test_project.tests`

If you'd like to run the test app to see your changes in the browser,
`python test_projectanage.py runserver`. URLs of the form `/status_code` provoke HTTP responses of the appropriate status code.