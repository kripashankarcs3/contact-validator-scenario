import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone


def test_is_valid_email_true():
    """Test a well-formed email."""
    # Arrange
    email = "student@lpu.in"

    # Act
    result = is_valid_email(email)

    # Assert
    assert result == True


def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    """Test a well-formed phone number with dashes."""
    # Arrange
    phone = "555-123-4567"

    # Act
    result = is_valid_phone(phone)

    # Assert
    assert result == True


def test_mask_email_basic():
    """Test masking a typical email address."""
    # Arrange
    email = "priya@example.com"

    # Act
    result = mask_email(email)

    # Assert
    assert result == "pr***@example.com"


def test_is_valid_phone_type_error():
    """Test that a non-string phone input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_phone(12345)


def test_mask_email_invalid_value_error():
    """Test masking an invalid email raises ValueError."""
    with pytest.raises(ValueError):
        mask_email("not-an-email")


def test_mask_email_short_local():
    """Test masking an email whose local-part is very short."""
    result = mask_email("a@example.com")
    assert result == "a@example.com"


def test_normalize_phone_valid():
    """Test converting a dashed phone number into digits only."""
    result = normalize_phone("555-123-4567")
    assert result == "5551234567"


def test_normalize_phone_invalid_value_error():
    """Test that an invalid phone raises ValueError."""
    with pytest.raises(ValueError):
        normalize_phone("123")