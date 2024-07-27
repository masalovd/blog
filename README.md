# Django Blog Project

## Overview
This project is a blog application built using pure Django. It allows users to register, log in, log out, change passwords, create posts, and view posts created by specific users.

## Features

### Authentication
- **User Registration**: Users can create an account using the registration form.
- **Login**: Registered users can log in to their accounts.
- **Logout**: Logged-in users can log out of their accounts.
- **Change Password**: Users can change their password using the password change form.

### Blog Functionality
- **Create Post**: Users can create new blog posts.
- **View All Posts**: Users can view all posts created by other users.
- **View Posts by User**: Users can view all posts created by a specific user.
- **CRUD Operations**: Basic Create, Read, Update, and Delete operations are implemented for blog posts.

### Signals
- **Custom Signals**: The application uses Django signals to perform specific actions automatically when certain events occur (e.g., sending notifications when a new post is created).

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv .venv
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Generate a Django SECRET_KEY** using [Djecrety](https://djecrety.ir/) and add it to your .env file:

    ```bash
    # ./crm_app/.env

    SECRET_KEY="your-secret-key"
    ...
    ```
    
6. **Generate an app password to send email from your app** using this [instructions](https://support.google.com/accounts/answer/185833?hl=en):

    ```bash
    # ./crm_app/.env

    EMAIL_USER=<your-email>
    EMAIL_PASSWORD=<generated-password>
    ...
    ```

7. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

## Technologies Used
- **Django**: Web framework for building the application.
- **Pillow**: Python Imaging Library that provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.
- **Crispy**: The best way to have Django DRY forms.
- **SQLite**: A small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- **HTML/CSS**: For the front-end design.
- **Bootstrap5**: CSS framework for the front-end design.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

