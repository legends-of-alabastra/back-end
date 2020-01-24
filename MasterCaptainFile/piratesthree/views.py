from .models import Items
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist


@api_view(["POST"])
def item_info(request):
    player_location_x = request.data.get("x")
    player_location_y = request.data.get("y")
    print(player_location_x)

    try:
        item_data = Items.objects.values().get(x=player_location_x, y=player_location_y)
        return Response(item_data)
    except ObjectDoesNotExist:
        return Response("Sorry nothing up in here")
