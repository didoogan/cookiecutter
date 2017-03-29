from django.conf.urls import include, url

from checkings.views import CheckingsListView, CheckingsDetailView

urlpatterns = [
         url(r'^$', view=CheckingsListView.as_view(), name='list'),
         url(r'^(?P<pk>\d+)/$', view=CheckingsDetailView.as_view(), name='detail'),
    ]
