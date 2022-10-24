from django.shortcuts import render, redirect
from product.models import Product, Category
from django.db.models import Q
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("/")

    else:
        form = SignupForm()

    return render(request, "core_pages/signup.html", {"form": form})


@login_required
def myaccount(request):
    if request.method == 'POST':
        
        user = request.user 
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')

        user.save()

        return redirect('myaccount')
    return render(request, "core_pages/myaccount.html")

@login_required
def edit_myaccount(request):

    # if request.method == 'POST':

    #     user = request.user 
    #     user.first_name = request.POST.get('first_name')
    #     user.last_name = request.POST.get('last_name')
    #     user.email = request.POST.get('email')
    #     user.username = request.POST.get('username')

    #     user.save()

    #     return redirect('myaccount')

    return render(request, "core_pages/edit_myaccount.html")




def home(request):
    products = Product.objects.all()[0:8]

    return render(request, "core_pages/index.html", {"products": products})


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get("category", "")

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get("query", "")

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        "products": products,
        "categories": categories,
        "active_category": active_category,
    }

    return render(request, "core_pages/shop.html", context)
