# 🍽️ Recipe API Project

A Django REST Framework API for managing recipes and categories with token authentication.

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Project
```bash
git clone https://github.com/<your-username>/recipe_api_project.git
cd recipe_api_project
2️⃣ Run Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
3️⃣ Create a Superuser
bash
Copy code
python manage.py createsuperuser
4️⃣ Run the Server
bash
Copy code
python manage.py runserver
🔑 Authentication (Postman Setup)
Step 1: Create a User
Option 1 – via Admin:

Go to http://127.0.0.1:8000/admin/ and add a new user.

Option 2 – via API:

http
Copy code
POST http://127.0.0.1:8000/users/register/
Content-Type: application/json

{
  "username": "testuser",
  "password": "1234"
}
Step 2: Get Token
http
Copy code
POST http://127.0.0.1:8000/auth/token/
Content-Type: application/json

{
  "username": "testuser",
  "password": "1234"
}
Response:

json
Copy code
{
  "token": "efbe02e4f42198c3239837be657af8652a4f359b"
}
Step 3: Use Token in Postman
In every API request:

Headers tab

makefile
Copy code
Key: Authorization
Value: Token efbe02e4f42198c3239837be657af8652a4f359b
Or use the Authorization tab:

Type: Bearer Token

Value: efbe02e4f42198c3239837be657af8652a4f359b

🍴 Recipes Endpoints
✅ List All Recipes
http
Copy code
GET http://127.0.0.1:8000/recipes/
➕ Create a Recipe
http
Copy code
POST http://127.0.0.1:8000/recipes/
Content-Type: application/json
Authorization: Token <your_token>

{
  "title": "Chocolate Cake",
  "description": "Delicious dessert",
  "ingredients": "Flour, Eggs, Cocoa, Sugar",
  "instructions": "Mix and bake",
  "category": 1
}
🔍 Get One Recipe
http
Copy code
GET http://127.0.0.1:8000/recipes/1/
✏️ Update a Recipe
http
Copy code
PUT http://127.0.0.1:8000/recipes/1/
Content-Type: application/json
Authorization: Token <your_token>

{
  "title": "Updated Chocolate Cake",
  "description": "Now with frosting",
  "ingredients": "Flour, Eggs, Cocoa, Sugar, Frosting",
  "instructions": "Mix, bake, frost",
  "category": 1
}
❌ Delete a Recipe
http
Copy code
DELETE http://127.0.0.1:8000/recipes/1/
Authorization: Token <your_token>
🗂️ Categories Endpoints
✅ List All Categories
http
Copy code
GET http://127.0.0.1:8000/categories/
➕ Create a Category
http
Copy code
POST http://127.0.0.1:8000/categories/
Content-Type: application/json
Authorization: Token <your_token>

{
  "name": "Dessert"
}
🔍 Get One Category
http
Copy code
GET http://127.0.0.1:8000/categories/1/
🧰 Notes
Make sure your token is added to every protected endpoint.

You can view, edit, and delete recipes only when authenticated.

Public users can view recipes but can’t create or edit them.

🧑‍💻 Developer
Hussain Salah