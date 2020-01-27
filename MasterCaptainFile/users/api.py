from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
import pusher
import sys
sys.path.append("..")
from piratestwo.models import ItemLocation

pusher_client = pusher.Pusher(
  app_id='937389',
  key='c94e812bb791c21a37e8',
  secret='e8ba260f0392ed97ff33',
  cluster='us2',
  ssl=True
)

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        pusher_client.trigger('my-channel', 'room', {'description': f'{user} has just became a Pirate of Alabastra!'})
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        pusher_client.trigger('my-channel', 'room', {'description': f'{user} has logged in'})
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "item_locations": item_locations
        })

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = {
        permissions.IsAuthenticated,
    }
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user