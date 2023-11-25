from collections.abc import Iterable
from datetime import datetime
from decimal import Decimal
from typing import Union
from system.models import (Attribute, AttributeName, AttributeValue, Product,
                           ProductAttributes, Image, ProductImage, Catalog)

# Define the type for system model classes
SystemModel = Union[Attribute, AttributeName, AttributeValue, Product,
                  ProductAttributes, Image, ProductImage, Catalog]


def set_up_import(data: dict, model: SystemModel, required_keys: set[str]) -> Union[SystemModel, None]:
    """
    Basic checks and setup for data import into system models.
    Return new model instance if import is ready, None if data are invalid or already exist.
    """
    # Check if input is a dictionary
    if not isinstance(data, dict):
        return None

    # Check if required keys and id are provided
    if not required_keys.issubset(data.keys()) or data["id"] is None:
        return None

    try:
        # If object already exists, skip it
        model.objects.get(id=data["id"])
        return None
    except model.DoesNotExist:
        # Otherwise create new instance
        return model(id=data["id"])


def import_attribute_name(data: dict) -> bool:
    """
    Create AttributeName object.
    Return True if import was successful, False if data are invalid or already exist.
    """
    required_keys = {"id", "nazev"}

    # Create new object, if it does not exist yet and data are valid
    attribute_name = set_up_import(data, AttributeName, required_keys)
    if attribute_name is None:
        return False

    # Set the provided values
    attribute_name.nazev = data["nazev"]
    if "kod" in data:
        attribute_name.kod = data["kod"]
    if "zobrazit" in data:
        attribute_name.zobrazit = data["zobrazit"]
    attribute_name.save()

    return True


def import_attribute_value(data: dict) -> bool:
    """
    Create AttributeValue object.
    Return True if import was successful, False if data are invalid or already exist.
    """
    required_keys = {"id", "hodnota"}

    # Create new object, if it does not exist yet and data are valid
    attribute_value = set_up_import(data, AttributeValue, required_keys)
    if attribute_value is None:
        return False

    # Set the provided value
    attribute_value.hodnota = data["hodnota"]
    attribute_value.save()

    return True


def import_attribute(data: dict) -> bool:
    """
    Create Attribute object.
    Return True if import was successful, False if data are invalid or already exist.
    """
    required_keys = {"id", "nazev_atributu_id", "hodnota_atributu_id"}

    # Create new object, if it does not exist yet and data are valid
    attribute = set_up_import(data, Attribute, required_keys)
    if attribute is None:
        return False

    # Look for objects by given ids
    try:
        attribute_name = AttributeName.objects.get(id=data["nazev_atributu_id"])
    except AttributeName.DoesNotExist:
        return False
    try:
        attribute_value = AttributeValue.objects.get(id=data["hodnota_atributu_id"])
    except AttributeValue.DoesNotExist:
        return False

    # Set the values if objects with given ids exist
    attribute.nazev_atributu = attribute_name
    attribute.hodnota_atributu = attribute_value
    attribute.save()

    return True


def import_product(data: dict) -> bool:
    """
    Create Product object.
    Return True if import was successful, False if data are invalid or already exist.
    """
    required_keys = {"id", "nazev", "cena", "mena"}

    # Create new object, if it does not exist yet and data are valid
    product = set_up_import(data, Product, required_keys)
    if product is None:
        return False

    # Set the provided values
    product.nazev = data["nazev"]
    product.mena = data["mena"]
    if data["cena"]:
        # Convert a price string to a decimal number
        product.cena = Decimal(data["cena"])
    if "description" in data:
        product.description = data["description"]
    if "published_on" in data and data["published_on"]:
        # Convert a date-time string to a datetime object
        product.published_on = datetime.fromisoformat(data["published_on"].replace('Z', '+00:00'))
    if "is_published" in data:
        product.is_published = data["is_published"]
    product.save()

    return True


def import_product_attributes(data: dict) -> bool:
    """
    Create ProductAttributes object.
    Return True if import was successful, False if data are invalid or already exist.
    """
    required_keys = {"id", "attribute", "product"}

    # Create new object, if it does not exist yet and data are valid
    product_attribute = set_up_import(data, ProductAttributes, required_keys)
    if product_attribute is None:
        return False

    # Look for objects by given ids
    try:
        attribute = Attribute.objects.get(id=data["attribute"])
    except Attribute.DoesNotExist:
        return False
    try:
        product = Product.objects.get(id=data["product"])
    except Product.DoesNotExist:
        return False

    # Set the values if objects with given ids exist
    product_attribute.attribute = attribute
    product_attribute.product = product
    product_attribute.save()

    return True


def import_image(data: dict) -> bool:
    """
    Create Image object.
    Return True if import was successful, False if data are invalid or already exist.
    """
    required_keys = {"id", "obrazek"}

    # Create new object, if it does not exist yet and data are valid
    image = set_up_import(data, Image, required_keys)
    if image is None:
        return False

    # Set the provided values
    image.obrazek = data["obrazek"]
    if "nazev" in data:
        image.nazev = data["nazev"]
    image.save()

    return True


def import_product_image(data: dict) -> bool:
    """
    Create ProductImage object.
    Return True if import was successful, False if data are invalid or already exist.
    """
    required_keys = {"id", "nazev", "product", "obrazek_id"}

    # Create new object, if it does not exist yet and data are valid
    product_image = set_up_import(data, ProductImage, required_keys)
    if product_image is None:
        return False

    # Look for objects by given ids
    try:
        product = Product.objects.get(id=data["product"])
    except Product.DoesNotExist:
        return False
    try:
        obrazek = Image.objects.get(id=data["obrazek_id"])
    except Image.DoesNotExist:
        return False

    # Set the values if objects with given ids exist
    product_image.nazev = data["nazev"]
    product_image.product = product
    product_image.obrazek = obrazek
    product_image.save()

    return True


def import_catalog(data: dict) -> bool:
    """
    Create Catalog object.
    Return True if import was successful, False if data are invalid or already exist.
    """
    required_keys = {"id", "nazev"}

    # Create new object, if it does not exist yet and data are valid
    catalog = set_up_import(data, Catalog, required_keys)
    if catalog is None:
        return False

    # Look for objects by given ids
    try:
        obrazek = Image.objects.get(id=data["obrazek_id"])
    except Image.DoesNotExist:
        obrazek = None

    # Set the values if objects with given ids exist
    catalog.nazev = data["nazev"]
    catalog.obrazek = obrazek
    catalog.save()

    # Set products and attributes if ids are provided and objects exist
    if "products_ids" in data and data["products_ids"] and isinstance(data["products_ids"], Iterable):
        for product_id in data["products_ids"]:
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return False
            catalog.products.add(product)
    if "attributes_ids" in data and data["attributes_ids"] and isinstance(data["attributes_ids"], Iterable):
        for attribute_id in data["attributes_ids"]:
            try:
                attribute = Attribute.objects.get(id=attribute_id)
            except Attribute.DoesNotExist:
                return False
            catalog.attributes.add(attribute)
    catalog.save()

    return True
