"""
This simple Python project is using 'random' and 'string' package to generate a random string of a given
length.
"""

import random
import string

# total = string.ascii_letters + string.digits + string.punctuation
# length = 16
# password = ''.join(random.sample(total, length))
# print(password)

# or

total = string.ascii_letters + string.digits
length = 16
password = ''.join(random.sample(total, length))
print(password)
