# Web Services and Applications - Project
This is my project for the module of Web Services and Applications, that demonstrates my understanding and consuming RESTful APIs. It is web application called Inventory which is hosted on www.pythonanywhere.com
Application provides create, update, search, delete functions, along with print function.

## Repository Contents:
inventory_server.py — Main Flask application file with API routes and CRUD logic.\
inventorydao.py — Data access layer (database operations).\
static/ — Static files (CSS, HTML, JS that consume the API)\
requirements.txt — Project dependencies.\
README.md (this file) — Instructions and overview.\

## How app was created:

##  How to Run the App Locally
With command in bash:

1.  Clone this repository:\  
    bash
    ```
    git clone https://github.com/lmacakova/wsaa.project.git
    cd wsaa.project
    ```
2.  Create  and activate an virtual environment:\
    bash
    ```
    python -m venv .venv
    ```
    in Windows:
    ```
    .venv\Scripts\activate
    ```
    or in Mac:
    ```
    source .venv/bin/activate
    ```
3.  Install dependencies:\
    bash
    ```
    pip install -r requirements.txt
    ```
4.  Set environment variables:\
    Create a file named .env in the project root (or set them directly in your shell):\
    bash
    ```
    FLASK_APP=inventory_server.py
    FLASK_ENV=development
    ```
    This tells Flask which script is the app and sets development mode.\
5.   Run the app:\
    bash
    ```
    flask run
    ```
6.  Open your browser and go to http://127.0.0.1:5000 to use the app or test the RESTful API endpoints.    

## 🗃️ Database Setup

This project uses **SQLite** for storage.

- By default, the database file (`inventory.db`) will be created automatically in the project directory the first time you run the app.
- If you want to reset the database, simply delete `inventory.db` and restart the app.
- (Optional) If migrations are enabled with Flask-Migrate, you can run:
  ```bash
  flask db upgrade 


## Resources:

