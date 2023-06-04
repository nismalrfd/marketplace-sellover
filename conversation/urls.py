from django.urls import path

from . import views

urlpatterns = [
    path('new<int:item_pk>/',views.new_conversation,name='new'),


]