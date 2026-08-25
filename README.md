# Customer Management API

A RESTful Customer Management API built with **Django**, **Django REST Framework**, **MySQL**, **JWT Authentication**, and **OpenAPI/Swagger documentation**.

This project was built as a backend development project to practice REST API development, database integration, authentication, authorization, validation, testing, and API documentation.

## 🚀 Features

* Django project and application setup
* MySQL database integration
* Customer model
* Django Admin
* Django REST Framework
* Customer serializer
* CRUD operations
* Data validation
* Email validation
* JWT authentication
* JWT refresh tokens
* Custom permissions
* Staff/Admin authorization
* Automated API tests
* OpenAPI schema
* Swagger API documentation
* Git and GitHub workflow

## 🛠️ Technologies

* Python
* Django
* Django REST Framework
* MySQL
* Simple JWT
* drf-spectacular
* Swagger / OpenAPI
* Postman
* Git
* GitHub

## 📁 Project Structure

```text
Customer-Management-API/
│
├── customers/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permission.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Irshadwev/Customer-Management-API.git
```

Move into the project:

```bash
cd Customer-Management-API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Git Bash

```bash
source venv/Scripts/activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🗄️ MySQL Configuration

Create a MySQL database:

```sql
CREATE DATABASE customer_management;
```

Configure the database in `system/settings.py`.

Example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "customer_management",
        "USER": "your_mysql_username",
        "PASSWORD": "your_mysql_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

> Keep your real database credentials and Django secret key out of GitHub. Use environment variables for sensitive configuration.

## 🔄 Database Migrations

Run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

## 👤 Create a Superuser

Create an administrator account:

```bash
python manage.py createsuperuser
```

Follow the instructions shown in the terminal.

## ▶️ Run the Development Server

```bash
python manage.py runserver
```

The development server will normally be available at:

```text
http://127.0.0.1:8000/
```

## 🔐 Authentication

The API uses **JWT (JSON Web Token)** authentication.

JWT provides:

* Access token
* Refresh token
* Token-based authentication for protected endpoints

### Obtain Access and Refresh Tokens

Endpoint:

```text
POST /api/token/
```

Example request:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Example response:

```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

### Refresh Access Token

Endpoint:

```text
POST /api/token/refresh/
```

Example request:

```json
{
    "refresh": "your_refresh_token"
}
```

### Use the Access Token

For protected API requests, include:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## 🛡️ Permissions

The project uses custom permission handling.

### Authenticated users

Authenticated users can access permitted read operations.

### Staff / Admin users

Staff users have permission to perform customer management operations such as:

* Create
* Update
* Partial update
* Delete

Unauthenticated users cannot access protected customer endpoints.

## 📡 Customer API

The customer routes are provided through the `customers` application.

### Get All Customers

```text
GET /customers/
```

### Get Customer by ID

```text
GET /customers/<customer_id>/
```

Example:

```text
GET /customers/1/
```

### Create Customer

```text
POST /customers/
```

Example request:

```json
{
    "name": "Ali Khan",
    "email": "ali@example.com",
    "phone": "03001234567",
    "city": "Lahore"
}
```

### Update Customer

```text
PUT /customers/<customer_id>/
```

Example:

```text
PUT /customers/1/
```

### Partial Update Customer

```text
PATCH /customers/<customer_id>/
```

Example:

```text
PATCH /customers/1/
```

Example request:

```json
{
    "city": "Multan"
}
```

### Delete Customer

```text
DELETE /customers/<customer_id>/
```

Example:

```text
DELETE /customers/1/
```

A successful deletion returns:

```text
204 No Content
```

## ✅ Validation

Customer data is validated through the serializer before being saved.

Validation includes:

* Required fields
* Valid email format
* Customer data validation
* Duplicate email validation

Example invalid email:

```json
{
    "email": "invalid-email"
}
```

The API returns a validation error instead of creating an invalid customer record.

## 📚 API Documentation

The project uses **drf-spectacular** to provide OpenAPI documentation and Swagger UI.

### OpenAPI Schema

```text
GET /api/schema/
```

### Swagger UI

```text
GET /api/docs/
```

Open Swagger UI in your browser:

```text
http://127.0.0.1:8000/api/docs/
```

Swagger allows you to explore and test the available API endpoints.

## 🧪 Testing

Automated tests are included in the `customers/tests.py` file.

Run the test suite with:

```bash
python manage.py test
```

The tests cover important API behavior such as:

* Customer API operations
* Authentication
* Permissions
* Unauthorized requests
* Forbidden requests
* Validation
* CRUD functionality

## 📊 HTTP Status Codes

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | OK                    |
| 201         | Created               |
| 204         | No Content            |
| 400         | Bad Request           |
| 401         | Unauthorized          |
| 403         | Forbidden             |
| 404         | Not Found             |
| 500         | Internal Server Error |

## 🔒 Security

The following files and values should not be committed to GitHub:

* `.env`
* Database passwords
* Secret keys
* Local virtual environment
* Python cache files

The project's `.gitignore` should be used to prevent sensitive and unnecessary files from being committed.

## 🔧 Git Workflow

Development work is performed on the `working` branch rather than directly on `main`.

Typical workflow:

```bash
git checkout working
```

Make changes and stage them:

```bash
git add .
```

Commit:

```bash
git commit -m "Your commit message"
```

Push the development branch:

```bash
git push origin working
```

Then create a Pull Request:

```text
working → main
```

After the Pull Request is reviewed and merged, update the local `main` branch:

```bash
git checkout main
git pull origin main
```

## 🎯 Project Goals

This project demonstrates practical backend development concepts:

* Django fundamentals
* REST API development
* Django REST Framework
* CRUD operations
* Serialization
* Validation
* MySQL database integration
* Authentication
* JWT
* Authorization
* Custom permissions
* API testing
* OpenAPI documentation
* Swagger
* Git and GitHub workflow

## 📌 Project Status

The project has completed the core Customer Management API implementation.

## 👨‍💻 Author

**Irshad Ahmed**

Backend Developer

GitHub:

https://github.com/Irshadwev

## 📄 License

This project was created for learning and backend development practice.
