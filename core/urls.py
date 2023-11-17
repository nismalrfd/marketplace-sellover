from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from core import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('register_view',views.register_view,name='register_view'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('check_username_availability', views.check_username_availability, name='check_username_availability'),

              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
