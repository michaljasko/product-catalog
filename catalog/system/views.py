from collections.abc import Iterable
from rest_framework.decorators import api_view
from rest_framework.response import Response
from system.utils import (import_attribute_name, import_attribute_value, import_attribute, import_product,
                          import_product_attributes, import_image, import_product_image, import_catalog)


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
