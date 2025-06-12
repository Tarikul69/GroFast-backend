from django.shortcuts import render


def download_app(request):
    return render(request, 'website/download_app.html')