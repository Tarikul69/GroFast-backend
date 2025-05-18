from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .serializers import UsersTableSerializer
from .models import Users_table
from rest_framework.decorators import api_view
from .controller.shop_controller import shop_list, shop_registration
from .controller.adminUI_controller import admin_index
from .controller.category_controller import  category_registration
from .controller.login_registration_controller import login_api

##########################################################
################### users registration.###################
##########################################################

@api_view(['POST'])
def registration(request):

    if request.method == 'POST':
        # Extract data from request
        username = request.data.get('username')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        address = request.data.get('address')
        profile_picture = request.FILES.get('profile_picture')
        password = request.data.get('password')
        is_verified = request.data.get('is_verified', False)
        created_at = request.data.get('created_at')
        
        # Check if all required fields are present
        if not username or not email or not password:
            return Response({"message": "Username, email, and password are required.", "status":"failed"}, status=400)
        elif Users_table.objects.filter(username=username, email=email, phone_number=phone_number).exists():
            return Response({"message": "User with this information already exists.", "status":"failed"}, status=400)
        
        # Hash the password using Django's built-in method
        hashed_password = make_password(password)

        # Create new user instance
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
        
        # Save the new user to the database
        users_instance.save()

        # Return a success response
        return Response({"message": "User registered successfully."}, status=200)
     
##########################################################
################### Users Information ####################
##########################################################
@api_view(['GET'])
def users_list(request):
    if request.method == 'GET':
        users = Users_table.objects.all()
        serializer = UsersTableSerializer(users, many=True)
        return Response(serializer.data, status=200)
    return HttpResponseNotAllowed(['GET'])