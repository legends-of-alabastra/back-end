from .models import Items, map
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

@api_view(["POST"])
def item_info(request):
    player_location = request.data.get(location)
    try:
        item_data = Items.objects.values().get(x = player_location[0], y = player_location[1]))
        return Response(item_data)
    except ObjectDoesNotExist:
        return Response("Sorry nothing up in here")

