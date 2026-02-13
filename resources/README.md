# Academic Resource Hub 🎓

A specialized RESTful API for Ghanaian students to share and access course-specific academic materials.

 Key Features
Custom Authentication: Leveraged Django’s `AbstractUser` to create a tailored user model including `Department` and `Level`.
Resource Management: Structured database for `Courses` and `Materials` using SQLite.
RESTful Endpoints: Clean API routes for listing and uploading resources.
Admin Control: Customized Django Admin panel for platform management.

 Tech Stack
Backend: Django & Django REST Framework
Database: SQLite (Perfect for development/testing)
Security: Extended AbstractUser Auth

##  Quick Start
1. `git clone https://github.com/pookrah31/Academic-Resource-Hub.git`
2. `source venv/Scripts/activate`
3. `pip install django djangorestframework django-cors-headers`
4. `python manage.py migrate`
5. `python manage.py runserver`