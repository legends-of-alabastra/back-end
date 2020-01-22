from django.db import models

# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    n_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)

    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id

        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("The Room You're Trying To Go To Does Not Exist")
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print("Invalid Direction Input")
                return
            
            self.save()

    
    def playerNames(self, currentPlayerID):
        return [p.user.username for p in Player.objects.filter(currentRoom = self.id) if p.id != int(currentPlayerID)]

    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]


class Item(models.Model):
    name = models.CharField(max_length=255, default="DEFAULT ITEM")
    description = models.CharField(max_length=255, default="DEFAULT DESCRIPTION")
    value = models.IntegerField(default=0)

    
# class Player(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     currentRoom = models.IntegerField(default = 0)
#     uuid = models.UUIDField(default = uuid.uuid4, unique=true)

#     def initialize(self):
#         if self.currentRoom == 0:
#             self.currentRoom = Room.objects.first().id
#             self.save()
    
=======
# class Player(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     currentRoom = models.IntegerField(default = 0)
#     uuid = models.UUIDField(default = uuid.uuid4, unique=true)

#     def initialize(self):
#         if self.currentRoom == 0:
#             self.currentRoom = Room.objects.first().id
#             self.save()
    

#     def room(self):
#         try:
#             return Room.objects.get(id = self.currentRoom)
#         except Room.DoesNotExist:
#             self.initialize()
#             return self.room()


# @receiver(post_save, sender = User)

# def create_user_player(sender, instance, created, **kwargs):
#     if created:
#         Player.objects.create(user = instance)
#         Token.objects.create(user = instance)


# @receiver(post_save, sender = User)

# def save_user_player(sender, instance, **kwargs):
#     instance.player.save()