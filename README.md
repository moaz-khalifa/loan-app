## Description

This is a bank app. We have many customers who can sign up. Each customer will login and can create many loans:
He will enter the parameters of the desired loan.
He can only enter the amount and the term of loan in years.
And then he will be able to see the amortization schedule of the loan. He can then apply for the loan. The status of the application will be pending.

Another role called bank admin user, can go and see the pending applications and approves the loan. The loan status becomes approved. Then the customer can see it.

## Prerequisites

Before getting started you should have the following installed and running:

- [X] Yarn
- [X] Vue Cli 3
- [X] Python 3
- [X] Pipenv

## Setup

Setup
```
$ yarn install
$ pipenv install --dev & pipenv shell
$ python manage.py migrate
```

## Running Development Servers

```
$ python manage.py runserver
```

From another tab in the same directory:

```
$ yarn serve
```

The Vuejs application will be served from `localhost:8080` and the Django Api
and static files will be served from `localhost:8000`.

## How to use

1- Run `localhost:8080` to register as a new user.
2- After registeration, you can login to start using the app
3- After login, you can request a new loan and check your loans history
4- Before requesting a new loan, you can check its amortization schedule by clicking on details button
5- To login as a bank admin, you first should register as any noraml user, then the django superuser should give you the Staff status permission from django admin portal. Once you granted this permission, you can login from the app to start approving or rejecting pending loans.

## Avaialble apps

`localhost:8080` is the app's portal through which the user can use the app (Vue app styled with vuetify)
`localhost:8000/api/` is the django rest framework portal
`localhost:8000/api/admin` is the django admin portal
