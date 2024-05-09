from django.urls import path
from .import views



app_name = 'myapp'

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('base', views.base, name="base"),
    # path('delete/<int:pk>', views.delete_item, name="delete"),
    path('view/<int:pk>', views.View_item, name="view"),
    # path('update/<int:pk>', views.update_item, name="update"),
    path('add_item', views.addItemm, name="add_item"),
]


  
