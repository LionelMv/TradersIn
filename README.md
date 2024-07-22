# TradersIn

## About
This is a blog web application for traders where they can share their knowledge and expertise and also get to interact with one another in the platform.

## Installation

### 1. Clone the repository
```
git clone https://github.com/LionelMv/TradersIn.git
```

### 2. Create a virtual environment.
To learn how to create and activate a virtual environment, check this link: [Django - Create Virtual Environment](https://www.w3schools.com/django/django_create_virtual_environment.php)

### 3. Install required packages
All these packages are listed in the requirements file:
- Django
- Python-decouple
- Pillow
- djangorestframework
- mysql-connector-python
- crispy-bootstrap5

To learn how to use python-decouple, check this link: [python-decouple](https://pypi.org/project/python-decouple/)
```
pip install requirements.txt
```

### 4. Configure your own database.
While using SQL lite is sufficient, you can choose to use a different database according to your preference.
For this project, I have used MySQL.
You need to install MySQL and configure it to work with this project.
Reference Manual: [How to Use MySQL with Django](https://studygyaan.com/django/how-to-use-mysql-database-with-django-project).

After, run the following commands when in the project directory.
```
cd TradersIn
python manage.py makemigrations
python manage.py migrate
```

### 5. View the webpage
```
cd TradersIn
python manage.py runserver
```

On your browser, run the following link: http://127.0.0.1:8000/ or http://localhost:8000/.