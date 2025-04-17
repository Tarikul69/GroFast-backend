from django.shortcuts import render


def landing_page(request):
    # Render the landing page template
    return render(request, 'website/index.html')