## Table of Contents

- [Welcome](#welcome)
- [Tables & Routes](#tables)


## Welcome

Find the production server at: https://workouttrackerprod.herokuapp.com/

This is the HQ of The Legends of Alabastra MUD Build Weeks Team. Where all the magic happens ;)


## Tables

### Register New User
| Column        |     Type      |    Required   |   Unique      |     Key       | 
| ------------- | ------------- | ------------- | ------------- | ------------- |
|  username     |  str          |   yes         |               |               |
|  email        | str           |    yes        |  unique       |               |
|  password     | str           |    yes        |               |               |

Route

POST: api/auth/register </br>
Requirements in the table

### Login User

| Column        |     Type      |    Required   |   Unique      |     Key       | 
| ------------- | ------------- | ------------- | ------------- | ------------- |
|  username     |  str          |   yes         |               |               |
|  password     | str           |    yes        |               |               |

Route

POST: api/auth/login </br>
Requirements in the table

When posted, it creates a session in the backend, and returns a token.

### Logout User
GET: api/auth/logout

Logs the user out of the backend session.

