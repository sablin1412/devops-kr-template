from validator import validate_email

def test_validate_email():
    assert validate_email("test@example.com") == True

def test_validate_phone():
    assert validate_phone("+79991234567") == True
    assert validate_phone("89991234567") == False
    assert validate_phone("+7999123") == False
