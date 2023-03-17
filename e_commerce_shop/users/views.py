from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import forms
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from payment.models import Order
from payment.models import OrderItem

User = get_user_model()

# Create your views here.
@csrf_protect
def register(request):
    is_error = False
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if len(first_name) == 0 or len(last_name) == 0:
            is_error = True
            messages.error(request, "Please provide your first and last names")
        if len(password1) == 0 or password1 != password2:
            is_error = True
            messages.error(request, "Password do not match or were not entered.")
        if len(username) == 0 or User.objects.filter(username=username).exists():
            is_error = True
            messages.error(request, "Username already taken or was not entered.")
        if len(email) == 0 or User.objects.filter(email=email).exists():
            is_error = True
            messages.error(request, "User with this email already exists, or email was not entered.")
        if not is_error:
            try:
                User.objects.create_user(first_name=first_name, last_name=last_name,username=username, email=email, password=password1)
            except Exception as err:
                is_error = True
                messages.erro(request, str(err))
        if not is_error:
            messages.success(request, f'user {username} has been succesfully registered. You can log in now.')
            return redirect(reverse_lazy('login'))
    return render(request, 'registration/registration.html')


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required
def track_orders(request):
    all_orders = Order.objects.filter(user=request.user.id)
    return render(request, 'users/my-orders.html', {'all_orders': all_orders})

@login_required
def order_details(request,pk):
    order = Order.objects.get(id=pk)
    order_items = OrderItem.objects.filter(order=order)
    order_shipping = ShippingAddress.objects.get(id=order.shipping_address.id)
    return render(request, 'users/order-details.html', {
        'order': order, 
        'order_items': order_items, 
        'shipping_address': order_shipping} )

@login_required
def profile_management(request):
    user_form = forms.UserUpdateForm(instance=request.user)
    if request.method == 'POST':
        user_form = forms.UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.info(request, 'Update success!')
            return redirect('dashboard')
    return render(request, 'users/profile-management.html', {
        'user_form': user_form
    })

@login_required
def manage_shipping(request):
    try:
        shipping_form = ShippingAddress.objects.get(user=request.user.id)
    except ShippingAddress.DoesNotExist:
        shipping_form = None
    form = ShippingForm(instance=shipping_form)
    if request.method == 'POST':
        form = ShippingForm(request.POST, instance=shipping_form)
        if form.is_valid():
            shipping_user = form.save()
            shipping_user.user = request.user
            shipping_user.save()
            messages.info(request, 'Shipping form was added successfully!')
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'users/manage-shipping.html', context=context)

@login_required
def delete_account(request):
    user = User.objects.get(id=request.user.id)
    print(user)
    if request.method == 'POST':
        user.delete()
        messages.info(request, 'Account deleted')
        return redirect('home-page')
    return render(request, 'users/delete-account.html')

