from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.conf.urls.static import static
from django.conf import settings

from core import views as core_views
from contact import views as contact_views
from account import views as account_views
from blog import views as blog_views
from catalog import views as catalog_views
from order import views as order_views


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Vumart API",
      default_version='v1',
      description="Vumart swagger",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name="index"),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/account/', include('account.api.urls', namespace='account-api')),
    path('api/catalog/', include('catalog.api.urls', namespace='catalog-api')),

    path('contact/', core_views.index, name="contact"),
    path('terms/', core_views.index, name="terms"),
    path('career/', core_views.index, name="career"),
    path('subscribe/', core_views.subscribe, name="subscribe"),
    path('kampaniyalar/', core_views.index, name="kampaniyalar"),
    path('endirimler/', core_views.index, name="endirimler"),
    path('yenimehsullar/', core_views.index, name="yenimehsullar"),
    path('brands/', core_views.index, name="brands"),
    path('about/', core_views.index, name="about"),
    path('blogs/', core_views.index, name="blogs"),
    path('offers/', core_views.index, name="offers"),
    path('track/', core_views.index, name="track"),
    path('search/', core_views.index, name="search"),

    path('signup/', core_views.index, name="signup"),
    path('user/dashboard/', core_views.index, name="user-dashboard"),
    path('user/wishlist/', core_views.index, name="wishlist"),
    path('user/history/', core_views.index, name="user-history"),
    path('user/logout/', core_views.index, name="logout"),

    path('category/<int:id>/', catalog_views.category, name="category"),
    path('product/<int:id>/', catalog_views.product, name="product"),
    path('blog/<int:id>/', core_views.index, name="blog"),
    path('profile/address-add/', core_views.index, name="address-add"),
    path('profile/address-edit/<int:id>/', core_views.index, name="address-edit"),

    path('order/', include('order.urls')),
    path('account/', include('account.urls')),
    path('catalog/', include('catalog.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
