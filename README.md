# 1. Django Course App
This simple Django app provides a platform for online courses with features such as displaying popular courses, detailed course information, and enrollment functionality. Below is an overview of the main components:

## Directory Structure
/viewTemp/: This directory contains Django templates for various views, including the course_list.html template.

## Django Course App - Visual Overview
In this section, we provide a visual overview of the Django Course App. Explore the screenshots below to get a glimpse of the app's interface and key functionalities.

1. Popular Courses List

Displaying the top 2 most popular courses in a list format.

2. Course Details

Details page showcasing information about a specific course.

![django views1](https://github.com/hihassan1998/djangoORMtemp/assets/150392365/9a6e6df4-94f0-44b6-9a67-c9269de18cbb)


3. Enrollment Process

The enrollment process, demonstrating the use of the Enroll button.

![django views2](https://github.com/hihassan1998/djangoORMtemp/assets/150392365/3c9a106e-7fc4-45b8-a09c-f11df38b1c9c)

## Concepts Covered
##  1. SQLite
Description: SQLite is a lightweight relational database management system (RDBMS) that provides an SQL-based interface to store, manage, and retrieve structured data.
## 2. List View
Description: The app utilizes a class-based view to present multiple records in a tabular or list format. This helps in showcasing a list of the top 10 most popular courses.
##  3. HttpResponseRedirect
Description: The HttpResponseRedirect class is used to redirect users to a different page or URL after processing a request. In this app, it is employed after a user enrolls in a course.
## 4. reverse()
Description: The reverse() utility function, provided by Django, is used to dynamically generate URLs. It takes the name of a URL pattern as an argument and returns the corresponding URL as a string. This is particularly useful for maintaining clean and manageable URL configurations.
##  5. CSS Container Class
Description: The app employs a CSS container class to create a responsive fixed-width container for webpage content. This ensures a consistent layout and spacing for content across different screen sizes and devices.
##  6. CSS Card Class
Description: A CSS card class is used to create flexible and stylized containers (cards) for presenting information, images, and actions. This enhances the visual appeal and organization of content in a compact manner.

##  How to Use
1. Clone the repository.

git clone https://github.com/your-username/your-repository.git

2. Install dependencies.

pip install -r requirements.txt

3. Run the Django development server.

python manage.py runserver

Access the application in your web browser at http://127.0.0.1:8000/onlinecourse/.

# 2. Standalone Django ORM Project Template

This project template provides a foundation for creating a standalone Django ORM (Object-Relational Mapping) project along with an app. It is designed to be used as a learning tool and starting point for building more complex Django ORM applications.

## Directory Structure
/ormtemplate/: This directory contains Django basic standalone template 

## Purpose

The main goal of this template is to help you understand and implement key concepts related to Django ORM, PostgreSQL (or Postgres), Psycopg, and database migrations. By using this template, you can explore how Django models map to database tables, work with PostgreSQL as the relational database management system, utilize Psycopg as the interface for PostgreSQL in Django, and manage database schema changes through migrations.

## Concepts Covered

### Django ORM

Django ORM is a powerful component of the Django web application framework. It provides an abstraction layer for interacting with databases, where each Django model corresponds to a database table. This template will guide you in creating and using Django models to define your database schema.

### PostgreSQL (Postgres)

PostgreSQL, often referred to as Postgres, is an open-source relational database management system. Django supports PostgreSQL as one of its database backends. This template is configured to work seamlessly with PostgreSQL, allowing you to leverage its features for efficient data storage and retrieval.

### Psycopg

Psycopg is a PostgreSQL adapter for Python that enables Django to interact with PostgreSQL databases. It serves as the bridge between Django's ORM and the PostgreSQL database backend. You will explore how to set up and configure Psycopg to work with this template.

### Database Migrations

Database migrations are crucial for managing version-controlled, incremental, and reversible changes to relational database schemas. The template includes examples and instructions on how to create, apply, and revert migrations using Django's `manage.py` command-line interface.

### manage.py

Django provides a command-line interface through the `manage.py` script. This template emphasizes the usage of `manage.py` for various tasks, including running the development server, creating database migrations, applying migrations, and other project management tasks.

## Getting Started

To use this template, follow these steps:

1. Clone this repository.
2. Create a virtual environment and install the required dependencies.
3. Configure the database settings in the `settings.py` file.
4. Create your Django models in the `models.py` file.
5. Run initial migrations and apply them to set up the database schema.

Feel free to explore the code, modify it, and build upon it to create your Django ORM projects.

## Credits

Contributing
If you'd like to contribute to the development of this Django app, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and commit them.
4. Push your branch to your fork.
5 .Submit a pull request.

Feel free to customize and extend the app based on your specific requirements!

Happy coding!
