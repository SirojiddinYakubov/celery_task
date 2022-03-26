from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name',
                    'is_active', 'is_superuser', 'is_staff', 'date_joined', 'last_login']
    list_display_links = ['email', 'first_name', 'last_name', ]
    list_filter = ['is_active', 'is_superuser', 'is_staff']
    search_fields = ['first_name', 'last_name', 'email']
    save_on_top = True
