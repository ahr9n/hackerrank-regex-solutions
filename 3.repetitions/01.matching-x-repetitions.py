Regex_Pattern = r'^[a-zA-Z0-8-2]{40}[\s1-9-2]{5}$'  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
