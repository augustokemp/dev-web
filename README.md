# Extraordinario Aproveitamento: BSI21 Desenvolvimento Web 2

```
## Ementa

O desenvolvimento de aplicações web com utilização de frameworks e banco de dados. Linguagens e ambientes de concepção de projeto de sistemas na web. Inovações de projeto e utilização de ferramentas avançadas.

## Objeto avaliativo de extraordiunário aproveitamento

Desenvolva um cadastro de usuários com as seguintes características:
- O cadastro deve conter os seguintes campos,
  - nome completo
  - email
  - senha
  - endereço (sendo necessário permitir cadastro de um ou mais endereços)
- O sistema deve permitir que qualquer usuário cadastrado e logado possa ver os seu dados dados e dos demais
- Alterações de informações só podem ser permitidas pelo usuário dono dos dados e/ou por um usuário que tenha permissão para este tipo de alteração
- Para criação de novos usuários, somente um usuário com esta permissão poderá fazê-lo

O frontend deve preferencialmente ser desenvolvido utilizando  React e deve conter as seguintes telas:
- Tela de login
- Tela de lista geral dados de usuários (paginada e com campo de pesquisa/filtro)
- Tela de criação/alteração de novo usuário

O backend deve preferencialmente ser preferencialmente uma API Rest ou GraphQL utilizando preferencialmente NodeJS (express), MySQL/MariaDB.
```

```
Projeto desenvolvido para Avialiação do Extraordinário Saber
da disciplina de Desenvolvimento Web II, cursada no Instituto
Federal Catarinense sob a direção do professor Daniel Varela.
```

### Linguagens & Frameworks

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

### Requerimentos:

```
docker & docker-compose
```

## Inicialização

```
1. cd dev-web
2. docker-compose up
3. [Localhost](http://localhost:8080/)
```
