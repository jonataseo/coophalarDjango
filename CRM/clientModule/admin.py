from django.contrib import admin

# Register your models here.
from .models import Client, Address

admin.site.register(Client)
admin.site.register(Address)
