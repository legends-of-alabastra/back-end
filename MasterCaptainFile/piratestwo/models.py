from django.db import models
from django.contrib.postgres.fields import ArrayField
import sys


# sys.path.insert(0, "/MasterCaptainFile/users/api")

# sys.path.append('../')
# from users.serializers import UserSerializer

# ROOM CLASS'S
#########################################################
#########################################################
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
        return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]

    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]

    def __str__(self):
        return self.title + self.description


# ITEM CLASS'S
##########################################################
#########################################################
class Items(models.Model):
    name = models.CharField(max_length=255, default="DEFAULT ITEM")
    description = models.CharField(max_length=255, default="DEFAULT DESCRIPTION")
    value = models.IntegerField(default=0)

    def location(self):
        return [self.x, self.y]

    def __str__(self):
        return self.name

class Weapon(Items):
    attack_power = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Gem(Items):
    rarity = models.CharField(default="", max_length=50)

    def __str__(self):
        return self.name


# Total gold carried by player
class Gold(Items):

    def __str__(self):
        return self.name


# PLAYER CLASS'S
#########################################################
#########################################################

class Player(models.Model):
    username = models.CharField(max_length=30, blank=False)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    # uuid = models.UUIDField(default = uuid.uuid4, unique=true)

    def location(self):
        return [self.x, self.y]

    def initialize(self):
        if self.currentRoom == 0:
            self.currentRoom = Room.objects.first().id
            self.save()

class Map(models.Model):
    tileset = ArrayField(ArrayField(models.IntegerField()))
    map = ArrayField(ArrayField(models.IntegerField()))
    colors = ArrayField(ArrayField(models.IntegerField()))
    
    def __str__(self):
        return self.tileset

class ItemLocation(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.PROTECT)
    x = models.IntegerField(default = 0)
    y= models.IntegerField(default = 0)
    item_id = models.IntegerField(default = 0)


class Merchant(models.Model):
    name = models.CharField(max_length=255, default="DEFAULT ITEM")
    description = models.CharField(max_length=255, default="DEFAULT DESCRIPTION")
    value = models.IntegerField(default=0)
    weapons_power =  models.CharField(max_length=255, default="DEFAULT DESCRIPTION")

class MerchantWeapons(Merchant):
    attack_power = models.IntegerField(default=0)

    def __str__(self):
        return self.name