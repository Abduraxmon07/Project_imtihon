from django.contrib import admin
from django.urls import path

from blog.views import index, product_detail, customers, product_list, customer_detail, add_customer, customer_edit, delete_customer

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('customers/', customers, name='customers'),
    path('list/', product_list, name='product_list'),
    path('customer_detail/<int:pk>', customer_detail, name='customer_detail'),
    path('add-customer/', add_customer, name='add_customer'),
    path('edit_customer/<int:pk>/', customer_edit, name="customer_edit"),
    path('delete_customer/<int:pk>/', delete_customer, name="customer_delete")
]
