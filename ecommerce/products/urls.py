from django.urls import path
from . import views
from django.urls import path
from .views import product_list, ProductDetailView

urlpatterns = [
    path("", product_list, name="product_list"),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]