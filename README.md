# 🍽️ Recipe API Project

A Django REST Framework API for managing recipes and categories with token authentication.

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Project
git clone https://github.com/HussainSalah404/Hussain-s-Capstone-project.git
cd recipe_api_project

### 2️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

### 3️⃣ Create a Superuser
python manage.py createsuperuser

### 4️⃣ Run the Server
python manage.py runserver

---

## 🔑 Authentication (Postman Setup)

### Step 1: Create a User
Option 1 – via Admin:
- Go to http://127.0.0.1:8000/admin/ and add a new user.

Option 2 – via API:
POST http://127.0.0.1:8000/users/register/
Content-Type: application/json

{
  "username": "testuser",
  "password": "1234"
}

### Step 2: Get Token
POST http://127.0.0.1:8000/auth/token/
Content-Type: application/json

{
  "username": "testuser",
  "password": "1234"
}

Response:
{
  "token": "efbe02e4f42198c3239837be657af8652a4f359b"
}

### Step 3: Use Token in Postman
In every API request:

Headers tab:
Key: Authorization  
Value: Token efbe02e4f42198c3239837be657af8652a4f359b

Or use the Authorization tab:
Type: Bearer Token  
Value: efbe02e4f42198c3239837be657af8652a4f359b

---

## 🍴 Recipes Endpoints

### ✅ List All Recipes
GET http://127.0.0.1:8000/recipes/

### ➕ Create a Recipe
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

### 🔍 Get One Recipe
GET http://127.0.0.1:8000/recipes/1/

### ✏️ Update a Recipe
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

### ❌ Delete a Recipe
DELETE http://127.0.0.1:8000/recipes/1/
Authorization: Token <your_token>

---

## 🗂️ Categories Endpoints

### ✅ List All Categories
GET http://127.0.0.1:8000/categories/

### ➕ Create a Category
POST http://127.0.0.1:8000/categories/
Content-Type: application/json
Authorization: Token <your_token>

{
  "name": "Dessert"
}

### 🔍 Get One Category
GET http://127.0.0.1:8000/categories/1/

---

## 🧩 Example API Workflow

Follow this flow in Postman:

1. Register or Create a User  
   POST /users/register/

2. Get the Auth Token  
   POST /auth/token/  
   → Copy the "token" from the response.

3. Set the Token in Postman  
   - Go to the “Authorization” tab  
   - Type: Bearer Token  
   - Paste your token value.

4. Create a Category  
   POST /categories/  
   {
     "name": "Dessert"
   }

5. Create a Recipe  
   POST /recipes/  
   {
     "title": "Chocolate Cake",
     "description": "Rich and moist",
     "ingredients": "Flour, Sugar, Cocoa, Eggs",
     "instructions": "Mix and bake",
     "category": 1
   }

6. View All Recipes  
   GET /recipes/

7. Update or Delete as Needed  
   PUT /recipes/1/  
   DELETE /recipes/1/

---

## 🧰 Notes

- Every protected endpoint requires the token in headers.
- You can view public recipes without authentication.
- Only authenticated users can add, edit, or delete recipes.

---

## 🧑‍💻 Developer
**Hussain Salah**
