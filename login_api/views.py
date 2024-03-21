from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        roll_number = "rudra"
        password = "abc"
        user = authenticate(request, username=roll_number, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'})
