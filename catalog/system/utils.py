from django.apps import apps
from typing import Tuple, Union
from system.models import (Attribute, AttributeName, AttributeValue, Product, ProductAttributes, Image,
                           ProductImage, Catalog)
from system.serializers import (AttributeNameSerializer, AttributeValueSerializer, AttributeSerializer,
                                ProductSerializer, ProductAttributesSerializer, ImageSerializer,
                                ProductImageSerializer, CatalogSerializer)


# Define the types for system model classes and serializers
SystemModel = Union[Attribute, AttributeName, AttributeValue, Product, ProductAttributes, Image,
                    ProductImage, Catalog]
SystemModelSerializer = Union[AttributeNameSerializer, AttributeValueSerializer, AttributeSerializer,
                              ProductSerializer, ProductAttributesSerializer, ImageSerializer,
                              ProductImageSerializer, CatalogSerializer]


# Mapping of model names to their serializers
SERIALIZERS = {
    "AttributeName": AttributeNameSerializer,
    "AttributeValue": AttributeValueSerializer,
    "Attribute": AttributeSerializer,
    "Product": ProductSerializer,
    "ProductAttributes": ProductAttributesSerializer,
    "Image": ImageSerializer,
    "ProductImage": ProductImageSerializer,
    "Catalog": CatalogSerializer,
}


def import_item(model_name: str, data: dict) -> bool:
    """
    Import data for a given model and create or update its instances.
    Returns True if import was successful, False if data are invalid.
    """
    # Try to get model and serializer for given model name
    model, serializer = get_model_by_name(model_name)
    if model is None or serializer is None:
        return False

    # Check if input is a dictionary
    if not isinstance(data, dict):
        return False

    # Check if ID number is provided
    if not ("id" in data and data["id"] and isinstance(data["id"], int)):
        return False

    # Look for existing instance to update
    try:
        instance = model.objects.get(id=data["id"])
    except model.DoesNotExist:
        instance = None

    # Deserialize the input data and check its validity
    serializer_result = serializer(instance=instance, data=data)
    if serializer_result.is_valid():
        serializer_result.save()
        return True
    return False


def get_model_by_name(model_name: str) -> Tuple[Union[SystemModel, None], Union[SystemModelSerializer, None]]:
    """
    Return system model with serializer by its name, None if model or serializer could not be found.
    """
    # Check provided model name
    if not isinstance(model_name, str):
        return None, None

    # Search for a model by model name
    try:
        model = apps.get_model("system", model_name)
    except LookupError:
        return None, None

    # Get the serializer class from the mapping
    serializer = SERIALIZERS.get(model.__name__)
    if serializer is None:
        return model, None

    return model, serializer


def get_object_list(model: SystemModel, serializer: SystemModelSerializer) -> list:
    """
    Return list of all objects for given system model class.
    """
    items = model.objects.all()
    serializer_result = serializer(items, many=True)

    return serializer_result.data


def get_object_detail(model: SystemModel, item_id: int, serializer: SystemModelSerializer) -> Union[dict, None]:
    """
    Return serialized object for given system model class and ID, None if not found.
    """
    try:
        item = model.objects.get(id=item_id)
    except model.DoesNotExist:
        return None
    serializer_result = serializer(item)

    return serializer_result.data
