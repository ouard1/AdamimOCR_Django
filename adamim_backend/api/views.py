
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests
import json
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer

User = get_user_model()
logger = logging.getLogger(__name__)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }

@api_view(['POST'])
@permission_classes([AllowAny])
def google_one_tap_auth(request):
    token_id = request.data.get('token_id')

    if not token_id:
        return Response({'error': 'Token ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
      
        CLIENT_ID = ' 146908205548-qsu2ppsmnju9cjsk1qgrngm3n09bhrd2.apps.googleusercontent.com'
        url = f"https://oauth2.googleapis.com/tokeninfo?id_token={token_id}"
        response = requests.get(url)
        data = response.json()
        
        google_sub = data.get('sub')
        email = data.get('email')

        if not google_sub or not email:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        username = email.split('@')[0]

        user, created = User.objects.get_or_create(google_sub=google_sub, defaults={'email': email, 'username': username})

        tokens = get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Google One Tap Auth Error: {e}")
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
