# AutoRegexGen

AutoRegexGen is a simple Python library that generates regular expression patterns from plain English descriptions.

Usage

python

from auto_regex_gen import auto_regex_gen

description = "I want to match an email address"
regex = auto_regex_gen(description)
print(f"Generated Regex: {regex}")


### Installing and Using the Library Locally

1. Save the project structure as outlined above.
2. Navigate to the root directory (where `setup.py` is) and run:



This will install the package locally so you can import it anywhere in your projects.
Step 5: Example Usage

Once installed, you can use the library like this:

###

python

from auto_regex_gen import auto_regex_gen

description = "Find all email addresses and URLs"
regex = auto_regex_gen(description)
print(f"Generated Regex: {regex}")
