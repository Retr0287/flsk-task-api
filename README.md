# Flask Task API

A backend REST API built with Flask and MySQL.

This project was created as a learning backend application focused on authentication, JWT authorization, CRUD operations, and project structure organization.

## Features 
- User registration with password hashing (bcrypt) 
- User authentication with JWT tokens 
- Protected routes using custom login_required decorator 
- Create tasks 
- View user tasks 
- Update tasks 
- Delete tasks 
- Request validation and input cleaning 
- Service layer architecture 
- Custom API exceptions 
- Centralized error handling 
- Application logging 
- MySQL database integration 
- Environment variables support (.env)

---

# Technologies

- Python
- Flask
- MySQL
- JWT (PyJWT)
- bcrypt
- dotenv

---

## Project Architecture

The project follows a layered architecture approach:

### Routes Layer
Handles HTTP requests and responses.

Responsibilities:
- Receive requests
- Validate input
- Call service functions
- Return JSON responses

Files:
- routes/auth_routes.py
- routes/task_routes.py

### Service Layer
Contains business logic and database operations.

Responsibilities:
- Create tasks
- Update tasks
- Delete tasks
- Fetch tasks
- Check task ownership

Files:
- services/task_service.py

### Validation Layer
Contains reusable validation functions.

Responsibilities:
- Validate task data
- Clean request input
- Prevent invalid data from reaching business logic

Files:
- utils/validators.py

### Authentication Layer
Handles JWT authentication.

Responsibilities:
- Verify tokens
- Extract user_id from JWT
- Protect private routes

Files:
- auth.py

### Exception Layer
Contains custom exceptions and centralized error handling.

Responsibilities:
- Raise meaningful API errors
- Handle errors consistently

Files:
- exceptions/api_exceptions.py

### Database Layer
Provides database connection and cursor management.

Files:
- db.py

### Configuration Layer
Stores application settings and environment variables.

Files:
- config.py

### Logging Layer
Handles application logging.

Files:
- utils/logger.py

---

# API Endpoints

## Authentication

### Register

```http
POST /register
```

Body:

```json
{
  "username": "test",
  "password": "123456"
}
```

---

### Login

```http
POST /login
```

Returns JWT token.

---

# Tasks

## Create Task

```http
POST /tasks
```

Headers:

```http
Authorization: YOUR_TOKEN
```

Body:

```json
{
  "title": "Learn Flask"
}
```

---

## Get Tasks

```http
GET /tasks
```

---

## Update Task

```http
PATCH /tasks/<task_id>
```

---

## Delete Task

```http
DELETE /task/<task_id>
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/Retr0287/flask-task-api.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
SECRET_KEY=your_secret_key
```

Configure MySQL database in `db.py`.

Run server:

```bash
python app.py
```

---

# Goals Of This Project

This project was built to practice:

- Backend development fundamentals
- REST API architecture
- Authentication systems
- Flask project organization
- Database interaction
- Writing cleaner and reusable code

---

# Future Improvements

- Refresh tokens
- SQLAlchemy migration
- Docker support
- Unit testing
- Pagination
- Task categories
- User roles
- Deployment

---

# Author

GitHub:
https://github.com/Retr0287