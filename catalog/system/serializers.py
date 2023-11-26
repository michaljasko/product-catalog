from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField
from system.models import (Attribute, AttributeName, AttributeValue, Product,
                           ProductAttributes, Image, ProductImage, Catalog)


class AttributeNameSerializer(ModelSerializer):
    class Meta:
        model = AttributeName
        fields = ["id", "nazev", "kod", "zobrazit"]


class AttributeValueSerializer(ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ["id", "hodnota"]


class AttributeSerializer(ModelSerializer):
    # Set alternative field names
    nazev_atributu_id = PrimaryKeyRelatedField(source='nazev_atributu', read_only=True)
    hodnota_atributu_id = PrimaryKeyRelatedField(source='hodnota_atributu', read_only=True)

    class Meta:
        model = Attribute
        fields = ["id", "nazev_atributu_id", "hodnota_atributu_id"]


class ProductSerializer(ModelSerializer):
    cena = SerializerMethodField()

    # Return price as a string
    def get_cena(self, obj):
        return str(obj.cena)

    class Meta:
        model = Product
        fields = ["id", "nazev", "description", "cena", "mena", "published_on", "is_published"]


class ProductAttributesSerializer(ModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = ["id", "attribute", "product"]


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "nazev", "obrazek"]


class ProductImageSerializer(ModelSerializer):
    # Set alternative field name
    obrazek_id = PrimaryKeyRelatedField(source='obrazek', read_only=True)

    class Meta:
        model = ProductImage
        fields = ["id", "product", "obrazek_id", "nazev"]


class CatalogSerializer(ModelSerializer):
    # Set alternative field names
    products_ids = PrimaryKeyRelatedField(many=True, source='products', read_only=True)
    attributes_ids = PrimaryKeyRelatedField(many=True, source='attributes', read_only=True)
    obrazek_id = PrimaryKeyRelatedField(source='obrazek', read_only=True)

    class Meta:
        model = Catalog
        fields = ["id", "nazev", "obrazek_id", "products_ids", "attributes_ids"]
