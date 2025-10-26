# 🍽️ Recipe API Project

A **Django REST Framework** API for managing recipes and categories with authentication (JWT-based).

---

## 🚀 Setup Instructions

1️⃣ **Clone the Project**
```bash
git clone https://github.com/HussainSalah404/Hussain-s-Capstone-project.git
cd recipe_api_project
```

2️⃣ **Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

3️⃣ **Create a Superuser**
```bash
python manage.py createsuperuser
```

4️⃣ **Run the Server**
```bash
python manage.py runserver
```

---

## 🔑 Authentication Endpoints

### 🧍 Register User
**POST** `http://127.0.0.1:8000/auth/register/`

**Request:**
```json
{
  "username": "testuser",
  "password": "1234"
}
```

**Response:**
```json
{
  "message": "User registered successfully, your id is 6",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6..."
}
```

---

### 🔐 Login User
**POST** `http://127.0.0.1:8000/auth/login/`

**Request:**
```json
{
  "username": "testuser",
  "password": "1234"
}
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6...",
  "id": 6
}
```

---

### 🚪 Logout
**POST** `http://127.0.0.1:8000/auth/logout/`

**Headers:**
```
Authorization: Bearer <your_token>
```

**Response:**
```json
{
  "message": "Logout successful (client-side only)"
}
```

---

## 🍴 Recipe Endpoints

### ✅ List All Recipes
**GET** `http://127.0.0.1:8000/recipes/`

**Response:**
```json
[
  {
    "id": 1,
    "title": "Chocolate Cake",
    "description": "Rich and moist",
    "ingredients": "Flour, Sugar, Cocoa, Eggs",
    "instructions": "Mix and bake",
    "category": { "id": 1, "name": "Dessert" },
    "owner": "testuser",
    "created_at": "2025-10-26T13:59:00Z"
  }
]
```

---

### ➕ Create a Recipe
**POST** `http://127.0.0.1:8000/recipes/`

**Headers:**
```
Authorization: Bearer <your_token>
Content-Type: application/json
```

**Request:**
```json
{
  "title": "Chocolate Cake",
  "description": "Delicious dessert",
  "ingredients": "Flour, Eggs, Cocoa, Sugar",
  "instructions": "Mix and bake",
  "category_id": 1
}
```

**Response:**
```json
{
  "id": 2,
  "title": "Chocolate Cake",
  "description": "Delicious dessert",
  "ingredients": "Flour, Eggs, Cocoa, Sugar",
  "instructions": "Mix and bake",
  "category": { "id": 1, "name": "Dessert" },
  "owner": "testuser",
  "created_at": "2025-10-26T14:00:00Z"
}
```

---

### 🔍 View One Recipe
**GET** `http://127.0.0.1:8000/recipes/1/`

---

### ✏️ Update a Recipe
**PUT** `http://127.0.0.1:8000/recipes/1/`

**Request:**
```json
{
  "title": "Updated Chocolate Cake",
  "description": "Now with frosting",
  "ingredients": "Flour, Eggs, Cocoa, Sugar, Frosting",
  "instructions": "Mix, bake, frost",
  "category_id": 1
}
```

---

### ❌ Delete a Recipe
**DELETE** `http://127.0.0.1:8000/recipes/1/`

---

## 🗂️ Category Endpoints

### ✅ List All Categories
**GET** `http://127.0.0.1:8000/categories/`

---

### ➕ Create a Category
**POST** `http://127.0.0.1:8000/categories/`
```json
{
  "name": "Dessert"
}
```

---

### 🔍 Get One Category
**GET** `http://127.0.0.1:8000/categories/1/`

---

## 🧑‍💻 Developer
**Hussain Salah**
