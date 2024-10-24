# auto_regex_gen/patterns.py

patterns = {
    "email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    "url": r'https?://(?:www\.)?[-\w]+(?:\.\w[-\w]*)+',
    "date": r'\b\d{1,2}/\d{1,2}/\d{4}\b',
    "phone": r'\+?\d[\d -]{8,12}\d',
    "ipv4": r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    "ipv6": r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b',
    "zipcode": r'\b\d{5}(?:-\d{4})?\b'
}

def get_patterns():
    return patterns
