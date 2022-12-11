from django.urls import path
from cmdb.views import device_list

urlpatterns = [
    path('device_list/', device_list, name='device_list')
]