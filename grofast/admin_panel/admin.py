from django.contrib import admin

from admin_panel.models import Review_table, Users_table, shop

# Register your models here.
admin.site.register([
    # Add your models here
    Users_table,
    shop,
    Review_table,
]) 