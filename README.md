# 🌐 Learning Log & Multi-App Django Project

<!-- 📛 Project Badges -->
![Last Commit](https://img.shields.io/github/last-commit/DigiFenix777/python-crash-course-getting-started-with-django-project)
![Top Language](https://img.shields.io/github/languages/top/DigiFenix777/python-crash-course-getting-started-with-django-project)
![Repo Size](https://img.shields.io/github/repo-size/DigiFenix777/python-crash-course-getting-started-with-django-project)
![Issues](https://img.shields.io/github/issues/DigiFenix777/python-crash-course-getting-started-with-django-project)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🔑 Executive Summary
This project demonstrates how to use **Python with Django** to build full-stack web applications that include authentication, data modeling, and modular app integration. While the focus was on learning Django’s fundamentals, the lessons directly connect to **cybersecurity principles**:

- Implementing **user authentication** (login, logout, registration).
- Enforcing **authorization and access control** with decorators and ownership checks.
- Exploring how **data privacy** can be tied to specific users.
- Gaining exposure to **modular, reusable security features** built into modern frameworks.

👉 For recruiters and hiring managers: this project highlights my ability to **understand how web applications handle authentication, authorization, and user data protections**—key concepts for application security, compliance, and secure system administration.

---

## 📌 Overview

Key lessons explored in this project:

- Setting up Django projects and apps.
- Defining **models** and working with a relational database.
- Using the **Django Admin site** for managing application data.
- Building views, templates, and URL mappings for navigation.
- Enabling **user account functionality** (login, logout, registration).
- Restricting access to content with `@login_required` decorators.
- Associating topics and entries with specific users.
- Styling applications with **Bootstrap**.

Customizations:
- Integrated multiple apps (Learning Log, Blogs, Pizzas, Meal Planner) into a **single Django project**.
- Extended authentication and navigation **globally across all apps** for consistency.

---

## 🧠 Skills & Concepts

- **Django fundamentals**: projects, apps, models, views, templates, URLconfs.
- **Database migrations** and data modeling.
- **User authentication** (login/logout, registration).
- **Access control**: restricting pages and associating data with specific users.
- **Form handling**: GET/POST requests, ModelForms.
- **UI/UX** with Bootstrap 5 integration.

Cybersecurity tie-ins:
- Learned how **modular authentication and access control** are implemented in a framework.
- Observed how **session management** and `@login_required` enforce least privilege.
- Gained appreciation for how frameworks simplify **secure defaults** and help prevent vulnerabilities (e.g., CSRF tokens, form validation).

---

## 🗂️ Repository Structure

<details>
<summary>Click to expand project tree</summary>

```plaintext
project-django-learning-log/
│
├── accounts/ 
│    ├── migrations
│    ├── templates
│    │   └── registration
│    │       ├── login.html
│    │       └── register.html
│    │
│    ├── __init__.py
│    ├── admin.py
│    ├── apps.py
│    ├── models.py
│    ├── tests.py
│    ├── urls.py
│    └── views.py
│
├── blog/
│    ├── __init__.py
│    └── urls.py
│                     
├── blogs/                    # Blog app with accounts & posts
│    ├── migrations
│    ├── templates
│    │   └── blogs
│    │       ├── base.html
│    │       ├── blog.html
│    │       ├── blogs.html
│    │       ├── end_post.html
│    │       ├── index.html
│    │       ├── new_blog.html
│    │       └── new_post.html
│    │
│    ├── __init__.py
│    ├── admin.py
│    ├── apps.py
│    ├── forms.py
│    ├── models.py
│    ├── tests.py
│    ├── urls.py
│    └── views.py
│
├── learning_log/             # Main project settings & URLs
│    ├── migrations
│    ├── templates
│    │   └── learning_logs
│    │       ├── base.html
│    │       ├── edit_entry.html
│    │       ├── index.html
│    │       ├── new_entry.html
│    │       ├── new_topic.html
│    │       ├── topic.html
│    │       └── topics.html
│    │
│    ├── __init__.py
│    ├── admin.py
│    ├── apps.py
│    ├── forms.py
│    ├── models.py
│    ├── tests.py
│    ├── urls.py
│    └── views.py
│
├── ll_project/ 
│    ├── __init__.py
│    ├── asgi.py
│    ├── settings.py
│    ├── urls.py
│    └── wsgi.py
│
├── meal_planner/             # Meal planner app
│    ├── migrations
│    ├── templates
│    │   └── meal_plans
│    │       ├── base.html
│    │       ├── index.html
│    │       ├── meal.html
│    │       └── meals.html
│    │
│    ├── __init__.py
│    ├── admin.py
│    ├── apps.py
│    ├── models.py
│    ├── tests.py
│    ├── urls.py
│    └── views.py
│
├── ll_project/ 
│    ├── __init__.py
│    └── urls.py
│
├── pizzas/                   # Pizzeria app (menu builder)
│    ├── migrations
│    ├── templates
│    │   └── pizzas
│    │       ├── base.html
│    │       ├── index.html
│    │       ├── pizza.html
│    │       └── pizzas.html
│    │
│    ├── __init__.py
│    ├── admin.py
│    ├── apps.py
│    ├── models.py
│    ├── tests.py
│    ├── urls.py
│    └── views.py
│
├── pizzeria_project/ 
│    ├── asgi.py
│    ├── __init__.py
│    ├── settings.py
│    ├── urls.py
│    └── wsgi.py
│
├── templates/                # Shared templates (base, nav, auth)
│    └── base.html
│
├── .gitattributes
├── .gitignore
├── LICENSE
├── manage.py
├── README.py
└── requirements.txt
```
</details>



---

## 🚀 How to Run

1. Clone this repo and move into the folder:

```bash
git clone git@github.com:your-username/project-django-learning-log.git
cd project-django-learning-log
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```
4. Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

5. Open in browser:

```bash
http://127.0.0.1:8000/
```

---

## 🔎 Skills Spotlight

- Django ORM for secure database queries.
- Authentication & Authorization baked into the framework.
- Modular architecture (apps with isolated models, views, templates).
- Bootstrap 5 integration for polished UI.

**Cybersecurity relevance:**
- Exposure to secure session handling.
- Practical understanding of access control enforcement.
- Insights into user data protection and principle of least privilege.

---

## 📝 Lessons Learned
- How Django projects are structured and why modular apps matter.
- How frameworks simplify secure coding practices (auth, forms, CSRF protection).
- Why access control and ownership checks are vital for protecting user data.
- The importance of styling and usability for adoption—even in secure systems.

---

# 📊 Exercises Implemented
- 18-1 to 18-8 → Pizzeria and Meal Planner apps (models, templates, forms).
- 19-1 to 19-5 → Blog app with authentication, refactoring, and protected entries.
- Customization → Integrated all apps into one unified project with global authentication and navigation.

---

# 📚 Attribution
Based on exercises from:
Matthes, E. (2023). Python Crash Course (3rd ed.). No Starch Press.
https://nostarch.com/python-crash-course-3rd-edition

---
## 🧩 License

Distributed under the MIT License.
See LICENSE for details.

---
