from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, MyPasswordChangeForm, CustomerProfileForm
from django.contrib import messages 
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q



def user_logout(request):
    logout(request)
    return render(request ,"app/home.html")


class ProductView(View):
 def get(self, request):
  drip = Product.objects.filter(category='D')
  pipe = Product.objects.filter(category='P')
  fitting = Product.objects.filter(category='F')
  tissue = Product.objects.filter(category='T')

  return render(request, 'app/home.html',{'drip':drip, 'pipe':pipe, 'fitting ':fitting, 'tissue':tissue})
  

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
 
class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
          item_already_in_cart = Cart.objects.filter(Q(product_id=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart})
    
def About_us(request):
 return render(request, 'app/about_us.html')

def Contact_us(request):
 return render(request, 'app/contact_us.html')

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart')

def show_cart(request):
  if request.user.is_authenticated:
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    # print(cart_product)
    if cart_product:
      for p in cart_product:
        tempamount = (p.quantity * p.product.discounted_price)
        amount += tempamount
        totalamount = amount + shipping_amount
      return render(request,'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount':amount})
    else:
      return render(request,'app/emptycart.html')

def plus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount 
      

    data = {
      'quantity': c.quantity,
      'amount':amount,
      'totalamount':amount + shipping_amount  
      }
    return JsonResponse(data)
  
def minus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity-=1
    c.save()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount 
    data = {
      'quantity': c.quantity,
      'amount':amount,
      'totalamount':amount + shipping_amount
      }
    return JsonResponse(data)
 
 
 
def remove_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.delete()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount 
     

    data = {
      'amount':amount,
      'totalamount':amount + shipping_amount 
      }
    return JsonResponse(data)

    


def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'add':add, 'active':'btn-primary'})

# @login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed': op})


def drip(request, data=None):
    if data is None:
        drip = Product.objects.filter(category='D')
    elif data == 'Jain' or data == 'Texamo' or data == 'Supreme' or data == 'Other':
        drip = Product.objects.filter(category='D', brand=data)
    elif data == 'below':
        drip = Product.objects.filter(category='D', discounted_price__lt=10000)
    elif data == 'above':
        drip = Product.objects.filter(category='D', discounted_price__gt=10000)
    else:
        drip = Product.objects.filter(category='D')
    return render(request, 'app/drip.html', {'drip': drip})

def pipe(request, data=None):
    if data is None:
        pipe = Product.objects.filter(category='P')
    elif data == 'Jain' or data == 'Supreme' or data == 'Other' or data == 'Texamo':
        pipe = Product.objects.filter(category='P', brand=data)
    else:
        pipe = Product.objects.filter(category='P')
    return render(request, 'app/pipe.html', {'pipe': pipe})

def tissue(request, data=None):
    if data is None:
        tissue = Product.objects.filter(category='T')
    elif data == 'Jain' or data == 'Other':
        tissue = Product.objects.filter(category='T', brand=data)
    else:
        tissue = Product.objects.filter(category='T')
    return render(request, 'app/tissue.html', {'tissue': tissue})

def fitting(request, data=None):
    if data is None:
        fitting = Product.objects.filter(category='F')
    elif data == 'Jain' or data == 'Supreme' or data == 'Other' or data == 'Texamo':
        fitting = Product.objects.filter(category='F', brand=data)
    else:
        fitting = Product.objects.filter(category='F')
    return render(request, 'app/fitting.html', {'fitting': fitting})

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html', {'form': form})
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations !! Registration Successfully')
   form.save()
  return render(request, 'app/customerregistration.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active':'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr,  name=name, mobile=mobile, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations!! Profile saved successfully")
            return redirect('profile')  # Redirect to profile page after successful form submission
        return render(request, 'app/profile.html', {'form': form, 'active':'btn-primary'})

@login_required
def checkout(request):
 user = request.user
 add = Customer.objects.filter(user=user)
 cart_item = Cart.objects.filter(user=user)
 amount = 0.0
 shipping_amount = 70.0
 totalamount = 0.0
 cart_product = [p for p in Cart.objects.all() if p.user == request.user]
 if cart_product:
   for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
      totalamount = amount + shipping_amount
 return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_item':cart_item})

@login_required
def payment_done(request):
  user = request.user
  custid = request.GET.get('custid')
  customer = Customer.objects.get(id=custid)
  cart = Cart.objects.filter(user=user)
  for c in cart:
    OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
    c.delete()
  return redirect("orders")
 