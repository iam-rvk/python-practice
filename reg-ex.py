import re

text = "My email is test123@example.com"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

match = re.search(pattern, text)

if match:
    print("Email found:", match.group())
else:
    print("No email found")
