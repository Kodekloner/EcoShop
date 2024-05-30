# EcoShop

EcoShop is a web application built with Django, designed to help users find and purchase eco-friendly products. This README will guide you through the process of setting up and running the EcoShop project on your local machine.

## Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python 3.8 or later
- pip (Python package installer)
- Git
- Virtualenv (optional, but recommended)

## Installation

### Clone the Repository
First, clone the repository to your local machine using Git:
```bash
git clone https://github.com/Kodekloner/EcoShop.git
cd EcoShop
```

### Set Up Virtual Environment
It is recommended to use a virtual environment to manage your dependencies. Create and activate a virtual environment using the following commands:
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
With the virtual environment activated, install the required dependencies:
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
Create a .env file in the project root directory and add the following configurations:
```bash
DEBUG=True
SECRET_KEY=your_secret_key
```

### Run Migrations
Apply the database migrations to set up your database schema:
```bash
python manage.py migrate
```

### Create a Superuser
Create a superuser to access the Django admin interface:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the superuser account


## Running the Project
To run the development server, use the following command:
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your web browser to see the application running.
