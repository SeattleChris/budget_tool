# budget_tool

**Author**: Chris L Chapman
**Version**: 0.2.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview

 scaffolding a new Django application to help manage some of your basic financials, though probably best to not put any actual data in here just yet! Your focus today is scaffolding, deployment and implementing the new class-based view controllers in place of function views.

Includes form input templates, which will allow user to add new Budgets and Transactions

## Getting Started

clone the repo
Start it up
    docker-compose up [--build possibly]
If port 5432 is already busy, from command line:
    sudo service postgresql stop
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


## Architecture

<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->
