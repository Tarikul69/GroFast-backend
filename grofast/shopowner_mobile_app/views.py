from django.http import JsonResponse
from django.shortcuts import render
from .controller.category_controller import  category_list

# Create your views here.
def api(request):
    if request.method == 'GET':
      data = {
          "name": "John Doe",
          "age": 30,
          "city": "New York"
      }
    return JsonResponse(data) 
