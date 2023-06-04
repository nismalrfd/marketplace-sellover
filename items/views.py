from django.shortcuts import render
from .models import *
# Create your views here.
def detail(request,pk):
    item = Item.objects.get(pk=pk)
    related_items =Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'item':item,
        'related_items':related_items
    }
    return render(request,'item/detail.html',context)