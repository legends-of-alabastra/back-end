from .models import Items, Map, ItemLocation, Merchant, PlayerWeapons
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
    items = ItemLocation.objects.values().all()

    return Response(list(items))

@api_view(["GET"])
def merchant_weapons(request):
    print('hi')
    all_weapons = Merchant.objects.values().all()
    print(list(all_weapons))
    return Response(all_weapons)


@api_view(["GET"])
def bigbang(request):
    item_location = ItemLocation.objects.all().delete()
    return Response(item_location)


@api_view(["PUT"])
def buy_weapon(request):
    name = request.data.get('name')
    weapon = Merchant.objects.values().get(name = request.data.get("name"))
    user = UserInfo.objects.values().get(id = request.data.get("id"))
    weapon_value = weapon['value']
    user_gem = user['gem']
    if weapon_value <= user_gem:
        print(user['gem'], 'PREV GEMS')
        new_gem = user_gem - weapon_value
        updated_user = UserInfo(id = user['id'], username = user['username'], gold = user['gold'], gem = new_gem)
        player_stuff = PlayerWeapons(player_id = user['id'], name = weapon['name'], description = weapon['description'], weapons_power = weapon['weapons_power'])
        updated_user.save()
        player_stuff.save()
        player_weapons = PlayerWeapons.objects.values().filter(player_id = user['id'])
        print(list(player_weapons))
        return Response(list(player_weapons))
    else:
        return Response( f"Sorry cannnot afford the {name}" )
