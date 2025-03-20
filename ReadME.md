# URL Shortener

A Django-based URL shortening service that allows users to shorten long URLs, redirect to the original URL using a short code, and view statistics for each shortened URL. The project includes features to update and delete URLs, with a responsive front-end built using Bootstrap.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- **Shorten URLs**: Convert long URLs into short, manageable codes.
- **Redirect**: Redirect users to the original URL using the short code.
- **Statistics**: View stats for each shortened URL, including access count, creation date, and last updated date.
- **Update/Delete URLs**: Modify or delete existing shortened URLs.
- **Responsive UI**: A clean, user-friendly interface built with Bootstrap 5.
- **Error Handling**: Proper error messages for invalid inputs or non-existent short codes.
- **CSRF Protection**: CSRF tokens are used for secure POST, PUT, and DELETE requests.

---

## Project Structure

```
urlshortener/
│
├── manage.py
├── urlshortener/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shortener/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── templates/
│   │   └── shortener/
│   │       └── index.html
│   │       └── stats.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── README.md
```
## Prerequisites

- **Python**: Version 3.8 or higher
- **Django**: Version 4.2 or higher
- **Django REST Framework**: For API functionality
- **Bootstrap**: Version 5.3.2 (included via CDN in the template)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AliAffanBajwa/URL-Shortening-Service.git
   cd urlshortener
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   django>=4.2
   djangorestframework>=3.14
   ```
   Then install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Run migrations to set up the SQLite database (or your preferred database):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Optional)**:
   To access the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   The app will be available at `http://127.0.0.1:8000/`.

---

## Usage

1. **Shorten a URL**:
   - Use the API endpoint `/shorten/` to create a new shortened URL.
   - Alternatively, implement a front-end form to interact with this endpoint.

2. **Redirect to Original URL**:
   - Visit `/r/<short_code>/` to redirect to the original URL.
   - Example: `http://127.0.0.1:8000/r/abc123/`

3. **View URL Statistics**:
   - Navigate to `/stats/` and enter the short code to view stats.
   - Example: Enter `abc123` to see details like the original URL, access count, and creation date.

4. **Update or Delete a URL**:
   - From the stats page, use the "Update" or "Delete" buttons to modify or remove a URL.

---

## API Endpoints

The project uses Django REST Framework to provide the following API endpoints:

| Method | Endpoint                | Description                          |
|--------|-------------------------|--------------------------------------|
| POST   | `/shorten/`             | Create a new shortened URL           |
| GET    | `/stats/<short_code>/`  | Retrieve stats for a short code      |
| PUT    | `/<short_code>/`        | Update the URL for a short code      |
| DELETE | `/<short_code>/`        | Delete a shortened URL               |
| GET    | `/r/<short_code>/`      | Redirect to the original URL         |



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
