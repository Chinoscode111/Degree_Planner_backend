
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from .models import User


@csrf_exempt
def register_view(request):
    if request.method == 'POST':

        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')
        # Rest of the code...

        profile = User(user=user, department=department, degree=degree)
        profile.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'})
