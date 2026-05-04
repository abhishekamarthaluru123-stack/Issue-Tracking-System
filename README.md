# 🐞 Issue Tracking System

A Django-based web application to manage and track bugs/issues within a project. This system allows users to create, assign, update, and monitor bugs efficiently.

---

## 🚀 Features

* 📝 Create and manage bugs
* 👤 Assign bugs to users
* 📊 Dashboard to view all issues
* 🔄 Update bug status
* 🧾 Form-based input validation
* 🌐 Full-stack implementation using Django templates

---

## 🏗️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Templates)
* **Database:** SQLite (default)
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```
IssueTrackingSystem/
│
├── manage.py
├── IssueTrackingSystem/     # Main project settings
├── bugs/                   # Core app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/              # HTML templates
│   ├── home.html
│   ├── dashboard.html
│   ├── create_bug.html
│   ├── assign.html
│   ├── login.html
│
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run migrations

```
python manage.py migrate
```

### 5. Start the server

```
python manage.py runserver
```

### 6. Open in browser

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

---

## 🔐 Future Improvements

* Authentication system (Login/Register with roles)
* Bug priority levels (Low, Medium, High)
* Advanced filtering & search
* File/image attachments
* REST API using Django REST Framework
* UI improvements (Bootstrap/Tailwind)
* Deployment (Render / AWS)

---

## 🌍 Deployment

*Deployment link will be added here*

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Abhishek Amarthaluru**

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!
