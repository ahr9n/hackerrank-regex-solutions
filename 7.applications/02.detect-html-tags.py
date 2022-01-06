# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

tags = set()


def detect_html(text):
    tag = re.findall(r'<(\w+)', text)
    for i in tag:
        tags.add(i)


if __name__ == '__main__':
    lines = eval(input())
    for _ in range(lines):
        line = input().strip()
        detect_html(line)

    tags = sorted(tags)
    print(';'.join(tags))
