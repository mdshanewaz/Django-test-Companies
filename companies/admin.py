from django.contrib import admin
from .models import *

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'job_title')
    search_fields = ('job_title',)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('type', 'company', 'model')

class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ('asset',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(DeviceLog, DeviceLogAdmin)