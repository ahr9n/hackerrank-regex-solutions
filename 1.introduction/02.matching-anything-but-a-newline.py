regex_pattern = r"...\....\....\....$"  # Do not delete 'r'.
# also, could be: regex_pattern = r".{3}\.{1}.{3}\.{1}.{3}\.{1}.{3}$"

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
