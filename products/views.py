from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product,Category

# Create your views here.

def product_list(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query)
        )
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    if request.user.is_authenticated:
        from wishlist.models import Wishlist

        wishlist_product_ids = Wishlist.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)
    else:
        wishlist_product_ids = []

    return render(
        request,
        'products/home.html',
        {
            'products': products,
            'categories': categories,
            'query': query,
            'wishlist_product_ids': wishlist_product_ids,
        }
    )

def product_detail(request, id):
    product = get_object_or_404(Product,id=id)

    return render(
        request,
        'products/detail.html',
        {'product': product}
    )

def category_products(request,id):
    category= get_object_or_404(Category, id=id)
    products= Product.objects.filter(category=category)
    categories= Category.objects.all()

    return render(
        request, 
        'products/home.html',
        {
            'products': products,
            'categories': categories,
            'selected_category': category,

        }
    )