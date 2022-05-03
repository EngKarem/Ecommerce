
from product import views
from django.urls import path, include


urlpatterns = [
    path('products/search/', views.search),
    path('latest-product/', views.LatestProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]
