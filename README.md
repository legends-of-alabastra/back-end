## Table of Contents

- [Welcome](#welcome)
- [Tech Stack](#tech-stack)
- [Tables & Routes](#tables)

## Welcome

Find the production server at: https://alabastraapp.herokuapp.com/

This is the HQ of The Legends of Alabastra MUD Build Weeks Team. Where all the magic happens ;)


## Tech Stack
+ [Django](https://www.djangoproject.com/) was the Web framework used for rapid, secure, and clean design for the backend.
+ [Python](https://www.python.org/) was the programming language used to write the backend.
+ [PostgreSQL](https://www.postgresql.org/) was implemented as the preferred choice for the database.
+ [Pusher](https://pusher.com/docs/chatkit/core-concepts) was utilized to make server calls to the front end, so player's can receive real time feedback from other player's in the game.

## Tables

### Register New User
POST: https://alabastraapp.herokuapp.com/api/auth/register </br>

| Column        |     Type      |    Required   |   Unique      |
| ------------- | ------------- | ------------- | ------------- |
|  username     |  str          |   yes         |               |              
|  email        | str           |    yes        |  unique       |               
|  password     | str           |    yes        |               |               

### Login User
POST: api/auth/login </br>
When posted, it creates a session in the backend, and returns a token for the front end.

| Column        |     Type      |    Required   |   Unique      |           
| ------------- | ------------- | ------------- | ------------- | 
|  username     |  str          |   yes         |               |               
|  password     | str           |    yes        |               |               

### Logout User
GET: https://alabastraapp.herokuapp.com/api/auth/logout
Logs the user out of the backend session (remember to clear the cookie/local storage if you set the token there).

### Map's Data
GET: https://alabastraapp.herokuapp.com/map/
Return's the map's data for the front end to generate the player's map.

### Merchant's Inventory
GET: https://alabastraapp.herokuapp.com/api/merchant/
This returns the merchant's inventory for players to buy weapons or trade gold for gems.

### Receive every Item's Location
GET: https://alabastraapp.herokuapp.com/api/getItems/
This returns every item in the databases' location on the map.

### Item in current player's position
POST: https://alabastraapp.herokuapp.com/api/items/
The requirements are to send that player's current x and y coordinates to seek if an item is in their current location.

| Column        |     Type      |    Required   |   Unique      |            
| ------------- | ------------- | ------------- | ------------- | 
|  x     |  str          |   yes         |               |               
|  y     | str           |    yes        |               |               

### Player Picks up Item
POST: https://alabastraapp.herokuapp.com/additems/
The id sent has to be the player's id. The user can either encounter gold or gem when they find an item, so then what they find in the next row. 

| Column        |     Type      |    Required   |   Unique      |            
| ------------- | ------------- | ------------- | ------------- | 
|  id     |  str          |   yes         |               |               
|  gold or gem     | str           |    yes        |               |      

### Delete All Item's from the Map
GET: https://alabastraapp.herokuapp.com/api/bigbang/ </br>
#### Careful ^ </br>
This deletes all the items located in the map, from the database. Mainly used to add a new batch of Items.
