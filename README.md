
Project developed for the Evaluation of Extraordinary Knowledge in the Web Development II course, taken at the Federal Institute of Santa Catarina under the guidance of Professor Daniel Varela

### Screens

#### Login Screen
![Captura de tela de 2023-09-15 20-22-32](https://github.com/augustokemp/dev-web/assets/80912604/c0808682-61f8-43a5-88e7-d2b63c97a2a9)

#### Home Screen
![Captura de tela de 2023-09-15 20-22-38](https://github.com/augustokemp/dev-web/assets/80912604/ef424728-f7cd-43da-afd2-e2995115824d)

#### Users Screen
![Captura de tela de 2023-09-15 20-22-40](https://github.com/augustokemp/dev-web/assets/80912604/fb7d5a57-53a0-4274-b9eb-5e685c683e9e)


#### Create/Update user form
![Captura de tela de 2023-09-15 20-22-50](https://github.com/augustokemp/dev-web/assets/80912604/0773d0d0-0363-44b2-8004-ddd676cf0f75)

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

Other libraries & tools:
- Docker;
- Date-fns;
- SweetAlert2;
- MD Fonts & Icons;
- Hashids;
- Starlette;
- & More.
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
