import re

print("REGULAR EXPRESSIONS LABORATORY")
print("=" * 40)

# Exercise 1: Finding Phone Numbers
text1 = "Call me at 555-1234 or office 555-5678. Emergency: 555-9999."
phones = re.findall(r"\d{3}-\d{4}", text1)
print("\n1. Phone Numbers:")
print(f"   Input: {text1}")
print(f"   Found: {phones}")

# Exercise 2: Matching at Start
text2a = "Hello, world! Welcome."
text2b = "Greetings! Hello there."
pattern = r"Hello"

print("\n2. String Start Matching:")
print(f"   re.match('Hello', '{text2a}'): {bool(re.match(pattern, text2a))}")
print(f"   re.match('Hello', '{text2b}'): {bool(re.match(pattern, text2b))}")
print(f"   re.search('Hello', '{text2b}'): {bool(re.search(pattern, text2b))}")

# Exercise 3: Replacing Numbers
text3 = "There are 3 apples, 15 oranges, and 256 bananas."
result3 = re.sub(r"\d+", "NUMBER", text3)
print("\n3. Number Replacement:")
print(f"   Original: {text3}")
print(f"   Modified: {result3}")

# Exercise 4: Extracting Email Addresses
text4 = "Contact support@example.com or sales-info@example.org for help."
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text4)
print("\n4. Email Extraction:")
print(f"   Found: {emails}")

# Exercise 5: Words Starting with Vowels
text5 = "An apple a day keeps the doctor away. Even elephants enjoy eating."
vowel_words = re.findall(r"\b[aeiou]\w*\b", text5, re.IGNORECASE)
print("\n5. Words Starting with Vowels:")
print(f"   Text: {text5}")
print(f"   Result: {vowel_words}")