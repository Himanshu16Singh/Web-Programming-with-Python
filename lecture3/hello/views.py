from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")    # HttpResponse special
# ... class created by django


def himanshu(request):
    return HttpResponse("Hello, Himanshu!")


def foo(request):
    return HttpResponse("This is a foo page!")


def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
