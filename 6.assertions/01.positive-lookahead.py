Regex_Pattern = r'o(?=o{2})'  # Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
