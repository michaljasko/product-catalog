from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def import_data(request):
    print(request.data)

    return Response({"done": True})
