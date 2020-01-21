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

