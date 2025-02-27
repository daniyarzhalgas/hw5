from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
