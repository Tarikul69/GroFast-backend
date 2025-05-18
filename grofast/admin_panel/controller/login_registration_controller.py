import hashlib
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from admin_panel.models import Users_table




@api_view(['POST'])
def login_api(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        print(password)
        if not email or not password:
            return Response({'message': 'Email and password are required.', 'status': 'failed'}, status=400)
            
        return Response({'message': 'Login successful', 'status': 'success'}, status=200)
    
    #result = authenticate(email=email, password=password)

 



@api_view(['POST'])
def registration_api(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({'message': 'Username, email, and password are required.', 'status': 'failed'}, status=400)


    return Response({'message': 'Registration successful', 'status': 'success'}, status=201)