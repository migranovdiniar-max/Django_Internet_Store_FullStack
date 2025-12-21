from django.http import Http404
from django.shortcuts import get_object_or_404, render

from goods.models import Categories, Products


def catalog(request, category_slug):
    if category_slug == 'all-goods':
        goods = Products.objects.all()
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        goods = Products.objects.filter(category=category)
        if not goods.exists():
            raise Http404()

    context = {
        "title": "Каталог товаров",
        "goods": goods
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug=False, product_id=False):
    if product_slug:
        product = Products.objects.get(slug=product_slug)
    elif product_id:
        product = Products.objects.get(id=product_id)
    else:
        return render(request, 'goods/product.html', context={"title": "Product not found", "product": None})

    context = {
        "title": product.name,
        "product": product
    }

    return render(request, 'goods/product.html', context)