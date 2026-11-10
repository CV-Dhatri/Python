
import re
from datetime import datetime
from hospital.exceptions import ValidationError

def validate_phone(phone: str) -> str:
    cleaned = phone.strip()
    if not re.fullmatch(r"^[6-9]\d{9}$", cleaned):
        raise ValidationError("Phone number must be a valid 10-digit Indian mobile number (starts with 6-9).")
    return cleaned

def validate_date(date_str: str, allow_past: bool = True) -> str:
    try:
        parsed_date = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError("Invalid date format. Expected format: YYYY-MM-DD.")
    
    if not allow_past and parsed_date < datetime.today().date():
        raise ValidationError("Date cannot be in the past.")
        
    return parsed_date.strftime("%Y-%m-%d")

def validate_gender(gender_str: str) -> str:
    cleaned = gender_str.strip().capitalize()
    valid_genders = ["Male", "Female", "Other"]
    if cleaned not in valid_genders:
        raise ValidationError(f"Invalid gender. Allowed: {', '.join(valid_genders)}")
    return cleaned

def validate_blood_group(bg_str: str) -> str:
    cleaned = bg_str.strip().upper()
    valid_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    if cleaned not in valid_groups:
        raise ValidationError(f"Invalid blood group. Allowed: {', '.join(valid_groups)}")
    return cleaned