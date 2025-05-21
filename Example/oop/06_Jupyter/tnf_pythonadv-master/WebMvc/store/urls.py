from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='list'),
    path('add', views.insertComposer, name='add'),
    path('details/<int:id>/', views.composerDetails, name='details'),
    path('details2', views.composerDetails2, name='details2'),
]