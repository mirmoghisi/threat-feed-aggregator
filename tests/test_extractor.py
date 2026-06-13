from src.extractor import extract_valid_ips


def test_valid_ips_are_extracted():
    # Arrange
    text = "The malicious server is located at 192.168.1.15 and also 10.0.0.5."

    # Act
    result = extract_valid_ips(text)

    # Assert
    assert result == ['192.168.1.15', '10.0.0.5']


def test_invalid_ips_are_ignored():
    # Arrange: 999 is not a valid IP octet
    text = "Ignore this fake IP 999.999.999.999 and this typo 192.168.1.999."

    # Act
    result = extract_valid_ips(text)

    # Assert
    assert result == []


def test_text_without_ips_returns_empty():
    text = "There are no IP addresses in this sentence."
    assert extract_valid_ips(text) == []