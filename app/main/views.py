from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        "title": "Home",
        "content": "Welcome to the homepage.",
        "list": ['first', "second"],
        "dict": {"first": "first", "second": "second"},
        "is_authenticated": False,
    }

    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")