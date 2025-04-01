# A Potato Server

This is a simple server that allows you to create and get potatoes.


## Run the app

```bash
docker build -t potato-api .
docker run -d -p 8000:8000 potato-api
```

## Test the app

### Create a potato

```bash
curl -X POST http://localhost:8000/api/v1/potatoes -H "Content-Type: application/json" -d '{"id": "1", "name": "Potato 1", "weight": 100}'
```

Expected output:

```json
{"id": "1", "name": "Potato 1", "weight": 100}
```

### Get a potato    

```bash
curl -X GET http://localhost:8000/api/v1/potatoes/1
```

Expected output:

```json
{"id": "1", "name": "Potato 1", "weight": 100}
```

### Get a potato that doesn't exist

```bash
curl -X GET http://localhost:8000/api/v1/potatoes/2
```

Expected output:


```
HTTP 404 Not Found

{"detail":"Potato not found"}
```
