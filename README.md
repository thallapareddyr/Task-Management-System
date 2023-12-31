# Task Management System

This Task Management System is a web application built using Django that facilitates task creation, assignment, tracking, and reporting. It allows for efficient management of tasks across different user roles with distinct privileges.

## Features

- **User Management:**
  - Registration for regular users and administrators.
  - Two user types: regular users and administrators with varying access rights.

- **Task Management:**
  - Create, assign, and track tasks.
  - Task categories for better organization and filtering.
  - Status tracking for tasks (e.g., pending, completed, overdue).

- **Email Notifications:**
  - Automated email notifications for task assignments, updates, and reminders for approaching due dates.

## Technologies Used

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (for local development)
- **Deployment:** PythonAnywhere/Heroku

## Project Structure

- **`/app`:** Contains Django application files.
- **`/templates`:** HTML templates for frontend pages.
- **`/static`:** CSS, JS, and other static files.
- **`/scripts`:** Scripts for automated tasks or setup.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository_url>
   cd task-management-system
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server:**
   ```
   python manage.py runserver
   ```

6. **Access the application:**
   - Open a web browser and go to `http://localhost:8000`

## Contribution Guidelines

- Fork the repository.
- Create a new branch (`git checkout -b feature/new-feature`).
- Commit your changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature/new-feature`).
- Create a new Pull Request.

## Authors

- [Your Name](https://github.com/your_username)

## Acknowledgements


## License

This project is licensed under the [MIT License](LICENSE).