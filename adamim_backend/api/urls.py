from django.urls import path, re_path
from . import views

app_name = 'api'

urlpatterns = [
    path('google-one-tap-auth/', views.google_one_tap_auth, name='google_one_tap_auth'),
]