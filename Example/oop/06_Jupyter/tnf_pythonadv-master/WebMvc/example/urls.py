from django.conf.urls import url
from django.urls import path

from . import view

app_name = 'example'
urlpatterns = [
    url(r'^$', view.index)
]
