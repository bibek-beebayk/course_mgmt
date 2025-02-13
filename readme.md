## Local Setup Guide
1. Create a virtual environment and install the dev dependencies:
```bash
python -m venv env
source env/bin/activate
pip install -r requirements/dev.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser to access the django admin interface:
```bash
python manage.py createsuperuser
```

4. Run the development server
```bash
python manage.py runserver
```

5. Now you can access the admin interface at ```http://127.0.0.7:8000/admin```

6. You can perform CRUD operations for Course, Student and Category from the admin interface.
7. The home page at ```http://127.0.0.1``` provides a basic interface that lists all the available courses and allows enrollment of students to specific course.