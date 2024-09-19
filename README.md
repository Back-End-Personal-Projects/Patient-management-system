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