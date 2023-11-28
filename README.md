# Learning Management System (LMS) Platform

## Project Overview

This Learning Management System (LMS) platform is designed to provide a comprehensive educational solution. Below is an outline of its typical scope:

### Scope
1. **User Management**
    - Authentication and registration
    - User roles and permissions (e.g., instructor, student)
2. **Course Management**
    - The admin manages semesters and semester courses
    - The teacher manages the lessons in a course
    - Creation, editing, and deletion of courses
3. **Content Management**
    - Upload and organization of learning materials (e.g., lectures, videos, documents)
    - Support for multimedia content
4. **Grades Management**
    - Upload, delete, and edit grades for students
    - Students can view their grades
5. **Certificates Management**
   - Upload and delete certificates for students
   - Students can view and download their certificates
6. **Profile Management**
   - Users can add additional information like bio,profile picture which can be updated too

## Installation Guide

### Requirements
- Python
- Django
- HTML, CSS, JavaScript
- dbsqlite

### Steps to Run the Project Locally

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/oneshikaa/LearningManagementPlatform
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

5. **Access the Application:**
    Open a web browser and go to `http://localhost:8000/`.

## Project Details

### Product Perspective
The LMS platform is a self-contained product developed from scratch. It serves as a web-based technology designed for planning, implementing, and assessing various learning processes.

### Product Features
The platform encompasses major features such as user, course, content, and grades management.

### User Classes and Characteristics
Users include admin,students,instructors with varying technical expertise and educational levels. The platform aims to be user-friendly for all levels of technical proficiency.

![Use Case Diagram](screenshots/use_case.png)

### Operating Environment
The LMS platform operates within a web-based environment, utilizing Django for the backend and supports various browsers and operating systems.

