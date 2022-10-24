from django.contrib.auth import views 
from django.urls import path
from .views import home,shop,signup,myaccount,edit_myaccount
from product.views import product




urlpatterns = [
    path("", home,name='home'),
    path("signup/", signup,name='signup'),
    path("logout/", views.LogoutView.as_view(),name='logout'),
    path("myaccount/", myaccount,name='myaccount'),
    path("myaccount/edit",edit_myaccount,name='edit_myaccount'),
    path("login/",views.LoginView.as_view(template_name='core_pages/login.html'),name='login'),
    path("shop/", shop,name='shop'),
    path("shop/<slug:slug>/", product,name='product'),
]
