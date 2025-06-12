from django.shortcuts import render


def download_app(request):
    return render(request, 'website/download_app.html')

def shop (request):
    return render(request, 'website/shop.html')

def offers (request):
    return render(request, 'website/offers.html')