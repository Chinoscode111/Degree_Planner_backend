
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_view(request):
    if request.method == 'POST':

        roll_number = request.POST.get('roll_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        department = request.POST.get('department')
        degree = request.POST.get('degree')

        if User.objects.filter(rollnum=roll_number).exists():
            return JsonResponse({'status': 'error', 'message': 'User already exists'})

        if password != confirm_password:
            return JsonResponse({'status': 'error', 'message': 'Passwords do not match'})

        user = User(rollnum=roll_number, password=make_password(password))
        user.save()

        
        profile = UserProfile(user=user, department=department, degree=degree)
        profile.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'})
