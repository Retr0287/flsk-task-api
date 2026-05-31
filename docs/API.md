POST /register

Request:
{
  "username": "john",
  "password": "123456"
}

Response:
{
  "message": "user created"
}

POST /login

Request:
{
  "username": "john",
  "password": "123456"
}

Response:
{
  "token": "jwt_token"
}

POST /tasks

Headers:
Authorization: jwt_token

Request:
{
  "title": "Learn Flask"
}

Response:
{
  "message": "task created"
}

GET /tasks

Headers:
Authorization: jwt_token

PATCH /tasks/<id>

Headers:
Authorization: jwt_token

Request:
{
  "title": "New title"
}

DELETE /task/<id>

Headers:
Authorization: jwt_token

## Error Responses

{
    "error": "title required"
}

{
    "error": "invalid token"
}

{
    "error": "access denied"
}

{
    "error": "task not found"
}