from .import views
from django.urls import  path

urlpatterns = [
    path('createimage', views.create_image),
    path('getallimage', views.get_alla_image)
]
