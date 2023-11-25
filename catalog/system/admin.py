from django.contrib import admin
from system.models import (Attribute, AttributeName, AttributeValue, Product,
                           ProductAttributes, Image, ProductImage, Catalog)

class ProductAttributesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Attribute)
admin.site.register(AttributeName, search_fields=['nazev', 'kod'])
admin.site.register(AttributeValue, search_fields=['hodnota'])
admin.site.register(Product, search_fields=['nazev', 'description'])
admin.site.register(ProductAttributes, ProductAttributesAdmin)
admin.site.register(Image)
admin.site.register(ProductImage)
admin.site.register(Catalog, search_fields=['nazev'])
