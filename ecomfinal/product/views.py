from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer, CategoryListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import viewsets


from .models import Product, Category

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductView(APIView):
    def getProduct(self,category_slug,product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except:
            raise Http404


    def get(self,request,category_slug,product_slug):
        productObj = self.getProduct(category_slug,product_slug)
        serializer = ProductSerializer(productObj)
        return Response(serializer.data)


class CategoryView(APIView):
    def getCategory(self,category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except:
            print("no such categ")
            raise Http404


    def get(self,request,category_slug):
        categoryObj = self.getCategory(category_slug)
        serializer = CategorySerializer(categoryObj)
        return Response(serializer.data)


class CategoryListView(APIView):

    def get(self,request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

