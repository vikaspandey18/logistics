from django.contrib import admin
from contacts.models import *
# Register your models here.

@admin.register(ContactDetail)

class ContactDetailAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','updated','created')
    ordering = ['-created']
    list_filter = ['created','updated']



@admin.register(Getquotes)

class GetquotesAdmin(admin.ModelAdmin):
    list_display = ('city_depature','city_deliver','weight','dimensions','updated','created')
    ordering = ['-created']
    list_filter = ['city_depature','created']