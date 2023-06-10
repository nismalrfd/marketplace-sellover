from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import NewitemForm, EdititemForm


# Create your views here.
@login_required(login_url='/login')
def items(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items= items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query)|Q(description__icontains=query) )


    context= {
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id),
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


@login_required(login_url='/login')
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

@login_required(login_url='/login')
def delete(request,pk):
    item = Item.objects.get(pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required(login_url='/login')
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
