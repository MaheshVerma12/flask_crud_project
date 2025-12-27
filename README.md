This is a React JS frontend and Flask backend full stack project. This project was done by following tutorials from "Tech With Tim" YouTube channel, although I myself have typed out the backend codes
by understanding what is happening. The link of the YouTube video of this project is -> "https://www.youtube.com/watch?v=PppslXOR7TA&t=2664s". 
The project has a contact model with fields id, first_name, last_name and email and has Flask create, read, update and delete (CRUD) endpoints for the model. The description of the backend 
is given below. 
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
