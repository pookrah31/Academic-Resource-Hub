Academic Resource Hub 🎓
A specialized platform for university students to share and access course-specific academic materials.

📝 Project Overview
The Academic Resource Hub is a RESTful API designed to solve the problem of disorganized study materials. It provides a centralized repository where students can upload and download lecture notes, past questions, and handouts linked directly to their university course codes.

This project is a Portfolio Project for the ALX Software Engineering program.

🚀 Key Features
Custom User Authentication: Extended Django's AbstractUser to include student-specific fields like Department and Academic Level.

JWT Security: Implemented JSON Web Tokens (SimpleJWT) to secure the API, ensuring only authenticated students can contribute resources.

Course-Resource Mapping: A structured database linking study materials to specific courses (e.g., CS 401).

Admin Management: A customized Django Admin dashboard for content moderation and user oversight.

🛠️ Technical Stack
Backend Framework: Django & Django REST Framework (DRF)

Database: SQLite (File-based database for development)

Security: Stateless authentication using JWT

Language: Python 3.14

🏗️ System Architecture
The project follows a decoupled API architecture:

Models: Custom User (AbstractUser), Course, and Material.

Serializers: Data translation between Python objects and JSON.

Permissions: IsAuthenticatedOrReadOnly ensures the API is publicly readable but requires a token for uploads.

⚙️ Setup & Installation
1. Clone and Navigate
Bash
git clone https://github.com/pookrah31/Academic-Resource-Hub.git
cd Academic-Resource-Hub
2. Environment Setup
Bash
# Activate Virtual Environment (Git Bash)
source venv/Scripts/activate

# Install Necessary Packages
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt
3. Database Initialization
Bash
# Build the SQLite database based on the AbstractUser and Resource models
python manage.py makemigrations users
python manage.py makemigrations resources
python manage.py migrate
4. Run the API
Bash
python manage.py runserver
📍 API Endpoints
🔐 Authentication
POST /api/token/ - Login with credentials to receive Access & Refresh tokens.

POST /api/token/refresh/ - Refresh an expired access token.

📚 Resources
GET /api/materials/ - View the list of all uploaded materials.

POST /api/materials/ - Upload a new academic resource (JWT Token Required).

GET /api/courses/ - View available courses.

🤝 Project Status
This project is currently in Week 2 of development. Upcoming features include:

Student Registration Endpoint: Allowing users to create accounts via the API.

Search & Filtering: Finding materials by Course Code or Title.

Voting System: Upvote/Downvote logic for quality control.

📄 License
MIT License - Developed by Peniel Osei Okrah. 
