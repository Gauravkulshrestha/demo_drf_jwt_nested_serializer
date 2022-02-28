from django.contrib import admin
from .models import Mobile, Company

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['id','mobile_name','model_name','price','description','company_name']

@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ['id','name']