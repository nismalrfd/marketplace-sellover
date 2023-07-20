from django.contrib import admin

from conversation.models import *

# Register your models here.
admin.site.register(Conversation)
admin.site.register(ConversationMessage)