from django.urls import path,include

from . import views

urlpatterns = [
    path('search/<str:query>/', views.ProductSearchView.as_view()),
]