from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseNotAllowed
from admin_panel.models import Category_table, shop
from ..serializers import CategorySerializer

###################################################
############# Add a New Category ##################
###################################################
@api_view(['POST'])
def category_list(request):
    # Function to add a new category
    if request.method == 'POST':
        category_name = request.data.get('category_name')
        shop_id = request.data.get('shop_id')
        print("Category Name:", category_name)
        print("Shop ID:", shop_id)
        if not category_name or not shop_id:
            return Response({"message": "Category name and shop ID are required.", "status": "failed"}, status=400)       
        try:
            shop_instance = shop.objects.get(shop_id=shop_id)
        except shop.DoesNotExist:
            return Response({"message": "Shop does not exist.", "status": "failed"}, status=404)
        
        category_instance = Category_table(
            category_name=category_name,
            shop_id=shop_instance
        )
         
        category_instance.save() 
        return Response({"message": "Category added successfully."}, status=200)
    else:
      return Response({"message": "Method not allowed."}, status=405)
    

@api_view(['GET'])
def category_list_id(request, shop_id):
    if request.method == 'GET':
        categories = Category_table.objects.filter(shop_id=shop_id)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    else:
      return Response({"message": "Method not allowed."}, status=405)