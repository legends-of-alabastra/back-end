from .models import Items, Map, ItemLocation, Merchant
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .map_gen.generate_map import generate_map
from .map_gen.tileset import tileset
from .map_gen.config import config
from rest_framework import status
from .serializers import MapSerializer
from .map_data import map_data
import sys
sys.path.append("..")
from users.models import UserInfo



@api_view(["POST"])
def item_location(request):
    player_location_x = request.data.get("x")
    player_location_y = request.data.get("y")

    try:
        print('trying to get item_location')
        item_location = ItemLocation.objects.values().get(x=player_location_x, y=player_location_y)
        print("this is the item_location")
        item_key = item_location.get('id')
        print("this is the item_key")
        item_data = Items.objects.values().get(id = item_location['item_id'])
        print('Passed the item_data')
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
    items = Items.objects.values().all()

    return Response(list(items))

@api_view(["GET"])
def merchant_weapons(request):
    print('hi')
    all_weapons = Merchant.objects.values().all()
    print(list(all_weapons))
    return Response(all_weapons)

@api_view(["POST"])
def buy_weapon(request):
    print(request.data.get(''))
    weapon = Merchant.objects.values().get(name = request.data.get("name"))
    user = UserInfo.objects.values().get(id = request.data.get("id"))
    if request.data.get('gold'):
        gold = user['gold']
        item_cost = weapon['values']
        print(gold, item_cost)




@api_view(["GET"])
def bigbang(request):
    item_location = ItemLocation.objects.all().delete()
    return Response(item_location)