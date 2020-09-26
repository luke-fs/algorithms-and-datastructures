# python3

def max_pairwise_product(numbers):
    max_a = 0
    max_b = 0
    elem = 0
    for i in range(0,len(numbers)):
        if max_a < numbers[i]:
            max_a = numbers[i]
            elem = i
    
    numbers.pop(elem)
    
    for x in numbers:
        if max_b < x:
            max_b = x

    return max_a * max_b

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
