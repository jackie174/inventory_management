
from .views import *
from django.urls import path

urlpatterns = [
    path(r'', index, name='index'),
    path(r'volunteers/', display_volunteers, name="display_volunteers"),
    path(r'participates/', display_participates, name="display_participates"),
   

    path(r'add_volunteer/', add_volunteer, name="add_volunteer"),
    path(r'add_participate/', add_participate, name="add_participate"),
    
    path(r'volunteers/edit_item/(?P<pk>\d+)/', edit_volunteer, name="edit_volunteer"),
    path(r'participates/edit_item/(?P<pk>\d+)/', edit_participate, name="edit_participate"),
    

    path(r'volunteers/delete/(?P<pk>\d+)/', delete_volunteer, name="delete_volunteer"),
    path(r'participates/delete/(?P<pk>\d+)/', delete_participate, name="delete_participate"),
   

]
