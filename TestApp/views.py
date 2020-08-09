import datetime

from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    date = datetime.datetime.now()
    return render(request, "TestApp/index.html", {
        "newmonth": date.month == date.day
    })


def hello(request, name):
    return HttpResponse(f'<b>Hello, {name.capitalize()}')
