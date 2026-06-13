import re


def extract_valid_ips(text_block):
    """
    Scans a block of text and returns a list of valid IPv4 addresses.
    """
    # A basic Regex pattern for an IPv4 address.
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    # Find all matches in the text
    potential_ips = re.findall(ip_pattern, text_block)

    valid_ips = []
    for ip in potential_ips:
        # Extra validation: ensure each octet is between 0 and 255
        octets = ip.split('.')
        if all(0 <= int(octet) <= 255 for octet in octets):
            valid_ips.append(ip)

    return valid_ips