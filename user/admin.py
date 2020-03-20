from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Post
from django.utils.html import format_html



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'groups', 'user_permissions', ('last_login'))}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'username')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)



class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['id', 'created_at', 'updated_at', 'user', 'show_post_detail_url']
    search_fields = ['text', 'user__email', ]

    def show_post_detail_url(self, obj):
        return format_html("<a href='/post/{url}/' target='_blank'>post link</a>", url=obj.id)

    show_post_detail_url.short_description = "Post URL"


admin.site.register(Post, PostAdmin)
admin.site.register(User, CustomUserAdmin)