from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .models import UserInfo
from rest_framework import status
import json
from django.http import JsonResponse

# Create your views here.

@api_view(['POST'])
def player_items(request):
    if request.method == 'POST':
        data = UserInfo(id = request.data['id'], username = request.data['username'], gold = request.data['gold'], gem = request.data['gem'])
        data.save()
        user_items = UserInfo.objects.values().get(username = request.data['username'])
        return Response(user_items, status=status.HTTP_201_CREATED)
    return Response("sorry", status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def add_items(request):
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
            return Response(user)
        elif request.data.get('gem'):
            gem = user['gem']
            updated_gem = int(request.data['gem']) + int(gem)
            data = UserInfo(id = user['id'], username = user['username'],  gold = user['gold'], gem = updated_gem)
            data.save()
            return Response(user)