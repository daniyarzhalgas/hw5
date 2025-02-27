from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Must call .all() to get a queryset
    return render(request, "products/product_list.html", {"products": products})


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'  # Your existing template
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'  # Create this template
    context_object_name = 'product'
