from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart

# Create your views here.

@login_required
def add_to_cart(request, id):
    product=get_object_or_404(Product, id=id)

    cart_item, created= Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if created:
        if product.stock < 1:
            cart_item.delete()
        else:
            cart_item.quantity = 1
            cart_item.save()
        
    else:
        if cart_item.quantity<product.stock:
            cart_item.quantity +=1
            cart_item.save()

    return redirect('cart')

@login_required
def cart_view(request):
    items = Cart.objects.filter(user=request.user)

    total=sum(
        item.subtotal()
        for item in items
    ) 
    return render(request,'cart/cart.html',
                  {
                     'items': items,
                     'total': total 
                  }
                  
    )            

@login_required
def increase_quantity(request, id):
    item=get_object_or_404(Cart,id=id,user=request.user)
    if item.quantity< item.product.stock:
        item.quantity += 1
        item.save()
    return redirect('cart')

@login_required
def decrease_quantity(request, id):
    item = get_object_or_404(Cart,id=id,user=request.user)
    if item.quantity>1:
        item.quantity -=1
        item.save()
    else:
        item.delete()
    return redirect('cart')

@login_required
def remove_cart(request,id):
    item=get_object_or_404(Cart,id=id,user=request.user)
    item.delete()
    return redirect('cart')