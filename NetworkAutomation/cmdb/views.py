from django.shortcuts import render

# Create your views here.
def device_list(request):
    devices = [
        {'ip':'192.168.1.1','name':'dev01'}
    ]

    return render(request, 'device_list.html', {'devices':devices})