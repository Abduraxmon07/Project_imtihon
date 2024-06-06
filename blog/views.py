from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import CustomerModelForm, ProductListModelForm
from django.db.models import Q

from blog.models import Product, Customer


# Create your views here.


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'blog/product-detail.html', context)


def customers(request):
    customers = Customer.objects.all()
    search = request.GET.get('search', '')
    if search:
        customer_all = customers.filter(Q(full_name__icontains=search) | Q(email__icontains=search))

    # paginator = Paginator(customer_all, 4)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    context = {
        'customers': customers,
        'search': search
    }

    return render(request, 'blog/customers.html', context)

def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)

    context = {
        'customer': customer,
    }

    return render(request, 'blog/customer-details.html', context)


def product_list(request):
    product = Product.objects.all()
    context = {
        'product': product,
    }

    return render(request, 'blog/product-list.html', context)

def add_customer(request):
    form = CustomerModelForm()

    if request.method == 'POST':
        form = CustomerModelForm(data=request.POST,)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'blog/add-customer.html', context)

def customer_edit(request, pk):
    customer = Customer.objects.get(id=pk)

    form = CustomerModelForm(instance=customer)

    if request.method == "POST":
        form = CustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customers")

    context = {
        'form': form,
    }
    return render(request, 'blog/add-customer.html', context)

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect("customers")
