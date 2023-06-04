from django.shortcuts import render, redirect

from conversation.forms import ConversationMessageForm
from conversation.models import Conversation
from items.models import Item


# Create your views here.


def new_conversation(request,item_pk):
    item = Item.objects.get(pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        pass #redirect to conversation
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.created(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('detail',pk=item_pk)
        else:
            form = ConversationMessageForm()
        context = {
            'form':form,
        }
        return render(request,'conversation/new.html',context)
