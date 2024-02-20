from django.http import JsonResponse

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
