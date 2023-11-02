from django.shortcuts import render, HttpResponse, redirect
from store.models import Product, Category, Order
from django.contrib import messages

# importing usercreationform and authenticationform
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# importing authenticate, login and logout
from django.contrib.auth import authenticate, login as loginUser, logout

# importing login_required
from django.contrib.auth.decorators import login_required

# Create your views here.

# function for homepage
def home(request):
#    get method for categories and products
   if request.method == "GET":
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.objects.all()
        categoryID = request.GET.get("category")
        if categoryID:
            def get_all_products_by_categoryid(category_id):
                if category_id:
                    return Product.objects.filter(category=category_id)
                else:
                    return Product.objects.all()

            products = get_all_products_by_categoryid(categoryID)
        else:
            products = Product.objects.all()

        context = {
        'products': products,
        'categories': categories
        }
        return render(request, "home.html", context)
   
#    post method for cart
   elif request.method == "POST":
        product = request.POST.get("product")
        remove = request.POST.get('remove')
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session["cart"] = cart
        return redirect("/home")
   

# function for cart
@login_required(login_url='login')
def cart(request):
    if request.method == "GET":
        ids = list(request.session.get("cart").keys())
        products = Product.get_products_by_id(ids)
        context = {
            'products': products
        }

        return render(request, "cart.html", context)


# function for checkout
def checkOut(request):
    if request.method == "POST":
        customer = request.POST.get('customer')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        # print(address, phone, customer, cart, products)

        for product in products:
            # print(cart.get(str(product.id)))
            order = Order(customer = customer, product = product, price = product.price, address = address, phone = phone,quantity = cart.get(str(product.id)))
            # print(order)
            order.save()

        request.session['cart'] = {}
        messages.success(request, 'Your order has been placed successfully! The delivery time is one week.')
        return redirect('cart')


# function for sign up into Application
def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "signup.html", context)
    else:
        form = UserCreationForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect("/login")
        else:
            return render(request, "signup.html", context)
        

# function for login into Application
def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "login.html", context)
    else:
        request.session.clear()
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                # getting session data
                request.session['username'] = user.username
                return redirect("/home")
        else:
            context = {"form": form}
            return render(request, "login.html", context)
        

# function for logout from Application
def signout(request):
    request.session.clear()
    logout(request)
    return redirect('/login')