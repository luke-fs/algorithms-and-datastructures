# python3
import numpy as np
import random

def max_pairwise_product(numbers):
    max_a = 0
    max_b = 0

    for i in numbers:
        if max_a < i:
            max_a = i
            numbers.pop(i)
    
    for x in numbers:
        if max_b < x:
            max_b = x

    return max_a * max_b

def max_pairwise_product_true(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    #input_n = int(input())
    #input_numbers = [int(x) for x in input().split()]

    failed = []
    x=10000000
    while x>0:
        amount = random.randint(2,5)
        input_numbers = np.random.randint(0,200001,amount)

        if max_pairwise_product(input_numbers) == max_pairwise_product_true(input_numbers):
            #print('OK ' + str(x))
            pass
        else:
            print('Amount: '+ str(amount))
            print('Input_Numbers: ' + str(input_numbers))
            failed.append(amount)
        x -= 1
    print(failed)
    #print(max_pairwise_product(input_numbers))
    