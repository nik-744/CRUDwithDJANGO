# Django CRUD Application with Forms

This is a simple Django-based CRUD (Create, Read, Update, Delete) application that manages student records using Django Forms (not Django REST Framework).

## 📁 Features

* Create new student entries
* View list of all students
* Update student information
* Delete student records
* Uses Django built-in forms for validation

---

## 🛠️ Technologies Used

* Python 3.x
* Django 4.x or 5.x
* SQLite (default DB)

---

## 📦 Project Structure

```
DjangoCRUDproject/
├── operations/
│   ├── migrations/
│   ├── templates/
│   │   └── operations/
│   │       ├── student_form.html
│   │       └── student_list.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── DjangoCRUDproject/
│   └── settings.py
├── db.sqlite3
└── manage.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-crud.git
cd django-crud
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Open your browser at: `http://127.0.0.1:8000/`

---

## 🧹 Models

```python
class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    department = models.CharField(max_length=100)
```

---

## 🖊 Forms

```python
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
```

---

## 🌐 URLs

```python
urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]
```

---

## 📬 License

This project is licensed under the MIT License. See `LICENSE` for more information.
