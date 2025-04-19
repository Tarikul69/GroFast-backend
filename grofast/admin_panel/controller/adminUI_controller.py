

from urllib import request
from django.shortcuts import render


def admin_index(request):
    """
    This function serves as the entry point for the admin panel. It renders the admin index page.
    """
    return render(request, 'admin_panel/admin_index.html')