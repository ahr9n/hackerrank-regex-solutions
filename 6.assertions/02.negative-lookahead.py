Regex_Pattern = r"(\w|\W)(?!\1)"  # Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
