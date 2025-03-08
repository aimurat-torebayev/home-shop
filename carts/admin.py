from django.contrib import admin

from carts.models import Cart

#admin.site.register(Cart)

# чтобы внутри админки пользователя выводить его корзину
# и не забудь привезать в inlines в user.admin
class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity', 'created_timestamp')
    search_fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 1
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'quantity', 'created_timestamp',] # тут штука product__name не работает поэтому создали метод product_display
    list_filter = ['created_timestamp', 'user', 'product__name',] # product__name если надо взять поле из модели product то прибавляем __ и название поля
    
    # для анонимов там буде - вместо имени
    # можно их заменить на что то
    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
    
    def product_display(self, obj):
        return str(obj.product.name)

