from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()

    context = {
        "title": "Магазин мебели HOME",
        "content": "Магазин мебели HOME",
        "categories": categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О магазине мебели HOME",
        "content": "Это интернет магазин мебели HOME. Здесь вы можете найти мебель для дома и офиса.",
        "text_on_page": "Магазин мебели HOME - лучший выбор для вашего дома и офиса.",
    }
    return render(request, "main/about.html", context)