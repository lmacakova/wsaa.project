![The shelves with pottery](https://images.pexels.com/photos/3094041/pexels-photo-3094041.jpeg)
# Web Services and Applications - Inventory App
This is my project for the module of Web Services and Applications, which demonstrates a RESTful API. It is a Flask [^1] web application called Inventory Management. The application provides create, update, search, and delete functions, along with a print function.

## Repository Contents:
inventory_server.py — Main Flask application file with API routes and CRUD logic.\
inventorydao.py — Data access layer (database operations).\
templates/ - containing HTML page for application, inventory.html\
static/ — containing style.css for HTML page\
requirements.txt — Project dependencies.\
README.md (this file) — Instructions and overview.\

##  How to Run the App Locally
With command in bash:

1. Clone this repository:\  
 bash
 ```
 git clone https://github.com/lmacakova/wsaa.project.git
 cd wsaa.project
 ```

2. Create and activate a virtual environment:\
 bash
 ```
 python -m venv .venv
 ```
 In Windows:
 ```
 .venv\Scripts\activate
 ```
 Or in Mac:
 ```
 source .venv/bin/activate
 ```

3. Install dependencies:\
 bash
 ```
 pip install -r requirements.txt
 ```

4. Set environment variables:\
 Create a file named .env in the project root (or set them directly in the shell):\
 bash
 ```
 FLASK_APP=inventory_server.py
 FLASK_ENV=development
 ```
    
5. Database Setup:\
 This project uses the MySQL server

a.  Open phpMyAdmin.
b.  Create a database (e.g., inventory).
c.  Update database connection settings in inventorydao.py with:\
 -   Database name
 -   Username (default: root)
 -   Password (if set)
 -   Host (usually localhost)

6. Open a browser and go to http://127.0.0.1:5000 to use the app.\
 Run the app:\
 bash
 ```
 flask run
 ```
7. Create a database of any products you want.

## Methodics:
First, I created a database inventory, locally on my machine, with a table product and parameters: Name, description, quantity, category, price, and supplier. Then, I made a data access object file[^2] (inventorydao.py), which connects the database with the server file (inventory_server.py) and handles SQL queries with methods (or functions) for search, fetch, add, update, and delete products.  The inventory_server.py, which I made, is the main entry point of the web application. The file contains the code that creates the web server, defines routes, and connects everything together. Database, DAO, and server file create the back-end[^3] of the application. The back-end is the behind-the-scenes part of a web application. It is everything that happens on the server side — things users don't see directly in their browsers. The front-end is the part of a web application that users see and interact with directly in their browsers. An HTML file (in my case, inventory.html in the folder templates) contains the hypertext markup code[^4] that defines the structure and content of a web page or application visible to users. Document object model (DOM)[^5] of the web application/page is constructed as a tree of objects. The DOM turns every element (tags, text, attributes) into an object that can be accessed and modified by code (JavaScript, jQuery, AJAX calls). For my application, I decided to create a DOM structure where, in the background, there is a main table divided into blocks by functions - header, buttons, formulas, and product list. The style of the application is defined by the style.css file in the static folder. CSS[^6] means cascade style sheet - in which elements of the DOM are styled. 


## Resources: 
[^1]:   https://flask.palletsprojects.com/en/stable/
[^2]:   https://en.wikipedia.org/wiki/Data_access_object#:~:text=In%20software%2C%20a%20data%20access
[^3]:   https://en.wikipedia.org/wiki/Front_end_and_back_end
[^4]:   https://www.w3schools.com/html/
[^5]:   https://www.w3schools.com/js/js_htmldom.asp  
[^6]:   https://www.w3schools.com/css/




 


Contact:\
Lucia Macakova\
email: G00439449@atu.ie

