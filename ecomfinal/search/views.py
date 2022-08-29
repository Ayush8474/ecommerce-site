from django.shortcuts import render
from rest_framework.views import APIView
from elasticsearch_dsl import Q
from product.document import ProductDocument
from product.serializers import ProductSerializer
from rest_framework.response import Response


class ProductSearchView(APIView):
    def get(self,request,query):
        q = Q(
            'multi_match',
            query=query,
            fields=[
                'name',
                'description',
                'category',
            ],
            fuzziness='auto')
        search = ProductDocument.search().query(q)
        response = search.execute()

        # print all the hits
        qs = search.to_queryset()
        serializer = ProductSerializer(qs, many=True)

        return Response(serializer.data)
