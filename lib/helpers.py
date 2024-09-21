from datetime import datetime

def format_date(date: datetime) -> str:
    """Format a datetime object to a readable string."""
    return date.strftime("%Y-%m-%d %H:%M")

def validate_patient_age(age: int) -> bool:
    """Validate the age of a patient."""
    return 0 < age < 120  # Example age validation

def validate_appointment_time(appointment_time: str) -> bool:
    """Validate the appointment time format (YYYY-MM-DD HH:MM)."""
    try:
        datetime.strptime(appointment_time, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False
