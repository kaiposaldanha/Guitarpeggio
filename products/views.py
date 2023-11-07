from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from .models import ItemCarrinho
from django.http import HttpResponseRedirect
from .models import Carrinho, ItemCarrinho
# Create your views here.

def index(request):
    return render(request,"products/index.html", {
        "products": Product.objects.all()
    })
    
def instruments(request):
    return render(request,"products/instruments.html", {
        "products": Product.objects.all()
    })
    
def whoweare(request):
    return render(request, "products/whoweare.html",{
        "products": Product.objects.all()
    })
    
def guitarists(request):
    return render(request, "products/guitarists.html",{
        "products": Product.objects.all()
    })
    
def about(request):
    return render(request,"products/about.html",{
        "products": Product.objects.all()
    })
    
def cart(request):
    items_in_cart = ItemCarrinho.objects.all()
    return render(request, "products/cart.html", {
        "products": Product.objects.all(),
        "cart": items_in_cart
    })    
        

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    item, created = ItemCarrinho.objects.get_or_create(product=product, defaults={'quantity': 1})

    if not created:
        item.quantity += 1
        item.save()

    return HttpResponseRedirect('/products/instruments')

    
def remove_from_cart(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    item.delete()
    return HttpResponseRedirect('/products/cart/')