crypto-app
==========

Mobile cryptocurrency app with React Native, Django and GraphQL
Technology stack:
- Django
- React native with Typescript
- GraphQL: Graphene + Apollo

## Requirements

- Python >3.6
- pipenv

## Instructions

### Backend

The first time run the following on a terminal
```
pipenv shell
cd backend
pipenv install
python manage.py migrate
```
and then each time you want to run the backend run the follwoing:
```
pipenv shell
cd backend
python manage.py runserver
```

### Mobile apps

```
cd mobile
yarn install
yarn start
```