# JVSK Trac - Full-Stack Product Inventory Management

A full-stack product inventory tracking and management system built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **React**.

---

## 📌 Project Overview & Development Journey

This repository demonstrates the step-by-step development of a complete inventory tracking system, starting from core backend architecture and database integration to seamless frontend connectivity.

---

## 🛠️ Phase 1: Backend Architecture & API Testing (Completed by JVSK)

The foundational backend was constructed using FastAPI and PostgreSQL, focusing on database persistence, schema validation, and CRUD API design.

### 1. Python Virtual Environment (`myenv`)
- Configured an isolated Python virtual environment (`myenv`) to manage dependencies cleanly without conflicts.
- Core packages: `fastapi`, `uvicorn`, `sqlalchemy`, `pydantic`, `psycopg2`.

### 2. PostgreSQL Database Connection (`database.py`)
- Configured PostgreSQL connection using SQLAlchemy `create_engine` with environment variables (`python-dotenv`):
  ```python
  load_dotenv()
  db_url = os.getenv("DATABASE_URL")
  engine = create_engine(db_url)
  SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  Base = declarative_base()
  ```
- Stored sensitive connection strings safely in `.env` (with `.env.example` template provided) to ensure credentials are never exposed on GitHub.
- Handled scoped database sessions using FastAPI's dependency injection (`get_db`) to guarantee connections are cleanly opened and closed per request.

### 3. Database Modeling & Schema Validation
- **Database Model (`database_models.py`)**:
  - Defined the relational table `Product` mapped with SQLAlchemy:
    - `id` (Integer, Primary Key, Indexed)
    - `name` (String)
    - `description` (String)
    - `price` (Float)
    - `quantity` (Integer)
  - Automatic table creation on startup with `Base.metadata.create_all(bind=engine)`.
- **Pydantic Validation (`models.py`)**:
  - Implemented the `Product` data schema inheriting from `BaseModel` for strict request/response data typing and validation.

### 4. RESTful CRUD API Implementation (`main.py`)
Developed complete REST endpoints covering the entire product lifecycle:
- **`GET /`**: Welcome/health-check endpoint.
- **`GET /products`**: Fetches all products stored in the database.
- **`GET /product/{id}`**: Fetches a single product by its ID.
- **`POST /product`**: Adds a new product into the database.
- **`PUT /product?id={id}`**: Updates an existing product's fields in PostgreSQL.
- **`DELETE /product?id={id}`**: Deletes a product from the database.
- **Database Seeding (`init_db`)**: Automatic seeding of initial inventory items on startup if the database is fresh.

### 5. API Testing & Verification
- Performed end-to-end API testing using:
  - FastAPI's interactive Swagger UI documentation at `http://localhost:8000/docs`.
  - Direct HTTP client calls (`curl` / Postman / `Invoke-RestMethod`).
  - Verification of data persistence, schema validation, and transaction commits in PostgreSQL.

---

## 🌐 Phase 2: Frontend Integration & Connectivity

With the backend API fully operational, the React frontend was connected to bridge the user interface with the backend services.

### 1. Seamless Communication via Proxy
- Connected the React development server to the FastAPI backend running in `myenv` using the `"proxy": "http://localhost:8000"` configuration in `frontend/package.json`.
- Eliminates browser CORS (Cross-Origin Resource Sharing) restrictions without needing backend middleware alterations.

### 2. Endpoint Alignment in Frontend (`App.js`)
- Standardized API requests to match the backend parameter specifications:
  - `GET /products` for real-time inventory listing.
  - `POST /product` with JSON payload for adding items.
  - `PUT /product?id={id}` with query parameter and payload for updating records.
  - `DELETE /product?id={id}` for removing items.
- Added live search, column sorting, and smooth form reset flows.

### 3. Custom Branding
- Branded the application as **JVSK Trac** across the interface, browser title, metadata, and badges.

---

## 📁 Repository Structure

```text
fastapi-practice/
├── database.py             # PostgreSQL connection and SQLAlchemy SessionLocal setup
├── database_models.py      # SQLAlchemy ORM database models
├── models.py               # Pydantic schemas for data validation
├── main.py                 # FastAPI app, route handlers, and CRUD endpoints
├── myenv/                  # Python virtual environment
├── README.md               # Project documentation
└── frontend/               # React UI
    ├── package.json        # Dependencies & proxy configuration to localhost:8000
    ├── public/
    │   └── index.html      # HTML entry point with JVSK Trac branding
    └── src/
        ├── App.js          # Core React component with API calls & inventory table
        ├── App.css         # Styling for inventory table, forms, and layout
        ├── TaglineSection.js  # JVSK branding and tagline component
        └── index.js        # React DOM render entry point
```

---

## 🚀 How to Run the Application

### Prerequisites
- Python 3.10+
- Node.js 16+ & npm
- PostgreSQL running locally with database `fastAPI`

### Step 1: Run the Backend (FastAPI)
1. Open a terminal in the root folder (`fastapi-practice`).
2. Activate your virtual environment:
   - **Windows (PowerShell)**:
     ```powershell
     .\myenv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     source myenv/bin/activate
     ```
3. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
4. The backend will be live at:
   - API: `http://localhost:8000`
   - Interactive Swagger Docs: `http://localhost:8000/docs`

### Step 2: Run the Frontend (React)
1. Open a second terminal window and navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Start the development server:
   ```bash
   npm start
   ```
3. Open `http://localhost:3000` in your browser. All inventory updates will sync with your PostgreSQL database in real time!

---

## 📊 API Reference Summary

| Method | Endpoint | Query / Path Params | Request Body | Description |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | None | None | Root health check |
| `GET` | `/products` | None | None | Fetch all products |
| `GET` | `/product/{id}` | `id` (path) | None | Fetch single product |
| `POST` | `/product` | None | `Product` JSON | Create product |
| `PUT` | `/product` | `id` (query) | `Product` JSON | Update product by ID |
| `DELETE` | `/product` | `id` (query) | None | Delete product by ID |
