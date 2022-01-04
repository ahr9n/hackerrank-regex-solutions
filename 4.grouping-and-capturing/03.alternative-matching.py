Regex_Pattern = r'^((Mr|Mrs|Ms|Dr|Er)\.)([a-zA-Z]+)$'  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
