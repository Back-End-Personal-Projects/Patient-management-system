from lib.models.__init__ import init_db
from lib.cli import cli

def main():
    """Main entry point for the application."""
    try:
        init_db()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing the database: {e}")
        return  
    cli()  

if __name__ == '__main__':
    main()
