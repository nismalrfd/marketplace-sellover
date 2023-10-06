from django.urls import path

from . import views

urlpatterns = [
    path('',views.items,name='items'),
    path('<int:pk>/',views.detail,name='detail'),
    path('new/',views.new,name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),


]