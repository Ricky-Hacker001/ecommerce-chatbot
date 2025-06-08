# 🛍️ IntelliShop: E-commerce Chatbot
An intelligent e-commerce chatbot application built with React, Flask, and SQLite3. Users can sign up, log in, and chat with a bot to search for products. The chatbot responds with relevant product suggestions in an inline conversational style.

# 🚀 Features
🔐 User authentication (Signup & Login)
💬 Chatbot-style product search interface
🛒 Smart inline product responses inside the chat
🖼️ Product cards with image, name, price, and description
🧠 React Context API for auth management
🧪 Faker-free mode: curated realistic products instead of dummy data

# 🧱 Tech Stack
Frontend: React + React Router
Backend: Flask (Python)
Database: SQLite3 with SQLAlchemy
Authentication: JWT
Styling: Custom CSS

# 🛠️ Installation
🔙 Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python db_init.py
python app.py

🔜 Frontend
cd frontend
npm install
npm start

# 🧪 Sample Users
You can sign up via the Signup page, or pre-create users in db_init.py using:
Add inside db_init.py (optional)
user = User(username="testuser", password=generate_password_hash("testpass"))
db.session.add(user)
db.session.commit()

# 🔑 API Endpoints
Auth
POST /api/auth/signup – Register a new user

POST /api/auth/login – Authenticate and return a JWT token

# Products
GET /api/products/search?q=<query> – Search products by name/category/brand
{
  "name": "iPhone 14 Pro Max",
  "category": "Smartphone",
  "brand": "Apple",
  "price": 139999,
  "description": "Flagship Apple smartphone with Dynamic Island and 48MP camera.",
  "image_url": "https://example.com/images/iphone14promax.jpg"
}
