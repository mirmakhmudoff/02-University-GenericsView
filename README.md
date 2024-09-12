
# University CRM - API with Read-Only Access

This project is a CRM (Customer Relationship Management) system for managing university entities such as faculties, groups, kafedras (departments), subjects, teachers, and students. The system is built using Django and Django REST Framework (DRF) and provides a read-only API.

## Features

- **Read-Only API**: Provides list and detail views for all models via the API.
- **Admin Interface**: All create, update, and delete operations are performed exclusively through the Django admin interface.
- **Model Relationships**: Models are interlinked to reflect real-world university relationships (e.g., Groups belong to Faculties, Teachers are associated with Subjects, etc.).

## Setup

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mirmakhmudoff/02-University-GenericsView.git
   cd 02-University-GenericsView
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Admin Interface**

   Visit `http://127.0.0.1:8000/admin/` to log in with the superuser credentials and manage the data.

## API Endpoints

The API is read-only and provides the following endpoints:

- **Faculties**:
  - `GET /faculties/` - List all faculties.
  - `GET /faculties/<id>/` - Retrieve a specific faculty.

- **Groups**:
  - `GET /groups/` - List all groups.
  - `GET /groups/<id>/` - Retrieve a specific group.

- **Kafedras**:
  - `GET /kafedras/` - List all kafedras.
  - `GET /kafedras/<id>/` - Retrieve a specific kafedra.

- **Subjects**:
  - `GET /subjects/` - List all subjects.
  - `GET /subjects/<id>/` - Retrieve a specific subject.

- **Teachers**:
  - `GET /teachers/` - List all teachers.
  - `GET /teachers/<id>/` - Retrieve a specific teacher.

- **Students**:
  - `GET /students/` - List all students.
  - `GET /students/<id>/` - Retrieve a specific student.

## Customization

Feel free to modify the models, serializers, and views according to your specific requirements. All database operations should continue to be managed through the Django admin interface to maintain the integrity and security of the data.
