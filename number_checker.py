import re
import re

def is_valid_contact_number(contact_number):
    pattern = r'^(\+?\d{1,3}[-. ]?)?(\d{1,4}[-. ]?)?\d{1,10}[-. ]?\d{1,10}$'

    if re.match(pattern, contact_number):
        return True
    else:
        return False


# Test cases
numbers = [
    '2124567890',
    '212-456-7890',
    '(212)456-7890',
    '(212)-456-7890',
    '212.456.7890',
    '212 456 7890',
    '+12124567890',
    '+12124567890',
    '+1 212.456.7890',
    '+212-456-7890',
    '1-212-456-7890'
]

for number in numbers:
    if is_valid_contact_number(number):
        print(f'{number} is a valid contact number.')
    else:
        print(f'{number} is an invalid contact number.')
