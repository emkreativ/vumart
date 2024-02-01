import imp
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from catalog.models import *
User = get_user_model()


class ProductListFeaturedSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    compareAtPrice = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    def get_slug(self, product, *args, **kwargs):
        return product.id
    def get_compareAtPrice(self, product, *args, **kwargs):
        return None

    def get_rating(self, product, *args, **kwargs):
        return 4

    def get_reviews(self, product, *args, **kwargs):
        return 3
    def get_compareAtPrice(self, product, *args, **kwargs):
        return None
    def get_images(self, product, *args, **kwargs):
        images = product.images.all()
        imgs = []
        for i in images:
            imgs.append("http://127.0.0.1:8000/media/"+ str(i.image))
        return imgs
    def get_price(self, product, *args, **kwargs):
        try:
            return product.prices.last().price
        except:
            return 0
    def get_main_image(self, product, *args, **kwargs):
        image = product.images.filter(is_main=True).last()
        if image:
            return str(image.image)
        else:
            return None


    class Meta:
        model = Product
        fields = ['id', 'slug','name','price','images','compareAtPrice','rating','reviews']


class ParentCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
class CategoryListSerializer(serializers.ModelSerializer):
    parent = ParentCategoryListSerializer()
    children = SubCategoryListSerializer(many=True)
    class Meta:
        model = Category
        fields = "__all__"




class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductListSerializer(serializers.ModelSerializer):

    def get_main_image(self, product, *args, **kwargs):
        image = product.images.filter(is_main=True).last()
        if image:
            return str(image.image)
        else:
            return None


    class Meta:
        model = Product
        fields = ['id', 'name',]





class CategoryRetrieveSerializer(serializers.ModelSerializer):
    parent = ParentCategoryListSerializer()
    children = SubCategoryListSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"