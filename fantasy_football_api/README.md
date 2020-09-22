Open in the online Swagger Editor [here](https://editor.swagger.io/)

Run Swagger-UI locally from this directory, assuming [Docker](https://docs.docker.com/get-docker/) is installed, via the following command:

```bash
docker run -p 8081:8080 -e SWAGGER_JSON=/tmp/fantasy_football_api.json -v `pwd`/swagger:/tmp swaggerapi/swagger-ui
```

Once up and running you can simply navigate to `http://localhost:8081` to view your Swagger documenation.
