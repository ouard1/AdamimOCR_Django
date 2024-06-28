from django.urls import path, re_path
from . import views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
app_name = 'api'


urlpatterns = [
    path('api/auth/google/', views.google_one_tap_auth, name='google_one_tap_auth'),
    path('api/auth/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', views.register, name='register'),
]
