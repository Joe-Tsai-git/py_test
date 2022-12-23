from django.contrib import admin
from cmdb.models import Device, Interface
from django.contrib import messages

def collect_intfs_act(modeladmin, request, queryset):
    from scripts.intf_collection_with_nornir import collect_intfs
    collect_intfs(queryset=queryset)
    messages.add_message(request, messages.INFO, "采集成功！")
    print("端口更新完成")

collect_intfs_act.short_description = "采集端口信息"
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'name', 'vendor', 'platform', 'created_time']
    list_display_links = ['id', 'ip', 'name']
    search_fields = ['ip', 'name', 'platform']
    list_per_page = 20
    exclude = ['sn']
    list_filter = ['vendor', 'platform']

    date_hierarchy='created_time'
    actions = [collect_intfs_act]

@admin.register(Interface)
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'device']
    list_display_links = ['name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['device'] 
    ordering = ('device','name')
# Register your models here.
