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
    if request.method == 'POST':
        category_name = request.data.get('category_name')
        shop_id = request.data.get('shop_id')
        shop_id = shop.objects.get(shop_id=shop_id)
        if not category_name or not shop_id:
            return Response({"message": "Category name and shop ID are required.", "status": "failed"}, status=400)
        category_instance = Category_table(
            category_name=category_name,
            shop_id=shop_id
        )
        category_instance.save()
        return Response({"message": "Category registered successfully."}, status=200)
    else:
      return Response({"message": "Method not allowed."}, status=405)
    
####################################################
############# Get Categories by Shop ID ############
####################################################
@api_view(['GET'])
def category_list_id(request, shop_id):
    if request.method == 'GET':

        categories = Category_table.objects.filter(shop_id=shop_id)
        if not categories.exists():
            return Response({"message": "No categories found for this shop.", "status": "failed"} )
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    else:
      return Response({"message": "Method not allowed."}, status=405)
####################################################
############# Get All By Categories ################
####################################################
@api_view(['DELETE'])
def category_delete(request, category_id):
    if request.method == 'DELETE':
        try:
            category = Category_table.objects.get(category_id=category_id)
            category.delete()
            return Response({"message": "Category deleted successfully."}, status=200)
        except Category_table.DoesNotExist:
            return Response({"message": "Category not found."}, status=404)
    else:
      return Response({"message": "Method not allowed."}, status=405)
#####################################################
############# Update Category #####################
#####################################################
@api_view(['PUT'])
def category_update(request, category_id):
    if request.method == 'PUT':
        try:
            category = Category_table.objects.get(category_id=category_id)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Category updated successfully."}, status=200)
            return Response(serializer.errors, status=400)
        except Category_table.DoesNotExist:
            return Response({"message": "Category not found."}, status=404)
    else:
      return Response({"message": "Method not allowed."}, status=405)