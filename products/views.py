from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()
    return render(
        request, 
        'index.html', 
        context={'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products')
    else:
        form = ProductForm()
    return render(
        request, 
        'add_product.html', 
        context={'form': form})

def modify_product(request):
    products = Product.objects.all()
    selected_product = None
    form = None

    if request.method == "POST":
        product_name = request.POST.get('product_name')
        if 'save_changes' in request.POST:
            if product_name:
                selected_product = get_object_or_404(Product, name=product_name)
                form = ProductForm(request.POST, instance=selected_product)
                if form.is_valid():
                    form.save()
                    return redirect('products:index')  
        elif 'delete_item' in request.POST:
            if product_name:
                selected_product = get_object_or_404(Product, name=product_name)
                selected_product.delete()
                return redirect('products:index') 
        else:
            if product_name:
                selected_product = get_object_or_404(Product, name=product_name)
                form = ProductForm(instance=selected_product)
            else:
                form = ProductForm()
    else:
        form = ProductForm()

    return render(request, 'modify_product.html', {'products': products, 'form': form, 'selected_product': selected_product})