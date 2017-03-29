from django.conf.urls import include, url

from checkings.views import CheckingsList

urlpatterns = [
         url(r'^$', view=CheckingsList.as_view(), name='list'),
    ]
