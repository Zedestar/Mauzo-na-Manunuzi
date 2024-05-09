from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import FillingForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.



@login_required
def dashboard(request):
    page_obj = products = Product.objects.all()

    product_name = request.GET.get('product_name')
    if product_name != "" and product_name is not None:
        page_obj = products.filter(name__icontains=product_name)

    paginate_by = 2
    paginator = Paginator(page_obj, paginate_by)
    page_number = request.GET.get('page')

   

    # PAGIANATION
    # Trying to get the page of the objects stored
    try:
        page_obj = paginator.get_page(page_number)
    except :
        # Handle the case when the page number is out of range
        page_obj = paginator.get_page(1)  # Show the first page

    # Passing the contents to the context
    context = {
        'all_products': products,  # Use 'all_products' for the entire queryset
        'page': page_obj,
    }
    return render(request, 'myapp/dashboard.html', context=context)





@login_required
def View_item(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        'product': product,
    }
    return render(request, 'myapp/view.html', context=context)


@login_required
def addItemm(request):
    form = FillingForm()
    if request.method == 'POST':
        form = FillingForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller_name = request.user
            product.save()
            return redirect("myapp:dashboard")
        else:
            print("The given data is inccorect")
    context = {
        'form':form,
    }
    return render(request, "myapp/add_item.html", context=context)
    



def base(request):
    return render(request, 'myapp/base.html')