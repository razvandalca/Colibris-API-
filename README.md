# Colibris POC Api

## Components

- `colibris-web` 
  - The django web application.
- `colibris-db`
  - The postgres DB


*Note: I have left the .env file in the repo even if it's not recomanded in order for you not to create it based on the .env.example file **
**Note: When the web app is starting if no data is found it will load the data using a custom command automatically **

## How to run locally ?
1. `cd` in the location you have cloned the repo
2. Run `docker-compose up`
3. Verify all containers are up and running `docker ps --filter "name=colibris" `

```
CONTAINER ID   IMAGE                COMMAND                  CREATED       STATUS       PORTS                    NAMES
1b5c797ec162   colibris             "sh -c ' python mana…"   2 hours ago   Up 2 hours   0.0.0.0:8000->8000/tcp   colibris-web
79320a1a1516   postgres:14-alpine   "docker-entrypoint.s…"   2 hours ago   Up 2 hours   0.0.0.0:5432->5432/tcp   colibris-db

```

## How to use the endpoints?
I have  used Postman and DRF Browsable API.
Just open http://0.0.0.0:8000/api/employees in a browser ,and you can use the api directly from there.
All statistic data is under /employees/<statistic>. In browsable api you can see them under extra actions.

