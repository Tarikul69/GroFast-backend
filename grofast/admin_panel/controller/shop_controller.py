from django.http import HttpResponseNotAllowed, JsonResponse
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from admin_panel.models import shop
from rest_framework.decorators import api_view

############################################### 
############# Register a New Shop #############
###############################################
@api_view(['POST'])
def shop_registration(request):
    if request.method == 'POST':
        # Extract data from request
        shop_id = request.data.get('shop_id')
        shop_name = request.data.get('shop_name')
        shop_address = request.data.get('shop_address')
        shop_phone_number = request.data.get('shop_phone_number')
        shop_type = request.data.get('shop_type')
        shop_status = request.data.get('shop_status')
        shop_condition = request.data.get('shop_condition')
        shop_rating = request.data.get('shop_rating', 0.00)
        is_verified = request.data.get('is_verified', False)
        created_at = request.data.get('created_at')

        # Check if all required fields are present
        if not shop_name or not shop_address or not shop_type:
            raise ValidationError("Shop name, address, and type are required.")

        # Create new shop instance
        shop_instance = shop(
            shop_id=shop_id,
            shop_name=shop_name,
            shop_address=shop_address,
            shop_phone_number=shop_phone_number,
            shop_type=shop_type,
            shop_status=shop_status,
            shop_condition=shop_condition,
            shop_rating=shop_rating,
            is_verified=is_verified,
            created_at=created_at
        )

        # Save the new shop to the database
        shop_instance.save()

        # Return a success response
        return Response({"message": "Shop registered successfully."}, status=200)


##################################################
################### Shop List ####################
##################################################
@api_view(['GET'])
def shop_list(request):
    # Get all shops from the database
    if request.method == 'GET':   
        shops = shop.objects.all()
        data = {
            "shops": [
                {
                    "shop_id": shop.shop_id,
                    "shop_name": shop.shop_name,
                    "shop_address": shop.shop_address,
                    "shop_phone_number": shop.shop_phone_number,
                    "shop_type": shop.shop_type,
                    "shop_status": shop.shop_status,
                    "shop_condition": shop.shop_condition,
                    "shop_rating": str(shop.shop_rating),
                    "is_verified": shop.is_verified,
                    "created_at": str(shop.created_at)
                } for shop in shops
            ]
        }
        return JsonResponse(data)
    return HttpResponseNotAllowed(['GET'])
         