from .import views
from django.urls import  path

urlpatterns = [
    path('createelectronic', views.create_electronic),
    path('getelectronic', views.get_electronic), 
    path('deleteelectronic', views.delete_electronic),
    path('addtocart', views.add_to_cart),
]
