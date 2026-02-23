🎓 Academic Resource Hub
A full-stack specialized platform for university students to share, organize, and access course-specific academic materials.

📝 Project Overview
The Academic Resource Hub is a comprehensive web application designed to solve the problem of disorganized study materials. It provides a centralized repository where students can upload and download lecture notes, past questions, and handouts linked directly to their university course codes.

This project is the Capstone Portfolio Project for the ALX Software Engineering program.

🚀 Key Features
Single Page Application (SPA): A fast, responsive frontend built with Vanilla JavaScript and Bootstrap 5.

JWT Security: Implemented stateless authentication using JSON Web Tokens (SimpleJWT).

Dynamic Grouping: Resources are automatically categorized by Course Code for a structured, folder-like user experience.

Gamification & Badges: A contribution-based system where students earn badges (Newcomer, Star Contributor, Academic Legend) based on their uploads.

Personalized Dashboard: Includes a user profile, department/level tracking, and profile picture support.

Interactive Header: Features a rotating slogan system for guests and a personalized greeting for logged-in students.

Search & Filtering: Real-time filtering of resources by Course Code.

🛠️ Technical Stack
Backend: Django & Django REST Framework (DRF)

Frontend: JavaScript (ES6+), HTML5, Bootstrap 5

Database: SQLite

Image Processing: Pillow

Security: Stateless JWT Authentication

⚙️ Setup & Installation
1. Clone and Navigate
Bash
git clone https://github.com/pookrah31/Academic-Resource-Hub.git
cd Academic-Resource-Hub
2. Environment Setup
Bash
# Create and Activate Virtual Environment
python -m venv venv
source venv/Scripts/activate  # On Windows use: venv\Scripts\activate

# Install Necessary Packages
pip install -r requirements.txt
3. Database Initialization
Bash
python manage.py makemigrations
python manage.py migrate
4. Run the Application
Bash
python manage.py runserver
The API will be available at http://127.0.0.1:8000/api/ and the frontend can be accessed via index.html.

📍 API Endpoints
🔐 Authentication
POST /api/register/ - Create a new student account.

POST /api/login/ - Login to receive JWT Access & Refresh tokens.

GET /api/auth/profile/ - Retrieve or update current user profile (Supports PATCH for profile pictures).

📚 Resources
GET /api/materials/ - View materials (Supports ?course__course_code= filtering).

POST /api/materials/ - Upload new resource (Requires JWT).

POST /api/materials/{id}/upvote/ - Upvote a resource to improve its quality ranking.

GET/POST /api/courses/ - View or register new course codes.

📄 License
MIT License - Developed by Peniel Osei Okrah.
