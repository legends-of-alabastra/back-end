from .models import Items, Map, ItemLocation
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .map_gen.generate_map import generate_map
from .map_gen.tileset import tileset
from .map_gen.config import config
from rest_framework import status
from .serializers import MapSerializer
from .map_data import map_data

@api_view(["POST"])
def item_location(request):
    player_location_x = request.data.get("x")
    player_location_y = request.data.get("y")

    try:
        item_location = ItemLocation.objects.values().get(x=player_location_x, y=player_location_y)
        item_key = item_location.get('id')
        item_data = Items.objects.values().get(id = item_location['item_id'])
        item_data['item_key'] = item_key
        print(item_data)
        return Response(item_data)
    except ObjectDoesNotExist:
        return Response("Sorry nothing up in here")

@api_view(["GET"])
def map(request):
        return Response(map_data)

@api_view(["GET"])
def get_items(request):
    items = Items.object.all()

    return Response(items)


# @api_view(["POST"])
# def player_info(request):
#     try:
#         player_data = Player.objects.values().get(email=request.data.get('email'))
#         current_city = map.search_map(player_data.get('city'))
#         if current_city == -1:
#             return Response("Player City does not exit")
#         elif current_city != -1:
#             player_data['left'] = current_city.left.city if current_city.left else None
#             player_data['right'] = current_city.right.city if current_city.right else None
#             player_data['previous'] = current_city.previous.city if current_city.previous else None
#         return Response(player_data)
#     except ObjectDoesNotExist:
#         return Response("Invalid email")
