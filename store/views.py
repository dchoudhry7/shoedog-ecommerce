from .models import Cart, CartItem, Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': True})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': True, 'username': username})
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'signup.html')

def add_to_cart(request, product_id):
    if(not request.user.is_authenticated):
        return redirect('login')
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = 0
    for item in cart_items:
        item.subtotal = item.product.price * item.quantity
        total += item.subtotal
    return render(request, 'cart.html', {
        'items': cart_items,
        'total': total
    })

def increase_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def decrease_quantity(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('view_cart')

def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity
    #payment gateway
    #just clear the cart and show a success message
    cart_items.delete()
    return render(request, 'checkout.html', {'total': total})