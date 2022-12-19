from django.contrib import admin
from cmdb.models import Device, Interface

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'name', 'vendor', 'platform', 'created_time']
    list_display_links = ['id', 'ip', 'name']
    search_fields = ['ip', 'name', 'platform']
    list_per_page = 20
    exclude = ['sn']
    list_filter = ['vendor', 'platform']

    date_hierarchy='created_time'

@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'device']
    list_display_links = ['name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['device'] 
    ordering = ('device','name')
# Register your models here.
