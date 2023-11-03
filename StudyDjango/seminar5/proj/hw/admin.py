from django.contrib import admin

from .models import Client, Category, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    # список полей для отображения в списке Админ.панели
    list_display = ['name', 'category', 'price', 'quantity']
    # поля только для чтения
    readonly_fields = ['date_added']
    ordering = ['-quantity']  # Сортировка
    list_filter = ['category', 'name', 'price']  # поля доступные для фильтрации (поиска)
    search_fields = ['description']  # текстовый поиск
    search_help_text = 'Поиск по полю Описание продукта (description)'  # описание к текстовому поиску
    actions = [reset_quantity]

    # fields = ['name', 'description', 'date_added', 'rating']  """Отдельный продукт."""
    # подробное отображение одной записи (с делением полей на абзацы)
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added', 'foto'],
            }
        ),
    ]


@admin.action(description="Сбросить полный адрес")
def reset_full_adress(modeladmin, request, queryset):
    queryset.update(full_adress='')


class ClientAdmin(admin.ModelAdmin):
    # список полей для отображения в списке Админ.панели
    list_display = ['name', 'phone', 'email', 'date_registered']
    # поля только для чтения
    readonly_fields = ['date_registered']
    ordering = ['name', 'date_registered']  # Сортировка
    list_filter = ['name', 'phone', 'email']  # поля доступные для фильтрации (поиска)
    search_fields = ['full_adress']  # текстовый поиск
    search_help_text = 'Поиск по полю полный адрес (full_adress)'
    actions = [reset_full_adress]
    # Отдельная запись
    fields = ['name', 'phone', 'email', 'full_adress', 'date_registered']


class OrderAdmin(admin.ModelAdmin):
    # список полей для отображения в списке Админ.панели
    list_display = ['client', 'order_summ', 'date_ordered']
    # поля только для чтения
    readonly_fields = ['date_ordered']
    ordering = ['client', 'date_ordered']  # Сортировка
    list_filter = ['client', 'order_summ', 'date_ordered']  # поля доступные для фильтрации (поиска)
    # Отдельная запись
    fields = ['client', 'order_summ', 'date_ordered', 'products']


admin.site.register(Client, ClientAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
