# ShopCart

A modern full-stack e-commerce application built with **React, FastAPI, PostgreSQL, and JWT authentication**.

ShopCart demonstrates end-to-end full-stack development with a clean separation between frontend and backend services. The project includes secure authentication, product management, shopping cart functionality, order management, REST API development, and relational database integration.

---

## Tech Stack

### Frontend

* React
* Vite
* JavaScript
* HTML5
* CSS3
* REST API Integration

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication
* OAuth2
* Pydantic
* Uvicorn

### Development Tools

* Git
* GitHub
* uv
* npm
* Swagger / OpenAPI
* pgAdmin
* Postman

---

## Key Features

* User registration and login
* JWT-based authentication
* Protected API endpoints
* User management
* Product management
* Product category management
* Shopping cart functionality
* Order creation and management
* PostgreSQL database integration
* RESTful API architecture
* Frontend and backend integration
* CORS configuration
* Automatic API documentation with Swagger

---

## Application Architecture

```text
React Frontend
      |
      | REST API
      v
FastAPI Backend
      |
      v
SQLAlchemy ORM
      |
      v
PostgreSQL Database
```

ShopCart follows a modular full-stack architecture where the React frontend communicates with the FastAPI backend through REST APIs.

The backend handles business logic, authentication, authorization, and database operations using SQLAlchemy and PostgreSQL.

---

## Authentication Flow

ShopCart uses JWT-based authentication for securing protected resources.

```text
User Login
    |
    v
Credentials Validation
    |
    v
JWT Access Token
    |
    v
Authenticated Request
    |
    v
Protected FastAPI Endpoint
```

After successful authentication, the backend generates an access token that is used to authorize protected API requests.

---

## Core Modules

### Authentication

The authentication module manages user registration, login, password validation, and JWT token generation.

### Users

The user module manages user-related information and authenticated user operations.

### Products

The product module provides functionality for managing products including:

* Creating products
* Retrieving products
* Updating products
* Deleting products

### Categories

Products can be organized into categories to improve product management and browsing.

### Shopping Cart

Authenticated users can manage products in their shopping cart.

Core cart functionality includes:

* Add products to cart
* View cart items
* Update cart items
* Remove products from cart

### Orders

The order module handles order creation and order management for authenticated users.

---

## Project Structure

```text
fastapi-react-ecommerce/
│
├── backend/
│   │
│   └── app/
│       │
│       ├── routers/
│       │   ├── auth.py
│       │   ├── users.py
│       │   ├── products.py
│       │   ├── categories.py
│       │   ├── cart.py
│       │   └── orders.py
│       │
│       ├── database.py
│       ├── models.py
│       └── main.py
│
├── frontend/
│   │
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       ├── App.jsx
│       └── main.jsx
│
├── .gitignore
└── README.md
```

The project structure separates responsibilities across different modules, helping keep the codebase maintainable and scalable.

---

## Backend Architecture

The FastAPI backend follows a modular router-based architecture.

Major backend modules include:

```text
Authentication
Users
Products
Categories
Cart
Orders
```

Each module is responsible for handling a specific part of the application.

This architecture helps improve:

* Code organization
* Maintainability
* Reusability
* Scalability
* Separation of concerns

---

## Database

ShopCart uses **PostgreSQL** as its relational database.

SQLAlchemy is used as the Object Relational Mapper between the FastAPI application and PostgreSQL.

```text
FastAPI
   |
   v
SQLAlchemy
   |
   v
PostgreSQL
```

The database stores application data such as:

* Users
* Products
* Categories
* Cart items
* Orders

---

## REST API

The backend exposes RESTful API endpoints for application operations.

The API follows standard HTTP methods including:

```text
GET
POST
PUT
DELETE
```

These APIs allow the React frontend to communicate with the backend and perform CRUD operations.

---

## API Documentation

FastAPI automatically generates interactive API documentation using OpenAPI.

The API can be explored and tested through:

### Swagger UI

```text
/docs
```

### ReDoc

```text
/redoc
```

Swagger provides an interactive interface for testing API endpoints directly from the browser.

---

## Security

ShopCart implements common authentication and application security practices.

These include:

* Password hashing
* JWT authentication
* OAuth2-based authentication flow
* Protected API endpoints
* Authentication dependencies
* Environment-based configuration
* CORS configuration
* Separation of frontend and backend responsibilities

Sensitive application credentials are not stored directly in the source code.

This project demonstrates practical experience with:

* Full-stack application development
* React application development
* FastAPI backend development
* REST API design
* CRUD operations
* Authentication and authorization
* JWT token-based security
* OAuth2 authentication
* Relational database design
* PostgreSQL
* SQLAlchemy ORM
* Pydantic data validation
* Dependency injection
* Modular backend architecture
* React and API integration
* Client-server architecture
* CORS configuration
* Git version control
* Environment-based configuration

---

## Frontend

The frontend is developed using React and Vite.

It communicates with the FastAPI backend through REST APIs and provides the user interface for the e-commerce application.

The frontend is responsible for:

* User interaction
* Authentication flow
* Product display
* Product browsing
* Shopping cart interaction
* Order interaction
* API communication
* Application navigation

---

## Backend

The backend is developed using FastAPI and Python.

It is responsible for:

* Authentication
* Authorization
* Business logic
* API endpoints
* Data validation
* Database operations
* User management
* Product management
* Category management
* Cart management
* Order management

---

## Why FastAPI?

FastAPI provides a modern approach to building Python APIs with strong support for:

* Type validation
* Dependency injection
* Async request handling
* Automatic API documentation
* Pydantic validation
* High-performance API development

It provides a clean and maintainable backend architecture for full-stack applications.

---

## Why PostgreSQL?

PostgreSQL provides a reliable relational database solution for managing structured application data.

It is well suited for handling relationships between:

```text
Users
  |
  ├── Cart
  |
  └── Orders

Categories
  |
  └── Products
```

Using PostgreSQL with SQLAlchemy provides both database reliability and maintainable application-level data access.

---

## Development Goals

ShopCart was built to demonstrate practical full-stack engineering skills by developing a complete application instead of isolated frontend or backend features.

The project focuses on:

* Building scalable REST APIs
* Implementing secure authentication
* Designing relational database models
* Integrating React with FastAPI
* Managing application state and API communication
* Organizing backend functionality into modular routers
* Building maintainable full-stack architecture

---

## Future Improvements

Planned enhancements include:

* Product search
* Product filtering
* Product sorting
* Pagination
* Product images
* Product reviews
* Product ratings
* User profile management
* Admin dashboard
* Role-based authorization
* Inventory management
* Payment integration
* Checkout workflow
* Order status tracking
* Automated testing
* Docker containerization
* CI/CD pipeline
* Cloud deployment
* Logging and monitoring
* Improved error handling

---

## Deployment

The application architecture allows the frontend, backend, and database to be deployed independently.

```text
React Frontend
      |
      v
Cloud Hosting
      |
      | HTTPS / REST API
      v
FastAPI Backend
      |
      v
Managed PostgreSQL Database
```

This separation provides flexibility for deploying different parts of the application using suitable cloud services.

---

## Project Highlights

ShopCart demonstrates the implementation of a complete e-commerce workflow using modern full-stack technologies.

Key technical highlights include:

* React frontend
* FastAPI REST API
* PostgreSQL relational database
* SQLAlchemy ORM
* JWT authentication
* OAuth2 authentication flow
* Protected backend routes
* Modular router architecture
* CRUD operations
* Frontend/backend API integration
* Automatic OpenAPI documentation

---

## Project Purpose

ShopCart is a portfolio project created to demonstrate real-world full-stack software development concepts.

Rather than focusing only on basic CRUD functionality, the project combines authentication, authorization, relational data modeling, modular API development, and frontend/backend integration within a single application.

---

## Author

**Navjot Singh**

Full-Stack Software Developer

### Technologies

`React` · `Vite` · `FastAPI` · `Python` · `PostgreSQL` · `SQLAlchemy` · `JWT` · `OAuth2` · `REST APIs`

---

## Repository

**ShopCart — Full-Stack E-Commerce Application**

Built with React, FastAPI, PostgreSQL, JWT authentication, and REST APIs.
