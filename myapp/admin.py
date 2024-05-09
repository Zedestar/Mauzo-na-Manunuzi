from django.contrib import admin
from .models import Product

# Register your models here.

#customizing the admin layout page
admin.site.site_header = "Buying and Selling Website"
admin.site.index_title = "ZEDEXY Company LTD"
admin.site.site_title = "Ukiishiwa Uzwa"


# Customizing the Product Model to include all its details
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc',  'price']
    search_fields = ('name',)

    # The function to set all product's price to Zero
    def set_product_price_zero(self, request, queryset):
        queryset.update('price')

    # The place we sert all our customized functions 
    actions = ('set_product_price_zero',)
    list_editable = ('price', 'desc')

# Registering the model and its Customizing list 
admin.site.register(Product, ProductAdmin)
