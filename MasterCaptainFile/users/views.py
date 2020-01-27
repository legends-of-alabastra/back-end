from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .models import UserInfo
import sys
sys.path.append("..")
from piratestwo.models import ItemLocation
from rest_framework import status
import json
from django.http import JsonResponse
import pusher
import sys
sys.path.append("..")
from piratestwo.models import ItemLocation

# Create your views here.
pusher_client = pusher.Pusher(
  app_id='937389',
  key='c94e812bb791c21a37e8',
  secret='e8ba260f0392ed97ff33',
  cluster='us2',
  ssl=True
)

@api_view(['GET'])
def pusher_item_locations(request):
    item_locations =  list(ItemLocation.objects.all().values())
    pusher_client.trigger('my-channel', 'itemArray', {'description': item_locations })
    return Response(item_locations)


@api_view(['POST'])
# POST to nitializes the player's inventory table
def player_items(request):
    if request.method == 'POST':
        data = UserInfo(id = request.data['id'], username = request.data['username'], gold = request.data['gold'], gem = request.data['gem'])
        data.save()
        user_items = UserInfo.objects.values().get(username = request.data['username'])
        return Response(user_items, status=status.HTTP_201_CREATED)
    return Response("sorry", status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
# PUT to update/add picked up items to their inventory
def add_items(request):
    new_items = ItemLocation.objects.all()
    print(new_items)
    if request.method == 'PUT':
        user = UserInfo.objects.values().get(id = request.data.get("id"))
        # is_gold = request.data['gold']
        # is_gem = request.data['gold']
        # print(is_gold, 'is gold')
        if request.data.get('gold'): 
            gold = user['gold']
            updated_gold = int(request.data['gold']) + int(gold)
            data = UserInfo(id = user['id'], username = user['username'], gold = updated_gold, gem = user['gem'])
            data.save()
        elif request.data.get('gem'):
            gem = user['gem']
            updated_gem = int(request.data['gem']) + int(gem)
            data = UserInfo(id = user['id'], username = user['username'],  gold = user['gold'], gem = updated_gem)
            data.save()
        
        ItemLocation.objects.filter(id = request.data.get('item_key')).delete() 

        pusher_client.trigger('my-channel', 'itemArray', {'description': list(ItemLocation.objects.all().values()) })
        return Response(user)