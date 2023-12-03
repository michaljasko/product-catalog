from collections.abc import Iterable
from rest_framework.decorators import api_view
from rest_framework.response import Response
from system.utils import import_item, get_model_by_name, get_object_list, get_object_detail


@api_view(['POST'])
def import_data(request):
    # Check if data for import were provided in request
    if not request.data:
        return Response({"error": "No data provided"}, status=400)

    # Check if data for import are in correct iterable list format (not JSON string)
    if not (isinstance(request.data, Iterable) and not isinstance(request.data, str)):
        return Response({"error": "Invalid data provided - list required"}, status=400)

    imported = 0
    skipped = 0

    # Iterate over each item and parse the data
    for item in request.data:
        # Check if item is a dictionary and skip if not
        if not isinstance(item, dict):
            skipped += 1
            continue

        # Use the first key of item as a model name and try to import item data
        model_name = list(item)[0]
        import_result = import_item(model_name, item[model_name])

        # Log the import result
        if import_result is True:
            imported += 1
        elif import_result is False:
            skipped += 1

    return Response({"message": f"Successfully processed {len(request.data)} items",
                     "imported": imported, "skipped": skipped}, status=200)


@api_view(['GET'])
def model_detail(request, model_name, item_id=None):
    model, serializer = get_model_by_name(model_name)
    if model is None or serializer is None:
        return Response({"error": "Invalid model name provided"}, status=400)

    if item_id is not None:
        # Provide single model instance by ID
        result = get_object_detail(model, item_id, serializer)
        if result is None:
            return Response({"error": f"{model_name} with ID {item_id} not found"}, status=400)
        return Response({"item": result}, status=200)
    else:
        # Provide list of model instances
        result = get_object_list(model, serializer)
        return Response({"items": result}, status=200)
