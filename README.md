# budget_tool

**Author**: Chris L Chapman
**Version**: 0.3.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview

 scaffolding a new Django application to help manage some of your basic financials, though probably best to not put any actual data in here just yet! Your focus today is scaffolding, deployment and implementing the new class-based view controllers in place of function views.

Includes form input templates, which will allow user to add new Budgets and Transactions

Implementing a token-based authentication through the use of RESTful architecture. Your users will have the ability to register and login to your app through an endpoint provided by Django REST Framework.

 Now that your application handles authentication through your RESTful endpoints, you will implement the ability to manage resources as an authenticated user!

## Getting Started

clone the repo
    start a virtual enviroment
pipenv shell [or whatever virt env you prefer]
Change Time Zone as desired in the settings.py file, eg: TIME_ZONE = 'America/Los_Angeles'
    To start it up
docker-compose up [--build possibly]
    If port 5432 is already busy, from command line:
sudo service postgresql stop
    If requirements are not up to date:
pip freeze > requirements.txt
    If changes in Models, maybe Views, or Static need a new build
docker-compose down
docker-compose up --build
    If changes in simpliar stuff
docker-compose down
docker-compose up
    To see what is still around from previous builds
docker container ls -a
docker images ls
docker system df
    remove old stuff
docker container prune
docker image prune {removes unattached images}
docker container rm [container id]
docker image rm [image id]
docker system prune

