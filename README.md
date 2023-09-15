
Project developed for the Evaluation of Extraordinary Knowledge in the Web Development II course, taken at the Federal Institute of Santa Catarina under the guidance of Professor Daniel Varela

### Goals

```
Develop a user registration system with the following features:

The registration must include the following fields:
- Full name
- Email
- Password
- Address (allowing the registration of one or more addresses if necessary)

The system should allow any registered and logged-in user to view their own data and the data of others.
Changes to information can only be allowed by the user who owns the data and/or by a user who has permission for this type of alteration.
For creating new users, only a user with this permission can do so.
The frontend should preferably be developed using React and should include the following screens:

Login screen
General user data list screen (paginated with a search/filter field)
New user creation/modification screen
The backend should preferably be an API, either Rest or GraphQL, preferably using Node.js (Express), and MySQL/MariaDB.
```


### Languages & Frameworks

```
Frontend:
- TypeScript (Programming Language)
- VueJS 2.7 (Web UI Framework)
- Vuetify 2 (Vue UI Library)
- Axios (Node HTTP Client)
- Lodash (JavaScript Utility Library)

Backend:
- Python 3 (Programming Language)
- FastAPI (API Web Framework)
- Uvicorn (ASGI Web Server)
- PostgreSQL (SQL DB)
- SQLAlchemy (Python SQL ORM)
- Pydantic (Data Validation Library)
```

### Requirements:

```
docker & docker-compose
```

## Initialization

```
1. cd dev-web
2. docker-compose up
3. [Localhost](http://localhost:8080/)
```
