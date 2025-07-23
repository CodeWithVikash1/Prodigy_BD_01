# 🛠️ Basic REST API with CRUD Operations (In-Memory Storage)

This is a simple REST API built using **Django** and **Django REST Framework**.  
It performs full **CRUD (Create, Read, Update, Delete)** operations on a `User` resource using an **in-memory data structure (Python dictionary / hashmap)** — no database used!

---

## 🚀 Features

- In-memory data storage using Python `dict` (like a hashmap)
- Unique `UUID` used as ID for each user
- Full CRUD API:
  - Create user
  - Get all users
  - Get single user
  - Update user
  - Delete user
- Input validation using DRF Serializers
- Clean and simple code structure

---

## 📦 Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework

---

## 🔧 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/CodeWithVikash1/Prodigy_BD_01
cd Prodigy_BD_01

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the development server
python manage.py runserver
