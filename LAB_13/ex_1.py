"""
Laboratory Work #13: Regular Expressions in Python
Student: [Your Name]
Group: [Your Group]
Date: 2026
"""

import re

# ============================================================
# BASIC FUNCTIONS DEMONSTRATION
# ============================================================

print("=" * 60)
print("BASIC REGEX FUNCTIONS")
print("=" * 60)

# 1. re.search() - Find pattern anywhere in string
sample_text = "The rain in Spain falls mainly on the plain."
search_pattern = r"Spain"

search_result = re.search(search_pattern, sample_text)
print("1. re.search() example:")
if search_result:
    print(f"   Found: '{search_result.group()}'")
else:
    print("   Not found")
print()

# 2. re.match() - Find pattern only at the beginning
first_text = "Hello, world!"
second_text = "Greetings! Hello there!"
match_pattern = r"Hello"

match_result1 = re.match(match_pattern, first_text)
match_result2 = re.match(match_pattern, second_text)

print("2. re.match() example:")
print(f"   Text: '{first_text}' - Match at beginning: {bool(match_result1)}")
print(f"   Text: '{second_text}' - Match at beginning: {bool(match_result2)}")
print()

# 3. re.findall() - Find all occurrences
contact_text = "John: 555-1234, Mary: 555-5678, Bob: 555-9999"
find_pattern = r"\d{3}-\d{4}"

all_matches = re.findall(find_pattern, contact_text)
print("3. re.findall() example:")
print(f"   All phone numbers: {all_matches}")
print()

# 4. re.sub() - Replace patterns
original = "My numbers: 123, 4567, 89"
replace_pattern = r"\d+"
modified = re.sub(replace_pattern, "DIGIT", original)

print("4. re.sub() example:")
print(f"   Original: '{original}'")
print(f"   Modified: '{modified}'")
print()

# 5. Case-insensitive search
case_text = "I love PYTHON programming and python is great"
case_pattern = r"python"
case_result = re.search(case_pattern, case_text, re.IGNORECASE)

print("5. Case-insensitive search (re.IGNORECASE):")
print(f"   Found: '{case_result.group()}'")
print("-" * 60)


# ============================================================
# LAB EXERCISE 1: Finding Phone Numbers
# ============================================================

print("\n" + "=" * 60)
print("LAB EXERCISE 1: Finding Phone Numbers")
print("=" * 60)

phone_text = "Call me at 555-1234 or at the office line 555-5678. For emergencies, dial 555-9999."
phone_pattern = r"\d{3}-\d{4}"

found_phones = re.findall(phone_pattern, phone_text)
print(f"Input text: {phone_text}")
print(f"Phone Numbers Found: {found_phones}")
print("-" * 60)


# ============================================================
# LAB EXERCISE 2: Matching at the Start of a String
# ============================================================

print("\n" + "=" * 60)
print("LAB EXERCISE 2: Matching at the Start of a String")
print("=" * 60)

string_a = "Hello, world! Welcome to regex."
string_b = "Greetings! Hello, how are you?"
hello_pattern = r"Hello"

print(f"Text 1: '{string_a}'")
print(f"Text 2: '{string_b}'")
print()

# Using re.match()
match_a = re.match(hello_pattern, string_a)
match_b = re.match(hello_pattern, string_b)

print("Using re.match():")
print(f"   Text 1: {'Match found: ' + match_a.group() if match_a else 'No match'}")
print(f"   Text 2: {'Match found: ' + match_b.group() if match_b else 'No match'}")
print()

# Using re.search()
search_a = re.search(hello_pattern, string_a)
search_b = re.search(hello_pattern, string_b)

print("Using re.search():")
print(f"   Text 1: {'Found: ' + search_a.group() if search_a else 'Not found'}")
print(f"   Text 2: {'Found: ' + search_b.group() if search_b else 'Not found'}")
print("-" * 60)


# ============================================================
# LAB EXERCISE 3: Replacing Numbers with a Word
# ============================================================

print("\n" + "=" * 60)
print("LAB EXERCISE 3: Replacing Numbers with a Word")
print("=" * 60)

fruit_text = "There are 3 apples, 15 oranges, and 256 bananas in the basket."
number_pattern = r"\d+"

replaced_text = re.sub(number_pattern, "NUMBER", fruit_text)
print(f"Original: {fruit_text}")
print(f"Modified: {replaced_text}")
print("-" * 60)


# ============================================================
# LAB EXERCISE 4: Extracting Email Addresses
# ============================================================

print("\n" + "=" * 60)
print("LAB EXERCISE 4: Extracting Email Addresses")
print("=" * 60)

email_text = "For more info, contact us at support@example.com or sales-info@example.org."
email_pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"

extracted_emails = re.findall(email_pattern, email_text)
print(f"Input: {email_text}")
print(f"Email Addresses Found: {extracted_emails}")
print("-" * 60)


# ============================================================
# LAB EXERCISE 5: Finding Words that Start with a Vowel
# ============================================================

print("\n" + "=" * 60)
print("LAB EXERCISE 5: Words Starting with Vowels")
print("=" * 60)

vowel_text = "An apple a day keeps the doctor away. Even elephants enjoy eating."
vowel_pattern = r"\b[aeiou]\w*\b"

vowel_words = re.findall(vowel_pattern, vowel_text, re.IGNORECASE)
print(f"Text: {vowel_text}")
print(f"Words starting with a vowel: {vowel_words}")
print("-" * 60)


# ============================================================
# ADDITIONAL EXAMPLES
# ============================================================

print("\n" + "=" * 60)
print("ADDITIONAL REGEX EXAMPLES")
print("=" * 60)

# Example 1: Extract all digits
sample = "Order #123: 5 items, total $45.67"
digits = re.findall(r"\d+", sample)
print(f"1. Extract digits: {digits}")

# Example 2: Split text by multiple spaces or punctuation
message = "Hello:world;how are you"
split_result = re.split(r"[;:\s]+", message)
print(f"2. Split by punctuation/spaces: {split_result}")

# Example 3: Validate simple email format
test_emails = ["user@example.com", "invalid-email", "name@domain.org"]
print("3. Email validation:")
for email in test_emails:
    validator = r"^[\w.-]+@[\w.-]+\.\w+$"
    is_valid = bool(re.match(validator, email))
    print(f"   {email}: {'Valid' if is_valid else 'Invalid'}")

# Example 4: Find words of specific length
sentence = "The cat sat on the mat with a hat"
four_letter = re.findall(r"\b\w{3}\b", sentence)
print(f"4. Three-letter words: {four_letter}")

# Example 5: Extract URLs
web_text = "Visit https://python.org or http://example.com for more info"
url_pattern = r"https?://[\w.]+"
urls = re.findall(url_pattern, web_text)
print(f"5. URLs found: {urls}")
print("-" * 60)


# ============================================================
# PRACTICAL APPLICATION: Data Cleaning
# ============================================================

print("\n" + "=" * 60)
print("PRACTICAL APPLICATION: Data Cleaning")
print("=" * 60)

dirty_data = "Contact: (555) 123-4567, Email: USER@EXAMPLE.COM, Age: 25 years"
print(f"Original: {dirty_data}")

# Clean phone number
phone_clean = re.sub(r"[()\s-]", "", dirty_data)
phone_match = re.search(r"\d{10}", phone_clean)
clean_phone = phone_match.group() if phone_match else "Not found"

# Normalize email
email_match = re.search(r"[\w.]+@[\w.]+", dirty_data, re.IGNORECASE)
clean_email = email_match.group().lower() if email_match else "Not found"

# Extract age
age_match = re.search(r"\d+", dirty_data)
clean_age = age_match.group() if age_match else "Not found"

print(f"Cleaned phone: {clean_phone}")
print(f"Normalized email: {clean_email}")
print(f"Extracted age: {clean_age}")
print("=" * 60)


# ============================================================
# REGEX PATTERN SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("REGEX PATTERN SUMMARY")
print("=" * 60)

patterns = {
    r"\d": "Any digit (0-9)",
    r"\w": "Word character (a-z, A-Z, 0-9, _)",
    r"\s": "Whitespace (space, tab, newline)",
    r".": "Any character except newline",
    r"^": "Start of string",
    r"$": "End of string",
    r"*": "0 or more repetitions",
    r"+": "1 or more repetitions",
    r"?": "0 or 1 repetition",
    r"{3}": "Exactly 3 repetitions",
    r"{2,4}": "Between 2 and 4 repetitions",
    r"[aeiou]": "Any character in set",
    r"[^0-9]": "Any character NOT in set",
    r"|": "OR operator",
    r"()": "Grouping",
    r"\b": "Word boundary"
}

print("Common regex patterns:")
for pattern, description in patterns.items():
    print(f"   {pattern:8} - {description}")

print("\n" + "=" * 60)
print("LAB WORK COMPLETED SUCCESSFULLY")
print("=" * 60)