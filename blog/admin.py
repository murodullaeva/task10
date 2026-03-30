from django.contrib import admin
from .models import Friend

@admin.register(Friend)
class AcharyaFriendAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'AUID')
