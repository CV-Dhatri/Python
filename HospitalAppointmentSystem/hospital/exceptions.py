"""
hospital/exceptions.py
Custom exception classes for Hospital Appointment System.
"""

class HospitalAppError(Exception):
    """Base exception for application errors."""
    pass

class PatientNotFoundError(HospitalAppError):
    """Raised when a patient ID does not exist."""
    pass

class DoctorNotFoundError(HospitalAppError):
    """Raised when a doctor ID does not exist or is inactive."""
    pass

class DepartmentNotFoundError(HospitalAppError):
    """Raised when a department ID does not exist."""
    pass

class AppointmentNotFoundError(HospitalAppError):
    """Raised when an appointment ID does not exist."""
    pass

class SlotUnavailableError(HospitalAppError):
    """Raised when a doctor time slot is already booked."""
    pass

class InvalidStatusTransitionError(HospitalAppError):
    """Raised when an appointment or bill status change is invalid."""
    pass

class ValidationError(HospitalAppError):
    """Raised when input validation fails."""
    pass