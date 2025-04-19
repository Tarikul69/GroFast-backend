from django.http import HttpResponseNotAllowed, JsonResponse
from grofast.admin_panel.models import shop
from rest_framework.decorators import api_view

##################################################
###### Shop List Api for Users Mobile App  #######
##################################################

@api_view(['GET'])
def shop_list_user(request):
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
                    #"shop_condition": shop.shop_condition,
                    #"shop_rating": str(shop.shop_rating),
                    "is_verified": shop.is_verified,
                    "created_at": str(shop.created_at)
                } for shop in shops
            ]
        }
        return JsonResponse(data)
    return HttpResponseNotAllowed(['GET'])