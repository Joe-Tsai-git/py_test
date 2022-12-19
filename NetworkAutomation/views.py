from django.shortcuts import render
from cmdb.models import Device

# Create your views here.
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'device_list.html', {'devices':devices})