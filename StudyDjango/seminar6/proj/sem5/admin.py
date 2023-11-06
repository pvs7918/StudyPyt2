from django.contrib import admin

from .models import SaveCoin, Product

admin.site.register(SaveCoin)

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['price']
    list_filter = ['description']
    search_fields = ['name']
    search_help_text = 'Поиск по наименованию продукта'
    actions = [reset_quantity]
