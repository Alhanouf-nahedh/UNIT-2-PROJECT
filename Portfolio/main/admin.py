from django.contrib import admin
from .models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "sent_at")
    list_filter = ("sent_at",)
admin.site.register(Message, MessageAdmin)