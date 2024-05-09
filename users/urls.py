from django.urls import path
from . import views
from django.contrib.auth import views as class_based_view

# - creating the Urls here

app_name = 'users'

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', class_based_view.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout', views.log_out, name="logout"),
    path('profile<int:id>', views.profile, name="Profile"),
    path('createProfile', views.create_profile, name="createProfile"),
    path('sellerProfile/<int:pk>', views.sellerProfile, name="sellerProfile"),   
    path('delete/<int:pk>', views.delete_item, name="delete"),
    path('view/<int:pk>', views.View_item, name="view"),
    path('update/<int:pk>', views.update_item, name="update"),
    path('edit_profile/<int:pk>', views.edit_profile, name="edit_profile"),
]