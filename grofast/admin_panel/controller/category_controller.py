from rest_framework.response import Response
from rest_framework.decorators import api_view
from admin_panel.models import Category_table, shop


@api_view(['POST'])
def category_registration(request):
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