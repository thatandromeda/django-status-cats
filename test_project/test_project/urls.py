from django.conf.urls import patterns, url

from test_project.views import StatusCodeView

urlpatterns = patterns('',
    url(r'^(?P<status_code>\d+)',
    	StatusCodeView.as_view(),
    	name='status_code_response'),
)
