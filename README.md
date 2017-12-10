# featureRequestsApp

## Env: 

OS Ubuntu

Python 2.7.12


## Installation Steps:

• On terminal run below command

• sudo apt-get update && sudo apt-get -y upgrade • sudo apt-get install python-pip

• pip install -r requirements.txt

• python app.py

## API Feature -

• Pagination - If List API has more that 30 object, the JSON will automatically put the page urls
in link hash.

- "links": {"first": "/clients", "last": "/clients?page%5Bnumber%5D=2", "prev": "/clients?page%5Bnumber%5D=1", "self": "/clients?page%5Bnumber%5D=2" },

• Sorting - One can sort the response using -

- http://127.0.0.1:5000/clients?sort=name 

- http://127.0.0.1:5000/clients?sort=-name

- Search - One can search by -

- GET /clients?filter=[{“name”:”field_name”,”op":"operator","val":"field_value”}] 

- GET /clients?filter=[{“name”:"name","op":"eq","val":"Client B”}]

- Common available operators:

- any: used to filter on to many relationships

- between: used to filter a field between two values

- endswith: check if field ends with a string

- eq: check if field is equal to something

- ge: check if field is greater than or equal to something

- gt: check if field is greater than to something

- has: used to filter on to one relationships

- ilike: check if field contains a string (case insensitive)

- in_: check if field is in a list of values

- is_: check if field is a value

- isnot: check if field is not a value

- like: check if field contains a string

- le: check if field is less than or equal to something

- lt: check if field is less than to something

- match: check if field match against a string or pattern

- ne: check if field is not equal to something

- notilike: check if field does not contains a string (case insensitive)

- notin_: check if field is not in a list of values

- notlike: check if field does not contains a string

- startswith: check if field starts with a string
    
## ALL APIS:
 
## Clients:

GET: http://127.0.0.1:5000/clients/1

{
"data": {
"attributes": {
"name": "Client A" },
"id": "1", "links": {
"self": "/clients/1" },
"type": "client" },
"jsonapi": {
"version": "1.0" },
"links": {
"self": "/clients/1" }
}

LIST: http://127.0.0.1:5000/clients

{
"data": [
{
"attributes": {
"name": "Client A" },
"id": "1", "links": {
"self": "/clients/1" },
"type": "client" },
{
"attributes": {
"name": "Client B" },
"id": "2", "links": {
"self": "/clients/2" },
"type": "client" }
], "jsonapi": {
"version": "1.0" },
"links": {
"first": "/clients",
"last": "/clients?page%5Bnumber%5D=2", "prev": "/clients?page%5Bnumber%5D=1", "self": "/clients?page%5Bnumber%5D=2"
}, "meta": {
    "count": 2

 } }
 
PATCH: http://127.0.0.1:5000/clients/1

{
"data": {
"type": "client", "id": "1", "attributes": {
"name": "Client C" }
} }

POST: http://127.0.0.1:5000/clients

{
"data": {
"type": "client", "attributes": {
"name": "Client B" }
} }
 
 ## Priority:
 
GET: http://127.0.0.1:5000/priorities/1

{
"data": {
"attributes": {
"priority": 12 },
"id": "1", "links": {
"self": "/priorities/1" },
"type": "priority" },
"jsonapi": {
"version": "1.0" },
"links": {
"self": "/priorities/1" }
}

LIST: http://127.0.0.1:5000/priorities

{
"data": [
{
"attributes": {
"priority": 12 },
"id": "1", "links": {
"self": "/priorities/1" },
"type": "priority" },
{
"attributes": {
"priority": 12 },
"id": "2", "links": {
"self": "/priorities/2" },
"type": "priority" }
], "jsonapi": {
"version": "1.0" },
"links": {
"self": "/priorities" },
"meta": {
"count": 2 }
}
 
 
 PATCH: http://127.0.0.1:5000/priorities/1
 
{
"data": {
"type": "priority", "id": "1", "attributes": {
"priority": "12" }
} }

POST: http://127.0.0.1:5000/priorities

{
"data": {
"type": "priority", "attributes": {
"priority": "1" }
} }

 ## Product Area:
 
GET: http://127.0.0.1:5000/product_areas/1

{
"jsonapi": {
"version": "1.0" },
"links": {
"self": "/product_areas/1" }
}

LIST: http://127.0.0.1:5000/product_areas

{
"data": [
{
"attributes": {
"name": "Policies" },
"id": "1", "links": {
"self": "/product_areas/1" },
"type": "product_area" },
{
"attributes": {
"name": "Billing" },
"id": "2", "links": {
"self": "/product_areas/2" },
"type": "product_area" }
], "jsonapi": {
"version": "1.0" },
"links": {
"self": "/product_areas" },
"meta": {
"count": 2 }
}
 "data": { "attributes": {
"name": "Policies" },
"id": "1", "links": {
"self": "/product_areas/1" },
"type": "product_area" },

 PATCH: http://127.0.0.1:5000/product_areas/3
 
{
"data": {
"type": "product_area", "id": "3",
"attributes": {
"name": "Billings" }
} }

POST: http://127.0.0.1:5000/product_areas

{
"data": {
"type": "product_area", "attributes": {
"name": "Billing" }
} }

 ## Feature Request:
 
GET: http://127.0.0.1:5000/feature_requests/1

{
"data": {
"attributes": {
"description": "Testing1...", "target_date": "1990-12-18", "title": "Test1"
},
"id": "1", "links": {
"self": "/feature_requests/1" },
"relationships": { "client": {
"links": {
"self": "/clients/1" }
}, "client_priority": {
"links": {
"self": "/priorities/1" }
}, "product_area": {
"links": {
"self": "/product_areas/1" }
} },
"type": "feature_request" },
"jsonapi": {
"version": "1.0" },
"links": {
"self": "/feature_requests/1" }
}

LIST: http://127.0.0.1:5000/feature_requests

{
"data": [
{
"attributes": {
"description": "Testing1...", "target_date": "1990-12-18", "title": "Test1"
},
"id": "1", "links": {
"self": "/feature_requests/1" },
"relationships": { "client": {
"links": {
"self": "/clients/1" }
 
 }, "client_priority": {
"links": {
"self": "/priorities/1" }
}, "product_area": {
"links": {
"self": "/product_areas/1" }
} },
"type": "feature_request" },
{
"attributes": {
"description": "Testing1...", "target_date": "1990-12-18", "title": "Test1"
},
"id": "2", "links": {
"self": "/feature_requests/2" },
"relationships": { "client": {
"links": {
"self": "/clients/2" }
}, "client_priority": {
"links": {
"self": "/priorities/2" }
}, "product_area": {
"links": {
"self": "/product_areas/2" }
} },
"type": "feature_request" }
], "jsonapi": {
"version": "1.0" },
"links": {
"self": "/feature_requests" },
"meta": {
"count": 2 }
}

PATCH: http://127.0.0.1:5000/feature_requests/1

{
"data": {
"type": "feature_request", "id": "1",
"attributes": {
"title": "Test1Patch", "description": "Testing1...", "target_date": "1990-12-18"
}, "relationships": {
"client": { "data": {
"type": "client",
"id": 1 }
}, "client_priority": {
"data": {
"type": "priority",
"id": 1 }
}, "product_area": {
"data": {
"type": "product_area",
"id": 1 }
} }
} }

POST: http://127.0.0.1:5000/feature_requests

{
"data": {
"type": "feature_request", "attributes": {
"title": "Test",
"description": "Testing...", "target_date": "1990-12-18"
}, "relationships": {
"client": { "data": {
"type": "client",
"id": 1 }
}, "client_priority": {
"data": {
"type": "priority",
"id": 1 }
}, "product_area": {
"data": {
"type": "product_area",
"id": 1 }
 
} }
} }

