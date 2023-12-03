from rest_framework.serializers import ModelSerializer, DecimalField, ValidationError
from decimal import Decimal, InvalidOperation
from system.models import (Attribute, AttributeName, AttributeValue, Product,
                           ProductAttributes, Image, ProductImage, Catalog)


class AttributeNameSerializer(ModelSerializer):
    class Meta:
        model = AttributeName
        fields = ["id", "name", "code", "is_visible"]

    def to_internal_value(self, data):
        # Remap the input data field names
        remapped_data = {
            "id": data.get("id"),
            "name": data.get("nazev"),
            "code": data.get("kod", None),
            "is_visible": data.get("zobrazit", False)
        }
        return super().to_internal_value(remapped_data)


class AttributeValueSerializer(ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ["id", "value"]

    def to_internal_value(self, data):
        # Remap the input data field names
        remapped_data = {
            "id": data.get("id"),
            "value": data.get("hodnota")
        }
        return super().to_internal_value(remapped_data)


class AttributeSerializer(ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["id", "attribute_name", "attribute_value"]

    def to_internal_value(self, data):
        # Remap the input data field names
        remapped_data = {
            "id": data.get("id"),
            "attribute_name": data.get("nazev_atributu_id"),
            "attribute_value": data.get("hodnota_atributu_id")
        }
        return super().to_internal_value(remapped_data)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "currency", "published_on", "is_published"]

    def to_internal_value(self, data):
        # Ensure that price is a valid Decimal
        try:
            price = Decimal(data.get("cena", "0.00"))
        except InvalidOperation:
            raise ValidationError({"cena": "Invalid price format"})

        # Remap the input data fields
        remapped_data = {
            "id": data.get("id"),
            "name": data.get("nazev"),
            "description": data.get("description", None),
            "price": price,
            "currency": data.get("mena", "CZK"),
            "published_on": data.get("published_on"),
            "is_published": data.get("is_published", False)
        }
        return super().to_internal_value(remapped_data)


class ProductAttributesSerializer(ModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = ["id", "attribute", "product"]


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "name", "image_url"]

    def to_internal_value(self, data):
        # Remap the input data field names
        remapped_data = {
            "id": data.get("id"),
            "name": data.get("nazev", None),
            "image_url": data.get("obrazek")
        }
        return super().to_internal_value(remapped_data)


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "name", "product", "image"]

    def to_internal_value(self, data):
        # Remap the input data field names
        remapped_data = {
            "id": data.get("id"),
            "name": data.get("nazev"),
            "product": data.get("product"),
            "image": data.get("obrazek_id")
        }
        return super().to_internal_value(remapped_data)


class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = ["id", "name", "image", "products", "attributes"]

    def to_internal_value(self, data):
        # Remap the input data field names
        remapped_data = {
            "id": data.get("id"),
            "name": data.get("nazev"),
            "image": data.get("obrazek_id", None),
            "products": data.get("products_ids", []),
            "attributes": data.get("attributes_ids", [])
        }
        return super().to_internal_value(remapped_data)
