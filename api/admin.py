from django.contrib import admin

from api.models import Category, Journal


# Register your models here to view them in the admin panel.
admin.site.register(Category)
admin.site.register(Journal)
