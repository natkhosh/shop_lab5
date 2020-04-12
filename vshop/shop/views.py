from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .settings.base import *
from django.core.paginator import Paginator

from django.http import HttpResponse
import json


class IndexView(View):

    def get(self, request):
    
        for k, v in request.COOKIES.items():
            print(k, v)
    
        return render(request, 'shop/index.html', {'phone_number': PHONE_NUMBER})


class ShopView(View):

    def get(self, request, page_id=1):    
    
        products_list = [{'name':       'Bell Pepper',
                     'image':      'shop/images/product-1.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'}, 
                    {'name':       'Strawberry',
                     'image':      'shop/images/product-2.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Green Beans',
                     'image':      'shop/images/product-3.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Purple Cabbage',
                     'image':      'shop/images/product-4.jpg',
                     'price':      '$120.00'},
                    {'name':       'Tomatoe',
                     'image':      'shop/images/product-5.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'},   
                    {'name':       'Brocolli',
                     'image':      'shop/images/product-6.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Carrots',
                     'image':      'shop/images/product-7.jpg',
                     'price':      '$120.00'}, 
                    {'name':       'Fruit Juice',
                     'image':      'shop/images/product-8.jpg',
                     'price':      '$120.00'},     
                    {'name':       'Onion',
                     'image':      'shop/images/product-9.jpg',
                     'price':      '$120.00',
                     'discount':   '30%',
                     'price_sale': '$80.00'},    
                    {'name':       'Apple',
                     'image':      'shop/images/product-10.jpg',
                     'price':      '$120.00'},   
                    {'name':       'Garlic',
                     'image':      'shop/images/product-11.jpg',
                     'price':      '$120.00'},     
                    {'name':       'Chilli',
                     'image':      'shop/images/product-12.jpg',
                     'price':      '$120.00'}]
                   
        paginator = Paginator(products_list, 12)
        
        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('shop'))
            
        return render(request, 'shop/shop.html', {'products': products, 'phone_number': PHONE_NUMBER})


class WishlistView(View):
   
    def get(self, request):
        food = [
            {'title': 'Bell Pepper',
             'img': 'images/product-1.jpg',
             'description': 'Far far away, behind the word mountains, far from the countries',
             'currency': '$',
             'price': 80.00,
             'quantity': 1,
             'total_price': 80.00
             },
            {'title': 'Stawberry',
             'img': 'images/product-2.jpg',
             'description': 'Far far away, behind the word mountains, far from the countries',
             'currency': '$',
             'price': 120.00,
             'quantity': 1,
             'total_price': 120.00
             },
            {'title': 'Green beans',
             'img': 'images/product-3.jpg',
             'description': 'Far far away, behind the word mountains, far from the countries',
             'currency': '$',
             'price': 20.00,
             'quantity': 1,
             'total_price': 20.00
             },
        ]

        if not request.is_ajax():
            return render(request, 'shop/wishlist.html', {'phone_number': PHONE_NUMBER})
        else:
            print('##########')
            return HttpResponse(json.dumps({'food': food}), content_type='application/json')
        
    # def post(self, request):
    #     global wishlist_count
    #     if request.is_ajax():
    #         message = f'WishlistView: {wishlist_count}'
    #         wishlist_count += 1
    #         print(message)
    #     else:
    #         message = 'Not AJAX request'
    #
    #     return HttpResponse(message)
    #
        
        
        
        
        
        
        
        
        
        
        
        
        
        