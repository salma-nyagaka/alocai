[![Build Status](https://app.travis-ci.com/salma-nyagaka/alocai.svg?branch=develop)](https://app.travis-ci.com/salma-nyagaka/alocai)
[![Coverage Status](https://coveralls.io/repos/github/salma-nyagaka/alocai/badge.svg?branch=develop)](https://coveralls.io/github/salma-nyagaka/alocai?branch=develop)


## Alocai backend recruitment task
A Video Game  application

### Description
A Django web application that ....


### Development set up

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7.10
    ```

-   Check that PostgreSQL is installed and create the database:


-   Clone the foodapp repo and cd into it:

    ```
    git clone https://github.com/salma-nyagaka/foodapp
    ```

- Access the project

    ```
    cd alocai/alocaiapi
    ```

- Install virtualenv

    ```
    pip install virtualenv
    ```

-   Create the virtual environment:

    ```
    virtualenv venv
    ```

-   Activate the virtual environment:

    ```
    source venv/bin/activate
    ```

-   Create a .env file and the following configurations

    ```
        export DB_NAME="DB_NAME"
        export DB_USER="DB_USER"
        export DB_HOST="localhost"
        export DB_PASSWORD="DB_PASSWORD"
        export SECRET_KEY="#8-9*p&2kor^he5v2$tbm$q5x3+nh@q&^9zev2em5e$pr2=qf$"
        export DJANGO_SETTINGS_MODULE=foodapi.settings

    ```

-   Get environment variables:

    ```
    source .env
    ```

-   Apply migrations:

    ```
    python manage.py migrate
    ```

-   Run Docker to install dependancies and start the project:

    ```
    docker-compose up
    ```
 

 #### Endpoints
| REQUEST | DESCRIPTION  | URL  |
| :-----: | :-: | :-: |
| GET | Get DB connection status |  http://{{BASE_URL}}}}/api/v1/status |
| GET | Get DB connection status |  http://{{BASE_URL}}}}/api/v1/status |
| GET | Get documentation|  http://{{BASE_URL}}}}/docs |
| GET | Get games|  http://{{BASE_URL}}}}/api/v1/games |
