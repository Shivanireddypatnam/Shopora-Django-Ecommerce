from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from .models import Order,OrderItem

# Create your views here.

@login_required
def checkout(request):
    cart_items=Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect('cart')

    total = sum(
       item.product.price * item.quantity
       for item in cart_items 
    )

    if request.method == 'POST':
        full_name=request.POST.get('full_name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')

        order=Order.objects.create(
            user=request.user,
            total_price=total,
            full_name=full_name,
            phone=phone,
            address=address,
            city=city,
            state=state,
            pincode=pincode
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

            item.product.stock-=item.quantity
            item.product.save()

        cart_items.delete()

        return redirect('orders')

    return render(
        request,
        'orders/checkout.html',
        {'total':total}
    )

@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'orders/orders.html',
        {'orders': orders}
    )


@login_required
def order_detail(request, id):
    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )

    return render(
        request,
        'orders/order_detail.html',
        {'order': order}
    )



@login_required
def cancel_order(request, id):
    if request.method == 'POST':
        order = get_object_or_404(
            Order,
            id=id,
            user=request.user
        )

        if order.status == 'ordered':
            for item in order.items.all():
                item.product.stock += item.quantity
                item.product.save()

            order.status = 'cancelled'
            order.save()

    return redirect('orders')
