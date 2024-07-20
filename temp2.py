def sum(numbers):
    result = 0
    for i in numbers:
        result += i
    return result
input_numbers = input()
numbers_list = list(map(int, input_numbers.split()))
re = sum(numbers_list)
print(re)