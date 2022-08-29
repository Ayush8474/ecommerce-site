from django.urls import path,include

from product import views

urlpatterns = [
    path('latest/', views.LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductView.as_view()),
    path('products/<slug:category_slug>/', views.CategoryView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    path('products/', views.ProductViewSet.as_view({'get': 'list'})),
]