from django.contrib import admin

from task.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'content', 'receiver', 'shipping_time', 'is_send', 'is_active', 'created_at',
                    'updated_at']
    list_display_links = ['subject', 'content', ]
    list_filter = ['is_send', 'is_active', 'created_at', 'updated_at']
    search_fields = ['subject', 'content']
    save_on_top = True
