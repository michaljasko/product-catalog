from collections.abc import Iterable
from rest_framework.decorators import api_view
from rest_framework.response import Response
from system.models import (Attribute, AttributeName, AttributeValue, Product, ProductAttributes, Image,
                           ProductImage, Catalog)
from system.serializers import (AttributeNameSerializer, AttributeValueSerializer, AttributeSerializer,
                                ProductSerializer, ProductAttributesSerializer, ImageSerializer,
                                ProductImageSerializer, CatalogSerializer)
from system.utils import (import_attribute_name, import_attribute_value, import_attribute, import_product,
                          import_product_attributes, import_image, import_product_image, import_catalog,
                          get_object_list, get_object_detail)


@api_view(['POST'])
def import_data(request):
    # Check if data for import were provided in request
    if not request.data:
        return Response({"error": "No data provided"}, status=400)

    # Check if data for import are in correct iterable list format (not JSON string)
    if not (isinstance(request.data, Iterable) and not isinstance(request.data, str)):
        return Response({"error": "Invalid data provided - list required"}, status=400)

    created = 0
    skipped = 0

    # Iterate over each item and parse the data
    for item in request.data:
        import_result = None

        # Look for expected objects
        if "AttributeName" in item:
            import_result = import_attribute_name(item["AttributeName"])
        elif "AttributeValue" in item:
            import_result = import_attribute_value(item["AttributeValue"])
        elif "Attribute" in item:
            import_result = import_attribute(item["Attribute"])
        elif "Product" in item:
            import_result = import_product(item["Product"])
        elif "ProductAttributes" in item:
            import_result = import_product_attributes(item["ProductAttributes"])
        elif "Image" in item:
            import_result = import_image(item["Image"])
        elif "ProductImage" in item:
            import_result = import_product_image(item["ProductImage"])
        elif "Catalog" in item:
            import_result = import_catalog(item["Catalog"])

        # Log the import result
        if import_result is True:
            created += 1
        elif import_result is False:
            skipped += 1

    return Response({"message": f"Successfully processed {len(request.data)} items",
                     "created": created, "skipped": skipped}, status=200)


@api_view(['GET'])
def model_list(request, model_name):
    # Check provided model name
    if not isinstance(model_name, str):
        return Response({"error": "Model name missing or invalid"}, status=400)

    # Make the search case-insensitive
    name = model_name.lower()
    # Look for expected model names
    if name == "attributename":
        result = get_object_list(AttributeName)
    elif name == "attributevalue":
        result = get_object_list(AttributeValue)
    elif name == "attribute":
        result = get_object_list(Attribute)
    elif name == "product":
        result = get_object_list(Product)
    elif name == "productattributes":
        result = get_object_list(ProductAttributes)
    elif name == "image":
        result = get_object_list(Image)
    elif name == "productimage":
        result = get_object_list(ProductImage)
    elif name == "catalog":
        result = get_object_list(Catalog)
    else:
        return Response({"error": "Invalid model name provided"}, status=400)

    return Response({"items": result}, status=200)


@api_view(['GET'])
def model_detail(request, model_name, item_id):
    # Check provided model name
    if not isinstance(model_name, str):
        return Response({"error": "Model name missing or invalid"}, status=400)

    # Make the search case-insensitive
    name = model_name.lower()
    # Look for expected model names
    if name == "attributename":
        result = get_object_detail(AttributeName, item_id, AttributeNameSerializer)
    elif name == "attributevalue":
        result = get_object_detail(AttributeValue, item_id, AttributeValueSerializer)
    elif name == "attribute":
        result = get_object_detail(Attribute, item_id, AttributeSerializer)
    elif name == "product":
        result = get_object_detail(Product, item_id, ProductSerializer)
    elif name == "productattributes":
        result = get_object_detail(ProductAttributes, item_id, ProductAttributesSerializer)
    elif name == "image":
        result = get_object_detail(Image, item_id, ImageSerializer)
    elif name == "productimage":
        result = get_object_detail(ProductImage, item_id, ProductImageSerializer)
    elif name == "catalog":
        result = get_object_detail(Catalog, item_id, CatalogSerializer)
    else:
        return Response({"error": "Invalid model name provided"}, status=400)

    # If object was not found
    if result is None:
        return Response({"error": f"{model_name} with ID {item_id} not found"}, status=400)

    return Response({"item": result})
