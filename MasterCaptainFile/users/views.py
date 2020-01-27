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
def add_items(request, id):
    if request.method == 'PUT':
        gold = UserInfo.objects.values().get['gold']
        print(gold)
        gem = UserInfo.objects.values().get(gem)
        print(gem)