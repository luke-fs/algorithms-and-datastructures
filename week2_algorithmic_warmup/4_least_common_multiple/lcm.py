# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_euclid_modern(a, b):
    while b != 0:
        h = a%b
        a = b
        b = h
    return a

def lcm_luke(a, b):
    return int((a*b)/gcd_euclid_modern(a,b))
    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_luke(a, b))

