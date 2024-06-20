from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from social_django.utils import psa

from requests.exceptions import HTTPError
from social_core.exceptions import AuthForbidden
from django.views.decorators.csrf import csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
@psa()
def register_by_access_token(request, backend):

    token = request.data.get('access_token')
    print(token)
    try:
        user = request.backend.do_auth(token)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

    except AuthForbidden as e:
        return Response({'error': 'Authentication with Google failed: {}'.format(e)}, status=status.HTTP_403_FORBIDDEN)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def authentication_test(request):
    print(request.user)
    return Response(
        {
            'message': "User successfully authenticated"
        },
        status=status.HTTP_200_OK,
    )

