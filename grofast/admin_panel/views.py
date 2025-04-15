from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from admin_panel.models import Users_table

##########################################################
################### users registration.###################
##########################################################

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        profile_picture = request.FILES.get('profile_picture')
        password = request.POST.get('password')
        is_verified = request.POST.get('is_verified', False)
        created_at = request.POST.get('created_at')
        
        hashed_password = csrf_exempt(password)
        users_instance = Users_table(
            username=username,
            email=email,
            phone_number=phone_number,
            address=address,
            profile_picture=profile_picture,
            password=hashed_password,
            is_verified=is_verified,
            created_at=created_at
        )
        users_instance.save()
        return JsonResponse({"message": "User registered successfully."})  
    return HttpResponseNotAllowed(['POST']) 