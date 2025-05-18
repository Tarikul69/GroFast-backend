import hashlib
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from admin_panel.models import Users_table
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


#############################################################
####################### Login API ###########################
#############################################################
@api_view(['POST'])
def login_api(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'status': 'failed', 'message': 'Email and password are required.'}, status=400)

    try:
        # Get user by email
        user = Users_table.objects.get(email=email)
        print(user.password)
        print(user.email)
    except Users_table.DoesNotExist:
        return Response({'status': 'failed', 'message': 'User not found.'}, status=404)

    # Use authenticate to check password
    user = authenticate(username=user.email, password=password)

    if user is not None:
        # Create or retrieve token
        #token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'status': 'success',
            'message': 'Login successful',
            #'token': token.key,
            'user': {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        }, status=200)
    else:
        return Response({'status': 'failed', 'message': 'Invalid password.'}, status=401)

##############################################################
#################### Registration API ########################
##############################################################
@api_view(['POST'])
def registration_api(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({'message': 'Username, email, and password are required.', 'status': 'failed'}, status=400)


    return Response({'message': 'Registration successful', 'status': 'success'}, status=201)


############################################################
############### Logout API #################################
############################################################
@api_view(['POST'])
def log_out(request):
    if request.method == 'POST':
        request.session.flush()
        request.users_table.auth_token.delete()
        return Response({'message': 'Logout successful', 'status': 'success'}, status=200)
    else:
        return Response({'message': 'Method not allowed', 'status': 'failed'}, status=405)