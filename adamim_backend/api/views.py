# api/views.py

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def google_one_tap_auth(request):
    id_token = request.data.get('id_token')

    try:
        # Verify id_token with Google
        CLIENT_ID = 'your_google_client_id'  # Replace with your Google Client ID
        idinfo = id_token.verify_oauth2_token(id_token, google_requests.Request(), CLIENT_ID)

        # Extract user information from idinfo
        google_sub = idinfo['sub']
        email = idinfo['email']

        # Check if user exists in database
        user, created = User.objects.get_or_create(google_sub=google_sub, defaults={'email': email})

        # Serialize user data
        serializer = UserSerializer(user)

        # Return serialized user data with JWT or session token
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
