from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests


'''# Google Auth Handling :
def google_login(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        expiration_time = request.POST.get('expiration_time')

        if token and expiration_time:
            # Store the token and expiration time securely
            request.session['token'] = token
            request.session['expiration_time'] = expiration_time
            return JsonResponse({'success': True})
        else:
            # Handle invalid or missing token
            return JsonResponse({'error': 'Invalid token'}, status=400)
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Method not allowed'}, status=405)
'''
from django.contrib.auth import authenticate
from django.http import JsonResponse
from google.oauth2 import id_token
from google.auth.transport import requests

def google_login(request):
    if request.method == 'POST':
        id_token = request.POST.get('id_token')
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(id_token, requests.Request())
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            # ID token is valid. Get the user's Google Account info from the decoded token.
            user_email = idinfo['email']
            user = authenticate(request, username=user_email, password=None)
            if user is not None:
                return JsonResponse({'user': {'email': user.email}})
            else:
                # Handle new user registration or other logic
                return JsonResponse({'user': {'email': user_email}})
        except ValueError as e:
            # Invalid token
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


# HuggingFace API access handling :

'''def huggingface_space(request):
    # Check if the user is authenticated in your Django app
    if request.user.is_authenticated:
        # Make a request to Hugging Face API to fetch content from the private space
        url = 'https://huggingface.co/spaces/RamyBTG/AdamimOCR'
        headers = {
            'Authorization': 'Bearer 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'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # If the request is successful, render the content in your template
            context = {'content': response.text}
            return render(request, 'huggingface_space.html', context)
        else:
            # Handle errors appropriately
            return render(request, 'error.html', {'message': 'Error accessing Hugging Face Space'})
    else:
        # Redirect unauthenticated users to the login page
        return redirect('login')'''