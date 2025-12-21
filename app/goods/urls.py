from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from goods import views

app_name = "goods"

urlpatterns = [
    path('search/', views.catalog, name="search"),
    path('<slug:category_slug>/', views.catalog, name="index"),
    path('product/<int:product_id>/', views.product, name="product"),
    path('product/<slug:product_slug>/', views.product, name="product"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=str(settings.BASE_DIR / 'static'))