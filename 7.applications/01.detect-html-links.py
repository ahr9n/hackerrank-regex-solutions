# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


def detect_html(text):
    link = re.findall(r'<a href="([^"]*)"', text)
    name = re.findall(r'<a .+?>(\s*)?([^<>]*?)</\w+>', text)

    for i in range(len(link)):
        print("{},{}".format(link[i].strip(), name[i][1].strip()))


if __name__ == '__main__':
    lines = eval(input())
    for _ in range(lines):
        line = input().strip()
        detect_html(line)
