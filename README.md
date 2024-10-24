Sure! Here's a comprehensive and detailed documentation for the **AutoRegexGen** Python library, including explanations, usage examples, pattern descriptions, and future improvements.

---

# AutoRegexGen: In-Depth Documentation

### Overview

**AutoRegexGen** is a Python library that automatically generates regular expression (regex) patterns based on plain English descriptions. It is designed to help developers quickly generate complex regex patterns for common use cases like emails, URLs, phone numbers, IP addresses, and more, without needing to manually write or memorize regex syntax.

### Key Features

- **Human-readable input**: Converts natural language descriptions into regex patterns.
- **Comprehensive regex library**: Covers common patterns like emails, URLs, phone numbers, IP addresses, UUIDs, credit card numbers, and more.
- **Flexible usage**: Can be used as a library or in command-line utilities for quick regex generation.
- **Extendable**: New patterns can be easily added to the core dictionary for additional use cases.

---

## Installation

### Install from Local Environment

To install AutoRegexGen from a local environment:

1. Clone or download the project repository.
2. Navigate to the project root directory where `setup.py` is located.
3. Run the following command to install the package locally:

```bash
pip install .
```

### Install from PyPI (Planned Future Support)

Once the library is published to PyPI (Python Package Index), you can install it using:

```bash
pip install auto_regex_gen
```

---

## Usage

### Basic Example

After installation, you can start using the library by importing the `auto_regex_gen` function and providing a description:

```python
from auto_regex_gen import auto_regex_gen

description = "I want to find all email addresses"
regex = auto_regex_gen(description)
print(f"Generated Regex: {regex}")
```

**Output**:
```
Generated Regex: [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
```

### Command-Line Usage

You can use the library as a simple command-line tool if desired:

```bash
python -m auto_regex_gen "find an ipv4 address"
```

This will return the regex pattern that matches the description.

---

## Supported Patterns

### 1. Email

- **Pattern**: `r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'`
- **Description**: Matches email addresses, e.g., `example@example.com`.

### 2. URL

- **Pattern**: `r'https?://(?:www\.)?[-\w]+(?:\.\w[-\w]*)+[-\w.,@?^=%&:/~+#]*[-\w@?^=%&/~+#]?'`
- **Description**: Matches URLs with optional query parameters, fragments, and subdomains, e.g., `https://www.example.com/path?query=1#fragment`.

### 3. Date

- **Pattern**: `r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2})\b'`
- **Description**: Matches various date formats, including `MM/DD/YYYY`, `DD-MM-YYYY`, and ISO formats like `YYYY-MM-DD`.

### 4. Phone Number

- **Pattern**: `r'(\+?\d{1,4}[\s-])?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}(?:\s*x\s*\d{1,5})?'`
- **Description**: Matches phone numbers in both international and local formats, with optional area codes and extensions.

### 5. IPv4 Address

- **Pattern**: `r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'`
- **Description**: Matches standard IPv4 addresses, e.g., `192.168.1.1`.

### 6. IPv6 Address

- **Pattern**: `r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}|\b(?:[A-Fa-f0-9]{1,4}:){1,7}:|\b:(:[A-Fa-f0-9]{1,4}){1,7}\b'`
- **Description**: Matches both full and compressed IPv6 addresses, e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.

### 7. ZIP Code

- **Pattern**: `r'\b\d{5}(?:-\d{4})?\b'`
- **Description**: Matches U.S. ZIP codes, including optional `+4` extensions, e.g., `12345` or `12345-6789`.

### 8. Social Security Number (SSN)

- **Pattern**: `r'\b\d{3}-\d{2}-\d{4}\b'`
- **Description**: Matches U.S. Social Security numbers in the format `123-45-6789`.

### 9. MAC Address

- **Pattern**: `r'\b([A-Fa-f0-9]{2}[:\-]){5}[A-Fa-f0-9]{2}\b'`
- **Description**: Matches MAC addresses in both colon and dash-separated formats, e.g., `00:1A:2B:3C:4D:5E`.

### 10. Credit Card Number

- **Pattern**: `r'\b(?:\d[ -]*?){13,19}\b'`
- **Description**: Matches common credit card numbers, including Visa, MasterCard, and American Express, with or without spaces/dashes.

### 11. Hexadecimal Color Code

- **Pattern**: `r'\b#(?:[0-9a-fA-F]{3}){1,2}\b'`
- **Description**: Matches hex color codes used in web development, e.g., `#FFF` or `#FFFFFF`.

### 12. UUID (Universally Unique Identifier)

- **Pattern**: `r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b'`
- **Description**: Matches UUIDs in the format `550e8400-e29b-41d4-a716-446655440000`.

### 13. File Path

- **Pattern**: `r'([a-zA-Z]:[\\/]|~[\\/])(?:[\w\s-]+[\\/])+[\w\s.-]+'`
- **Description**: Matches file paths for both Windows and Unix-like systems, e.g., `C:\Users\Name\file.txt` or `/home/user/file.txt`.

### 14. Time (24-hour and 12-hour Clock)

- **Pattern**: `r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'`
- **Description**: Matches times in 24-hour and 12-hour formats with optional AM/PM, e.g., `14:30`, `7:45 PM`.

### 15. Bitcoin Address

- **Pattern**: `r'\b(1[1-9A-HJ-NP-Za-km-z]{25,34}|3[1-9A-HJ-NP-Za-km-z]{25,34})\b'`
- **Description**: Matches Bitcoin addresses in P2PKH and P2SH formats.

---

## Advanced Usage

### Custom Pattern Addition

You can easily extend the library by adding new patterns to the `patterns.py` file. For example, to add a pattern for matching VIN (Vehicle Identification Number) codes:

1. Open `patterns.py`.
2. Add a new entry in the dictionary:

```python
patterns['vin'] = r'\b[A-HJ-NPR-Z0-9]{17}\b'
```

3. Use it in the `auto_regex_gen` function:

```python
description = "match a vehicle identification number (VIN)"
regex = auto_regex_gen(description)
print(f"Generated Regex: {regex}")
```

---

## Extensibility and Future Enhancements

### NLP Integration

Currently, the library uses keyword matching to map descriptions to regex patterns. Future improvements could involve integrating an NLP library such as `spaCy` or `nltk` to allow for more flexible descriptions. For example, "Find email addresses" and "Extract emails from text" would both trigger the email regex.

### Support for Multiple Patterns

You could enhance the library to detect and return multiple regex patterns for more complex descriptions, such as:

```python
description = "find both emails and phone numbers"
regex = auto_regex_gen(description)
print(f"Generated Regex: {regex}")
```

**Output**:
```
Generated Regex:
Email: [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
Phone: (\+?\d{1,4}[\s-])?(\(?\d{

3}\)?[\s-]?)?\d{3}[\s-]?\d{4}(?:\s*x\s*\d{1,5})?
```

---

## Contributing

We welcome contributions! If you would like to add new patterns, optimize regex performance, or improve natural language handling, please feel free to submit a pull request or open an issue in the GitHub repository.

---

## License

**AutoRegexGen** is licensed under the GPL License. See `LICENSE` file for more information.

---

With this documentation, you should now be able to use **AutoRegexGen** effectively in your projects. Would you like to explore some advanced features, or need any specific help with using it?
