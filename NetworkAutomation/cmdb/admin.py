from django.contrib import admin
from cmdb.models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'name', 'vendor', 'created_time']
    list_display_links = ['id', 'ip', 'name']
    search_fields = ['ip', 'name', 'vendor']
    list_per_page = 20
    exclude = ['sn']
    list_filter = ['vendor', 'group']

    date_hierarchy='created_time'

# Register your models here.
