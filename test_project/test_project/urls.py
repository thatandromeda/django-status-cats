from django.conf.urls import patterns, url

from test_project.views import StatusCodeView, ExceptionView

urlpatterns = patterns('',
    url(r'^(?P<status_code>\d+)',
        StatusCodeView.as_view(),
        name='status_code_response'),
    url(r'^exception/',
        ExceptionView.as_view(),
        name='exception_response'),
)
