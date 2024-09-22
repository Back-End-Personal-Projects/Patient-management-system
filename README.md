# Patient-management-system
This system is meant to manage patient records, schedule appointments with specialists, track patient visits and prescriptions
### Set up
Create a virtual environment and install Pipenv.
- pipenv install
- pipenv install sqlalchemy
- pipenv install click
- pipenv install pytest
- pipenv shell

### Migrations
They are used to manage changes in the database. Alembic is used for migrations.
1. This command initializes a new migration repository. It creates the necessary directory structure and files for managing database migrations in a project.
    # alembic init migration *

2. Create Initial Migration: To generate the initial migration files, run:
 * alembic revision --autogenerate -m "Initial migration" *

3. Apply Migrations: After creating migration files, apply the migrations to your database:
    * alembic upgrade head *

### Models Directory
contains the following files:
1. __init__ -   is used to initialize the pyton package. it contains import statements.
2. **__init__.py** - is used for setting up the database connection and configuration. It has the code for creating the database engine, defining base class and provides a function to initialize the database.
3. **patient.py** - Deals with the patients data like creating patients tables.
4. **appointment.py** - Deals with the appointments made for various patients .
5. **specialist.py** - Contains the doctors' details.
6. **department.py** - Has details on the different departments

### Command Line Interface
The CLI provides a user-friendly way to interact with the hospital management system directly from the command line, allowing you to initialize the database and add patients, specialists,departments and appointments efficiently.

### Helpers.py
The helpers.py file contains utility functions that support various operations within the application. It includes functions that are used across multiple files, reducing code duplication. Examples might include formatting dates, validating input, or constructing database queries.

### Seed.py
The seed.py file is used to populate the database with initial data. It includes scripts to insert sample or default data into the database, which can be useful for development and testing purposes.


