import re

def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    pattern = r'^\+?7\d{10}$'
    return bool(re.match(pattern, phone.replace('-', '').replace(' ', '')))

def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))
