from django.urls import path

from . import views
app_name = 'conversation'
urlpatterns = [

     path('message/<int:pk>', views.message, name='message'),
     path('detail/<int:pk>', views.detail, name='detail'),

     path('inbox', views.inbox, name='inbox'),

]