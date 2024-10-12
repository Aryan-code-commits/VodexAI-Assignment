# VodexAI Assignment - FastAPI CRUD Application

This project is a FastAPI-based CRUD application using MongoDB for database operations. It includes CRUD endpoints, MongoDB aggregation, and filtering, and is documented with FastAPI's integrated Swagger UI.

## Features
- MongoDB for database
- CRUD operations for items
- Filtering and aggregation using MongoDB
- FastAPI Swagger Documentation

## Setup and Run Locally

### Prerequisites
- Python 3.8+
- MongoDB server (local or cloud)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aryan-code-commits/VodexAI-Assignment.git
   cd VodexAI-Assignment
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # For Linux/macOS
   .venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure MongoDB connection in the `src/vodex/database.py` file. If you use a MongoDB URI, update it accordingly.

5. Run the application:
   ```bash
   run-vodex
   ```

6. Visit the API documentation at:
   - `http://127.0.0.1:8000/docs`

## API Endpoints

### Root
- `GET /`: Returns a welcome message.

### Items
- `GET /items/`: Get a list of items.
- `POST /items/`: Create a new item.
- `PUT /items/{item_id}`: Update an item by ID.
- `DELETE /items/{item_id}`: Delete an item by ID.

## MongoDB Filters and Aggregation
- Example usage of MongoDB aggregation pipelines and query filters.

## Deployment
The app is deployed on [Your Hosting Service]. You can access the live Swagger documentation [here](#).