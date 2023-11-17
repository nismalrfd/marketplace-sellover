from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from items.models import *


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items

    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')


#
# def registerPage(request):
#     form =UserCreationForm()
#
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'form':form
#
#     }
#     return render(request,'core/signupPage.html',context)
#
#
# def loginPage(request):
#     context = {
#
#     }
#     return render(request, 'core/login.html', context)


def loginPage(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            from django.contrib.auth.models import User
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.warning(request, 'User not Found ')
                return redirect('/login')
            # if not Profile.objects.filter(user = user_obj).first().is_verified:
            #     messages.warning(request, 'your profile not verified..')
            #     raise Exception('profile not verified')
            #
            user_obj = authenticate(username=username, password=password)

            if user_obj:
                login(request, user_obj)
                return redirect('/')

            messages.warning(request, 'wrong password ')
            return redirect('login')

        except Exception as e:
            messages.warning(request, 'Something went wrong')

    return render(request, 'core/login.html')



def register_view(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.warning(request, 'username already exists')
                return redirect('/register')
            if confirm_password and password and password != confirm_password:
                messages.warning(request, 'password not matching !')
                return redirect('/register')

            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()

            # Profile.objects.create(user= user_obj,token = genarate_random_string(20))

            messages.success(request, 'Account created')
            return redirect('login')
        except Exception as e:
            messages.warning(request, 'Something went wrong')


    return render(request, 'core/signupPage.html')
from django.http import JsonResponse
from django.contrib.auth.models import User

def check_username_availability(request):
    username = request.GET.get('username', None)
    if username is not None:
        is_available = not User.objects.filter(username=username).exists()
        return JsonResponse({'available': is_available})
    return JsonResponse({'available': False})

def logout_view(request):
    logout(request)
    return redirect('/')
