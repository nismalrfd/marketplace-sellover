from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from core import views
from core.views import index, contact

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('register',views.registerPage,name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logout_view, name='logout'),

              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
