import string

def is_palindrome(s):
    # Remove spaces, punctuation, and convert to lowercase
    clean_string = ''.join(char for char in s if char.isalnum()).lower()
    # Check if the cleaned string is equal to its reverse
    return clean_string == clean_string[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama!"))  # Output: True
print(is_palindrome("Race car"))  # Output: True
print(is_palindrome("Hello, World!"))  # Output: False
