import string
import random
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework import permissions, serializers,status, viewsets, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from catalog.api.serializers import *
from catalog.models import Product
User = get_user_model()

class ProductListFeaturedAPIView(generics.ListAPIView):
    serializer_class = ProductListFeaturedSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny,]

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        try:
            response.data = {
                "status": 200,
                "message": "Featured products list",
                "isLoading": False,
                "data": response.data
            }
        except:
            response.data = {
                "status": 500,
                "message": "Featured products list",
                "success": False,
                "data": None
            }
        return response

class ProductListNewAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny,]

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        try:
            response.data = {
                "status": 200,
                "message": "Featured products list",
                "success": True,
                "data": response.data
            }
        except:
            response.data = {
                "status": 500,
                "message": "Featured products list",
                "success": False,
                "data": None
            }
        return response

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny,]

    def get_queryset(self):
        queryset = Category.objects.filter(is_active=True, parent=None)
        return queryset



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 18
    page_size_query_param = 'page_size'
    max_page_size = 30





class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CategoryRetrieveSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny,]
    queryset = Category.objects.all()




