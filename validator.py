import re

def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС."""
    pattern = r'^\d{3}-\d{3}-\d{3} \d{2}$'
    return bool(re.match(pattern, snils))

def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))
