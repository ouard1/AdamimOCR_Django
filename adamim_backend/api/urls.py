from django.urls import path, re_path
from . import views

app_name = 'api'

urlpatterns = [
    # Match the dynamic segment for backend using re_path
    re_path(r'^api/register-by-access-token/social/(?P<backend>[^/]+)/$', views.register_by_access_token),
    path('api/authentication-test/', views.authentication_test),
 
]