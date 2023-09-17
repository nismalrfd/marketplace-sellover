from django.urls import path

from . import views
app_name = 'adminpanel'
urlpatterns = [
    path('adminHome', views.adminHome, name='adminHome'),
    path('adminLogin', views.adminLogin, name='adminLogin'),

]