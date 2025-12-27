# Backend API

A simple Flask REST API for managing contacts.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the server:**
    ```bash
    python main.py
    ```
    The server will start at `http://127.0.0.1:5000`.

## API Documentation

### Contacts

| Method | Endpoint | Description | Request Body |
| :--- | :--- | :--- | :--- |
| `GET` | `/contacts/` | Get all contacts | N/A |
| `GET` | `/contacts/<id>/` | Get a single contact | N/A |
| `POST` | `/contacts/` | Create a new contact | `{"firstName": "...", "lastName": "...", "email": "..."}` |
| `PATCH` | `/update_contact/<id>/` | Update a contact | `{"firstName": "...", "lastName": "...", "email": "..."}` (Partial updates allowed) |
| `DELETE` | `/delete_contact/<id>/` | Delete a contact | N/A |

### Data Models -> 

**Contact**
*   `id`: Integer (Primary Key)
*   `firstName`: String
*   `lastName`: String
*   `email`: String (Unique)
