# Uses python3
import sys

def calc_fib(n):
    if (n <= 1):
        return n

    f = []
    f.append(0)
    f.append(1)

    for i in range(2,n+1):
        f.append((f[i-2] + f[i-1])%10)
   
    return f[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(calc_fib(n))
