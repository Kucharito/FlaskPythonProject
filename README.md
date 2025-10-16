# 💰 ExpensesProject – Flask Expense Tracker

A simple and modular **Flask-based web application** for tracking personal expenses.  
The project is built to demonstrate the structure of a modern Flask app with authentication, database models, and templating.  
It is currently under active development and serves as a foundation for further expansion (e.g., user registration, login system, dashboards, and analytics).

---

## 🧱 Project Overview

The goal of the project is to provide a lightweight **Expense Tracker** web app where users can:

- Register and log in (via `Flask-Login`)
- Manage personal expenses stored in a local database (SQLite)
- View expenses through a simple dashboard
- Extend functionality easily using Flask blueprints

At the current stage, the core Flask setup is functional — the app runs successfully, loads templates, serves static files, and initializes the database.

---

## ⚙️ Tech Stack

| Category | Technology |
|-----------|-------------|
| Backend | **Python 3.12**, **Flask** |
| ORM / DB | **SQLAlchemy**, **SQLite** |
| Authentication | **Flask-Login** |
| Forms | **Flask-WTF** |
| Frontend | **HTML5**, **CSS (Bootstrap planned)** |
| Configuration | **dotenv (.env)** |
| IDE | **PyCharm Professional** |

---


## 💾 Database

The project uses **SQLite** for simplicity during development.  
The database file (`app.db`) is created automatically via SQLAlchemy when the application starts.

Environment configuration (in `.env`):
```bash
SECRET_KEY=super-secret-dev-key-change-me
DATABASE_URL=sqlite:///app.db
```

## 🚀 Running the Application
1. Clone the repostory
```bash
git clone https://github.com/yourusername/ExpensesProject.git
cd ExpensesProject
```

2. Create and activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the app
```bash
python main.py
```

5. Open your browser:
http://127.0.0.1:5000


## 🔒 Authentication

The project integrates **Flask-Login** for user session management.  
The `User` model and `user_loader` function are already implemented, and authentication blueprints are prepared (`auth.py`).

### Next steps include:
- [ ] Creating registration and login forms  
- [ ] Password hashing using `werkzeug.security`  
- [ ] Restricting access to certain routes (e.g., `/expenses`)

---

## 🧩 Planned Features

- [ ] User registration & login pages  
- [ ] Dashboard for expenses overview  
- [ ] Add / edit / delete expense entries  
- [ ] Category-based filtering  
- [ ] Monthly statistics (using Chart.js or Plotly)  
- [ ] Export data to CSV  
- [ ] Responsive Bootstrap 5 UI  

---

## 🧑‍💻 Development Notes

- The project uses the **App Factory Pattern**, which improves scalability.  
- **Blueprints** (`auth`, `expenses`) allow modular structure and cleaner code organization.  
- **Templates** follow the **Jinja2 inheritance model** – `base.html` serves as a common layout for all pages.  


## 🧑‍💻 Author
Created by Adam Kuchár