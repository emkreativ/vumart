from django.shortcuts import render

from catalog.models import Category, Product, NewProduct
from core.models import General, Social
from order.models import Order


def products(request):
    import json

    from django.http import HttpResponse

    response_data = {}
    response_data['name'] = 'Pivə məhsulu'
    response_data['slug'] = 'brandix-spark-plug-kit-asr-400'
    response_data['sku'] = '140-10440-B'
    response_data['price'] = 19
    response_data['images'] = [
            '/images/products/product-1-1.jpg',
            '/images/products/product-1-2.jpg',
        ]
    response_data['badges'] = ['sale', 'new', 'hot']
    response_data['rating'] = 4
    response_data['reviews'] = 3
    response_data['availability'] = 'in-stock'
    response_data['compatibility'] = [1, 2]
    d = {"Color": 'White',}
    response_data['attributes'] = d

    response_data2 = {}
    response_data2['name'] = 'Pivə məhsulu'
    response_data2['slug'] = 'brandix-spark-plug-kit-asr-400'
    response_data2['sku'] = '140-10440-B'
    response_data2['price'] = 19
    response_data2['images'] = [
        '/images/products/product-1-1.jpg',
        '/images/products/product-1-2.jpg',
    ]
    response_data2['badges'] = ['sale', 'new', 'hot']
    response_data2['rating'] = 4
    response_data2['reviews'] = 3
    response_data2['availability'] = 'in-stock'
    response_data2['compatibility'] = [1, 2]
    d = {"Color": 'White', }
    response_data2['attributes'] = d
    alll = {}
    alll['isLoading'] = False
    alll['data'] = [response_data,response_data2]


    return HttpResponse(json.dumps(alll), content_type="application/json")


def category(request, id):
    if request.user_agent.is_mobile == True:
        context = {

        }
        return render(request, "mobile/page/index.html", context)
    else:
        cart = None
        if request.user.is_authenticated:
            cart = Order.objects.filter(customer=request.user, is_ordered=False).last()
        cart_sum = 0
        if request.user.is_authenticated:
            order = Order.objects.filter(is_ordered=False, customer=request.user).last()
            if order:
                for o in order.items.all():
                    cart_sum = cart_sum + o.quantity * o.product.prices.last().price
        cats = Category.objects.filter(is_active=True)
        category = Category.objects.get(pk=id)
        general = General.objects.last()
        socials = Social.objects.all()
        context = {
            "socials": socials,
            "general": general,
            "cats": cats,
            "category": category,
            'cart': cart,
            'cart_sum': cart_sum,
        }
        return render(request, "desktop/catalog/category.html", context)

def product(request, id):
    if request.user_agent.is_mobile == True:
        context = {

        }
        return render(request, "mobile/page/index.html", context)
    else:
        cats = Category.objects.filter(is_active=True)
        product = Product.objects.get(pk=id)
        related_products = Product.objects.all()
        best_products = NewProduct.objects.all()

        cart = None
        if request.user.is_authenticated:
            cart = Order.objects.filter(customer=request.user, is_ordered=False).last()
        cart_sum = 0
        if request.user.is_authenticated:
            order = Order.objects.filter(is_ordered=False, customer=request.user).last()
            if order:
                for o in order.items.all():
                    cart_sum = cart_sum + o.quantity * o.product.prices.last().price
        general = General.objects.last()
        socials = Social.objects.all()
        context = {
            "cats": cats,
            "product": product,
            "best_products": best_products,
            "related_products": related_products,
            "socials": socials,
            "general": general,
            'cart': cart,
            'cart_sum': cart_sum,
        }
        return render(request, "desktop/catalog/product.html", context)