from goods.models import Categories


def categories(request):
    return {'categories': Categories.objects.all()}