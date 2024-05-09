from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import User
from .models import Profile, User
from myapp.models import Product
from myapp.forms import FillingForm
from .forms import EditProfile
from django.shortcuts import get_object_or_404

# Create your views here.
# - This is for reistering the user
def register(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print("Ilipokea data zedexy")
        if form.is_valid():
            user = form.save()
            return redirect("users:createProfile")
        else:
            print("I think YOu provide bad data")
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context=context)

@login_required
def profile(request, id):
    my_profile = Profile.objects.get(id=id)
    my_products = Product.objects.filter(seller_name = request.user)
    context = {
        'user':my_profile,
        'my_products':my_products
    }
    return render(request, 'users/profile.html', context)
   

@login_required
def create_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        uploaded_image = request.FILES.get('upload')
        contact = request.POST.get('contact')
        
        if uploaded_image:
            profile.image = uploaded_image
        if contact:
            profile.contact = contact
        
        profile.save()
        return redirect('myapp:dashboard')
    context = {
        'profile':profile,
    }
    return render(request, 'users/createProfile.html', context=context)


def sellerProfile(request, pk):
    seller = Profile.objects.get(id=pk)
    context = {
        'seller': seller,
    }
    return render(request, 'users/sellerProfile.html', context=context)

def log_out(request):
    logout(request)
    return render(request, 'users/logout.html')


def View_item(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        'product': product,
    }
    return render(request, 'myapp/view.html', context=context)



@login_required
def delete_item(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product':product,
    }
    if request.method == 'POST':
        product.delete()
        return redirect("myapp:dashboard")
    return render(request, 'myapp/delete.html', context=context)




@login_required
def update_item(request, pk):
    product = Product.objects.get(id=pk) 
    if request.method == 'POST':
        form = FillingForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            print("Data were ipdated")
            return redirect("myapp:dashboard")
        else:
            print("The data provide were incorrect")
    else:
        form = FillingForm(instance=product)
    context = {
        'form':form,
        'product':product,
    }
    return render(request, "myapp/update.html", context=context)


def edit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form  = EditProfile(instance=profile)
    if request.method == 'POST':
        form  = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('users:Profile', profile.id)
    context = {
        'form':form,
        'profile':profile
    }
    return render(request, 'users/edit_profile.html', context=context)
    