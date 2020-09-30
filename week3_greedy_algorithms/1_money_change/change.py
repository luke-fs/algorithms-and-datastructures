# Uses python3
import sys

def get_change(m):
    #write your code here
    c = 0
    while m >= 0:
        if m-10 >= 0:
            m -= 10
            c += 1
        elif m-5 >= 0:
            m -= 5
            c += 1
        elif m-1 >= 0:
            m -= 1
            c += 1
        else:
            return c

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = int(input())
    print(get_change(m))
