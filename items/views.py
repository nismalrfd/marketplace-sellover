from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import NewitemForm, EdititemForm


# Create your views here.
def items(request):
    items = Item.objects.filter(is_sold=False)
    context= {
        'items':items
    }
    return render(request,'item/items.html',context)

def detail(request,pk):
    item = Item.objects.get(pk=pk)
    related_items =Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'item':item,
        'related_items':related_items
    }
    return render(request,'item/detail.html',context)


@login_required()
def new(request):
    if request.method == 'POST':
        form = NewitemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('detail',pk=item.id)
    form = NewitemForm()
    context = {
        'form':form,
        'title':'New item'
    }
    return render(request,'item/form.html',context)

@login_required()
def delete(request,pk):
    item = Item.objects.get(pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required()
def edit(request,pk):
    item = Item.objects.get(pk=pk,created_by=request.user)

    if request.method == 'POST':
        form = EdititemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()

            return redirect('detail',pk=item.id)
    else:
        form = EdititemForm(instance=item)

    context = {
        'form':form,
        'title':'Edit item'
    }
    return render(request,'item/form.html',context)
