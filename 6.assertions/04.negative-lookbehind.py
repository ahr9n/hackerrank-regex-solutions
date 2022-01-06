Regex_Pattern = r"(?<![aeiouAEIOU])[\w|\W]"  # Do not delete 'r'.
# r"(?<![aeiouAEIOU])(\w|\W)" and r"(?<![aeiouAEIOU])." are working too ;)

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
