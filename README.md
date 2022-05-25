# eastvantage_task
It is a Basic address book in FastAPI and docker.

Steps for running the project:

    for running server - docker-compose up
    for shell docker-compose run --service-ports web bash

Steps need to be done initially:

    do - docker-compose up
    then run sudo chown -R 1001:1001 data in the project base directory
    exec into postgres container and create a database with name eastvantage_assignment
        docker exec -ti eastvantage_postgres bash
        psql -U user_name -W password
        create database eastvantage_assignment;
    then run - docker-compose up again all containers should work now

