from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'created_at', 'end_at', 'plated_end_at')
    list_select_related = ('user', 'user')
    fields = ('user', 'book', 'plated_end_at')

