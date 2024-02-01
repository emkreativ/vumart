from django.urls import path
from catalog import views


urlpatterns = [
   path('<int:id>/', views.category, name="category"),
   path('product/<int:id>/', views.product, name="product"),
   path('brand/<int:id>/', views.product, name="brand"),
   path('products/', views.products, name="products"),
]

