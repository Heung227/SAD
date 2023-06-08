from .import views
from django.urls import path

urlpatterns = [
    path('productmodel', views.get_product_data),
    path('createproduct', views.create_product),
    path('deleteproduct', views.delete_product),
    path('getallproduct', views.get_all_product),
]
