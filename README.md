# Patient-management-system
This system is meant to manage patient records, schedule appointments with specialists, track patient visits and prescriptions
### Set up
Create a virtual environment and install Pipenv.
- pipenv install
- pipenv install sqlalchemy
- pipenv install click
- pipenv install pytest
- pipenv shell

### Models Directory
contains the following files:
1. __init__ -   is used to initialize the pyton package. it contains import statements.
2. **Models_init.py** - is used for setting up the database connection and configuration. It has the code for creating the database engine, defining base class and provides a function to initialize the database.
3. **patient.py** - Deals with the patients data like creating patients tables.
4. **appointment.py** - Deals with the appointments made for various patients .
5. **specialist.py** - Contains the doctors' details.
6. **department.py** - Has details on the different departments

### Command Line Interface
The CLI provides a user-friendly way to interact with the hospital management system directly from the command line, allowing you to initialize the database and add patients, specialists,departments and appointments efficiently.