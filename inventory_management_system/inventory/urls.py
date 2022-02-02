
from .views import *
from django.urls import path

urlpatterns = [
    path(r'', index, name='index'),
    path(r'volunteers/', display_volunteers, name="display_volunteers"),
    path(r'participates/', display_participates, name="display_participates"),
   

    path(r'add_laptop/', add_laptop, name="add_laptop"),
    path(r'add_desktop/', add_desktop, name="add_desktop"),
    
    path(r'laptops/edit_item/(?P<pk>\d+)/', edit_laptop, name="edit_laptop"),
    path(r'desktops/edit_item/(?P<pk>\d+)/', edit_desktop, name="edit_desktop"),
    

    path(r'laptops/delete/(?P<pk>\d+)/', delete_laptop, name="delete_laptop"),
    path(r'desktops/delete/(?P<pk>\d+)/', delete_desktop, name="delete_desktop"),
   

]
