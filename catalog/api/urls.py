from django.urls import path
from catalog.api import views as api_views

app_name = 'catalog'

urlpatterns = [
    path('product/new/', api_views.ProductListNewAPIView.as_view(), name='products-new'),
    path('products/featured/', api_views.ProductListFeaturedAPIView.as_view(), name='products-featured'),
    path('category/list/', api_views.CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/', api_views.CategoryRetrieveAPIView.as_view(), name='category-retrieve'),
]
