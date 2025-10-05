# 🍳 Recipe Management API

A Django REST Framework project for managing recipes.  
Users can create, update, delete, and view recipes by category or ingredient.

---

## 🚀 Features
- User registration and authentication
- CRUD operations for recipes
- Filter recipes by category or ingredient
- Organized structure for scalability

---

## 🧠 Models Overview
**Category** – groups recipes (e.g., Dessert, Breakfast)  
**Recipe** – stores all recipe details, linked to a user and a category  

---

## ⚙️ Setup Instructions
1. Clone the repository  
   ```bash
   git clone <your-repo-url>
   cd recipe_management_api
Create a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # on macOS/Linux
venv\Scripts\activate     # on Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Apply migrations

bash
Copy code
python manage.py migrate
Run the server

bash
Copy code
python manage.py runserver