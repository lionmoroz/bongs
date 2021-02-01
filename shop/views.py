
import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .filters import ProductFilter
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'home.html'
    extra_context={
        "instagram_profile_name": "3d_print.ua"
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoriy'] = Category.objects.filter(is_active=True)
        context['top_product'] = random.sample(list(Product.objects.filter(available=True)), 4)
        return context

    
# Create your views here.
# def product_list_2(request):
#     products = Product.objects.filter(available=True)
#     myFilter = ProductFilter(request.GET,
#                              queryset = products
#                             )
#     products = myFilter.qs
#     context ={
#         'products': products,
#         'myFilter': myFilter
#     }
#     return render(request, 'shop/product/list2.html', context)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(available=True)
        
    myFilter = ProductFilter(request.GET,
                             queryset = products
                            )
    products = myFilter.qs


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render (request, 'shop/product/list.html', { 'category': category,
                                                        'categories': categories,
                                                        'products': products,
                                                        'myFilter': myFilter, })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, 
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    
    similar_product = Product.objects.filter(category = product.category).exclude(pk=product.pk)
    similar_products = random.sample(list(similar_product), 1) 
        
    
    
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        "similar_products": similar_products,
                                                        "instagram_profile_name": "3d_print.ua"})


