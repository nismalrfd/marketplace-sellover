from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def adminHome(request):
    return render(request, 'admin/signup.html')

def adminLogin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        if uname=='admin' or uname=='ADMIN' or uname=='Admin' and pwd=='admin':
            request.session['admin']=uname
            return redirect(adminHome)
        else:
            return HttpResponse('PLEASE ENTER A VALID USERNAME AND PASSWORD')
    else:
        return render(request,'admin/login.html')