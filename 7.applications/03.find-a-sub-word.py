# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

lines = []
dictionary = {}


def detect_sub_word():
    for line in lines:
        sub = re.findall(r'(?<=\w)%s(?=\w)' % query, line)
        dictionary[query] += len(sub)


if __name__ == '__main__':
    n = eval(input())
    for _ in range(n):
        line = ' ' + input() + ' '
        lines.append(line)

    q = eval(input())
    for _ in range(q):
        query = input()
        if query not in dictionary:
            dictionary[query] = 0
            detect_sub_word()
        print(dictionary[query])
