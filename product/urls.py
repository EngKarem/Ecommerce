
from .views import LatestProductList, ProductDetail

from django.urls import path, include


urlpatterns = [
    path('latest-product/', LatestProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
]
