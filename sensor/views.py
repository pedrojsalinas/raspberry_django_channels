from django.shortcuts import render

def sensor(request):

    return render(request, "sensor.html", {
        'sensor': '99',
    })