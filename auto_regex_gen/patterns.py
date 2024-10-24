# auto_regex_gen/patterns.py

patterns = {
    patterns = {
    # Email patterns
    "email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    
    # URL patterns with optional query parameters and fragments
    "url": r'https?://(?:www\.)?[-\w]+(?:\.\w[-\w]*)+[-\w.,@?^=%&:/~+#]*[-\w@?^=%&/~+#]?',
    
    # ISO date format and other common date formats
    "date": r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2})\b',
    
    # Phone numbers: International and local formats with various separators
    "phone": r'(\+?\d{1,4}[\s-])?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}(?:\s*x\s*\d{1,5})?',
    
    # IPv4 address (supports edge cases like leading zeros)
    "ipv4": r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
    
    # IPv6 address (full and compressed forms)
    "ipv6": r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}|\b(?:[A-Fa-f0-9]{1,4}:){1,7}:|\b:(:[A-Fa-f0-9]{1,4}){1,7}\b',
    
    # U.S. Zipcode with optional +4 extension
    "zipcode": r'\b\d{5}(?:-\d{4})?\b',

    # SSN (Social Security Number, U.S. format)
    "ssn": r'\b\d{3}-\d{2}-\d{4}\b',

    # MAC address (supports colon and dash-separated formats)
    "mac_address": r'\b([A-Fa-f0-9]{2}[:\-]){5}[A-Fa-f0-9]{2}\b',
    
    # Credit card numbers (Visa, MasterCard, AMEX, etc.)
    "credit_card": r'\b(?:\d[ -]*?){13,19}\b',
    
    # Hexadecimal color code
    "hex_color": r'\b#(?:[0-9a-fA-F]{3}){1,2}\b',
    
    # UUID (Universally Unique Identifier) patterns
    "uuid": r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b',
    
    # File path (for Unix-like and Windows systems)
    "file_path": r'([a-zA-Z]:[\\/]|~[\\/])(?:[\w\s-]+[\\/])+[\w\s.-]+',
    
    # Time (24-hour or 12-hour clock with optional AM/PM)
    "time": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b',
    
    # Currency (general pattern for dollar, euro, pound, yen)
    "currency": r'\b(?:\$|€|£|¥)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b',
    
    # HTML tags (basic tag matching, not perfect for nested tags)
    "html_tag": r'<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\/>)',
    
    # Hashtags (for social media platforms)
    "hashtag": r'\B#\w\w+',
    
    # Twitter handles
    "twitter_handle": r'\B@\w{1,15}\b',

    # Postal code (international generic pattern)
    "postal_code": r'\b[A-Za-z0-9]{3,10}[-\s]?[A-Za-z0-9]{3,10}\b',

    # IP address (generic IPv4 and IPv6 combined)
    "ip_address": r'\b(?:\d{1,3}\.){3}\d{1,3}|\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b',
    
    # Base64 strings
    "base64": r'\b[A-Za-z0-9+/]{4,}(?:==|=)?\b',
    
    # Binary strings (e.g., "1101" or "0b10101")
    "binary_string": r'\b(0b)?[01]+\b',
    
    # SHA-256 hash
    "sha256": r'\b[A-Fa-f0-9]{64}\b',
    
    # MD5 hash
    "md5": r'\b[A-Fa-f0-9]{32}\b',

    # Ethereum address
    "ethereum_address": r'\b0x[a-fA-F0-9]{40}\b',

    # Bitcoin address (P2PKH and P2SH formats)
    "bitcoin_address": r'\b(1[1-9A-HJ-NP-Za-km-z]{25,34}|3[1-9A-HJ-NP-Za-km-z]{25,34})\b'
}

def get_patterns():
    return patterns
