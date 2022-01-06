# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


def check(text):
    if bool(re.search('^[_\.]\d+[a-zA-Z]*_?$', text)) is True:
        print('VALID')
    else:
        print('INVALID')


if __name__ == '__main__':
    n = eval(input())
    for _ in range(n):
        check(input())
