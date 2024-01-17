# Task Management System

This Task Management System is a web application built using Django that facilitates task creation, assignment, tracking, and reporting. It allows for efficient management of tasks across different user roles with distinct privileges.

## Features

- **User Management:**
  - Registration for regular users and administrators.
  - Three user types: Admin and Manager have access to create, assign, and modify the tasks
- **Task Management:**
  - Create, assign, and track tasks.
  - Task categories for better organization and filtering.
  - Status tracking for tasks (e.g., pending, completed, overdue).

- **Email Notifications:**
  - Automated email notifications for task assignments, updates, and changes in due dates.

## Technologies Used

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (for local development)
- **Deployment:** AWS EC2

## Project Structure

- **`/app`:** Contains Django application files.
- **`/templates`:** HTML templates for frontend pages.
- **`/static`:** CSS, JS, and other static files.
- **`/scripts`:** Scripts for automated tasks or setup.

## ER Diagram
![TaskManagementSystem ER Diagram](https://github.com/thallapareddyr/Task-Management-System/assets/149210091/8b3683ce-2720-4636-8600-17d270bcc144)

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/thallapareddyr/Task-Management-System.git
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

- [Thallapa Rahul](https://github.com/thallapareddyr)

## Acknowledgements

I would like to acknowledge the following sources that were instrumental in the development of this project:

- [Django Documentation](https://docs.djangoproject.com/): I referred to the official Django documentation for guidance on web development using Django.

- AWS EC2 Instance Creation: The process of creating EC2 instances on AWS was guided by the AWS documentation and tutorials available on the [AWS website](https://aws.amazon.com/).

These references played a significant role in shaping certain aspects of the project. I am grateful for the valuable insights provided by these resources.


## License

This project is licensed under the [MIT License](LICENSE).
