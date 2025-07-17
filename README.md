# Hyper-Cars-Dealership-E-Commerce
## Description

Hyper-Cars-Dealership-E-Commerce is a comprehensive web application built with Django that serves as a Car Dealership Management System. It provides functionalities for managing car inventory, handling customer orders, and administering staff and drivers. The system supports different user roles: Admin, Staff, Driver, and Customer, each with tailored dashboards and permissions.

## Features

*   **User Authentication & Authorization:** Secure login and registration for different user roles (Admin, Staff, Driver, Customer).
*   **Role-Based Dashboards:** Customized dashboards for Admin, Staff, and Driver roles, providing relevant information and functionalities.
*   **Car Management:**
    *   Add, edit, and delete car listings.
    *   Manage car details including make, model, category, price, stock, type, transmission, gas, power, and year.
    *   Handle multiple images for each car.
*   **Order Management:**
    *   Customers can create orders for available cars.
    *   Staff can view pending orders, confirm them, assign drivers, and set delivery dates.
    *   Drivers can update the delivery status of assigned orders.
    *   View order history for both customers and staff.
*   **Staff Management (Admin only):**
    *   Add, edit, and delete staff accounts.
*   **Driver Management (Admin only):**
    *   Add, edit, and delete driver accounts.
*   **Contact Form:** A contact form for users to send messages to the dealership, with a dedicated section for staff to view received messages.
*   **Responsive Design:** (Assumed based on typical web development practices, will verify if possible during further analysis of templates/static files)

## Installation

To set up MyProject locally, follow these steps:

### Prerequisites

*   Python 3.x
*   pip (Python package installer)
*   Django (will be installed)
*   SQLite (default database, no separate installation needed)

### Steps

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd MyProject/My project/SD_project_code/version2/SD_project/myproject
    ```

    *(Note: Replace `<repository_url>` with the actual repository URL once available. The current path is based on the unzipped structure.)*

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Note: A `requirements.txt` file is assumed. If not present, you will need to create one with the necessary Django and other package versions.)*

4.  **Apply database migrations:**

    ```bash
    python manage.py makemigrations myproject
    python manage.py migrate
    ```

5.  **Create a superuser (admin account):**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an admin user. Alternatively, a default admin user (`admin@example.com` with password `0000`) is created automatically on `post_migrate` signal as per `models.py`.

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

### Accessing the Application

Open your web browser and navigate to `http://127.0.0.1:8000/`.

### User Roles and Access

*   **Admin:** Access the admin dashboard to manage staff, drivers, and view overall statistics. Default credentials: `admin@example.com` / `0000`.
*   **Staff:** Log in to manage cars, view pending orders, and order history.
*   **Driver:** Log in to view assigned orders and update delivery statuses.
*   **Customer:** Register for an account, browse cars, create orders, and view personal order history.

### Key Pages

*   `/`: Homepage displaying available cars.
*   `/login/`: User login page.
*   `/register/`: User registration page.
*   `/admin-dashboard/`: Admin dashboard.
*   `/staff-dashboard/`: Staff dashboard.
*   `/driver-dashboard/`: Driver dashboard.
*   `/manage-cars/`: Staff car management page.
*   `/pending-orders/`: Staff pending orders page.
*   `/orders_history/`: Staff order history page.
*   `/my-orders/`: Customer's order history.
*   `/contact/`: Contact form.
*   `/staff/messages/`: Staff's received messages.

## Project Structure

```
MyProject/
├── My project/
│   └── SD_project_code/
│       └── version2/
│           └── SD_project/
│               └── myproject/
│                   ├── manage.py
│                   ├── myproject/                  # Main Django project directory
│                   │   ├── __init__.py
│                   │   ├── settings.py             # Project settings
│                   │   ├── urls.py                 # Project URL configurations
│                   │   ├── wsgi.py
│                   │   ├── asgi.py
│                   │   ├── backends.py             # Custom authentication backend
│                   │   ├── forms.py                # Django forms
│                   │   ├── models.py               # Database models
│                   │   ├── views.py                # View functions
│                   │   ├── img/                    # Image assets
│                   │   ├── migrations/             # Database migrations
│                   │   ├── static/                 # Static files (CSS, JS, images)
│                   │   │   ├── css/
│                   │   │   └── img/
│                   │   └── templates/              # HTML templates
│                   │       └── partials/
│                   └── db.sqlite3                  # SQLite database file (generated)
└── Myproject.zip
```

## Technologies Used

*   **Backend:** Django (Python Web Framework)
*   **Database:** SQLite3 (default, can be configured for PostgreSQL, MySQL, etc.)
*   **Frontend:** HTML, CSS, JavaScript (standard web technologies)
*   **Styling:** Bootstrap (assumed based on common Django project setups and `bootstrap.min.css` in static files)
