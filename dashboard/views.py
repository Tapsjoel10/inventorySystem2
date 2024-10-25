from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    itemsCount = Product.objects.all().count()
    ordersCount = Order.objects.all().count()
    workersCount = User.objects.all().count()
    context = {
        'orders': orders,
        'products': products,
        'workersCount':workersCount,
        'itemsCount':itemsCount,
        'ordersCount':ordersCount,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    workersCount = workers.count()
    itemsCount = Product.objects.all().count()
    ordersCount = Order.objects.all().count()
    context = {
        'workers':workers,
        'workersCount':workersCount,
        'itemsCount':itemsCount,
        'ordersCount':ordersCount,
   }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staffDetail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staffDetail.html', context)

@login_required
def product(request):
    items = Product.objects.all()
    itemsCount = items.count()
    workersCount = User.objects.all().count()
    ordersCount = Order.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            productName = form.cleaned_data.get('name')
            messages.success(request, f'{productName} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context = {
        'items':items,
        'form':form,
        'itemsCount':itemsCount,
        'workersCount':workersCount,
        'ordersCount':ordersCount,
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def productDelete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/productDelete.html')

@login_required
def productUpdate(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/productUpdate.html', context)

@login_required
def order(request):
    orders = Order.objects.all()
    ordersCount = orders.count()
    workersCount = User.objects.all().count()
    itemsCount = Product.objects.all().count()
    context = {
        'orders':orders,
        'ordersCount':ordersCount,
        'workersCount':workersCount,
        'itemsCount':itemsCount,
    }
    return render(request, 'dashboard/order.html', context)