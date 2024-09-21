from models.models_init import init_db
from lib.cli import cli

def main():
    """Main entry point for the application."""
    init_db() 
    cli()  

if __name__ == '__main__':
    main()
