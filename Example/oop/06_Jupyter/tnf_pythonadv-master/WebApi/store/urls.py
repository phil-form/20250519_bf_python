from django.urls import path
from . import views

urlpatterns = [
    path('', views.ComposerViewSet.as_view(), name='get_post_composers'),
    path('add/', views.ComposerCreate.as_view(), name='post_composers'),
    path('<int:pk>', views.ComposerUpRetDel.as_view(), name='get_put_delete_composer')
]
