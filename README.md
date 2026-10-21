# FastAPI Employee Management API

A RESTful Employee Management API built with **FastAPI, Python, MySQL, SQLAlchemy, and Alembic**. This project follows a layered architecture inspired by Laravel, separating routes, controllers, services, models, and schemas.

## Features

- Employee CRUD operations (Create, Read, Update, Delete)
- RESTful API endpoints
- Request validation using Pydantic
- MySQL database integration
- SQLAlchemy ORM for database operations
- Alembic for database migrations
- Environment-based configuration using `.env`
- Separate routes, controllers, services, models, and schemas
- Automatic API documentation with Swagger UI
- Database session management using FastAPI dependencies

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Validation:** Pydantic
- **Database Driver:** PyMySQL
- **Environment Variables:** python-dotenv

## Project Structure

```text
fastapi_learning/
├── alembic/
│   ├── versions/
│   └── env.py
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── employee.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── employee.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── employee_routes.py
│   ├── controllers/
│   │   └── employee_controller.py
│   └── services/
│       └── employee_service.py
├── .env.example
├── .gitignore
├── alembic.ini
├── main.py
└── README.md
```

## Architecture

The application separates responsibilities into different layers:

- **Routes:** Define API endpoints and HTTP methods.
- **Controllers:** Handle endpoint-level request and response coordination.
- **Services:** Contain business logic and database operations.
- **Models:** Define database tables using SQLAlchemy.
- **Schemas:** Validate incoming request data and structure API responses.
- **Database:** Configure the database engine, sessions, and shared SQLAlchemy base.
- **Alembic:** Manages database schema migrations.

## Getting Started

### 1. Clone the repository

```bash
git clone <git@github.com:Yeasinarafatshuvo/fast_api_crud_apps.git>
cd fastapi_learning
```

Replace the placeholder with your GitHub repository URL.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install "fastapi[standard]" sqlalchemy pymysql python-dotenv alembic email-validator
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```dotenv
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fastapi_learning
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

Replace the values with your local MySQL configuration.

**Security:** Never commit your actual `.env` file or database credentials to GitHub.

### 5. Create the MySQL database

Log in to MySQL and create the database:

```sql
CREATE DATABASE fastapi_learning;
```

Configure the database user and permissions according to your local MySQL setup.

### 6. Run database migrations

Apply the existing Alembic migrations:

```bash
alembic upgrade head
```

This applies the database schema defined by the project's migration files.

### 7. Start the development server

```bash
uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Use Swagger UI to inspect and test the API endpoints.

## API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome endpoint |
| GET | `/about` | Application information |
| POST | `/employees/` | Create an employee |
| GET | `/employees/` | Retrieve all employees |
| GET | `/employees/{employee_id}` | Retrieve an employee by ID |
| PUT | `/employees/{employee_id}` | Update an employee |
| DELETE | `/employees/{employee_id}` | Delete an employee |

### Example: Create an Employee

**Request**

```http
POST /employees/
Content-Type: application/json
```

**JSON body**

```json
{
  "name": "Yeasin Arafat",
  "email": "yeasin@example.com",
  "salary": 89000
}
```

The email must be valid, the name must satisfy the configured length constraints, and the salary must be greater than zero.

## Database Migrations

Create a new migration after modifying SQLAlchemy models:

```bash
alembic revision --autogenerate -m "describe your changes"
```

Review the generated migration before applying it:

```bash
alembic upgrade head
```

Keep migration files under version control so other developers can reproduce the schema.

## Development Goals

This project is being developed incrementally as part of a practical journey toward professional backend engineering with Python and FastAPI.

Planned improvements may include:

- Centralized exception handling
- Pagination, search, and filtering
- Automated API testing with pytest
- JWT authentication and authorization
- Role-based access control
- Logging and production configuration
- Docker and deployment

## License

No license has been specified yet.
