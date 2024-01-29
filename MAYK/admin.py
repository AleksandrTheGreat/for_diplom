from django.contrib import admin
from .models import *

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('title','cena')

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('mail','workphone','mobilephone')