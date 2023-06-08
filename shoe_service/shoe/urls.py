from .import views
from django.urls import  path

urlpatterns = [
    path('createshoe', views.create_shoe),
    path('getshoe', views.get_shoe), 
    path('deleteshoe', views.delete_shoe),
    path('addtocart', views.add_to_cart),
]
