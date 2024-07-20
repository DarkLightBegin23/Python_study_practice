def sum(numbers):
    result = 0
    for i in numbers:
        result += i
    return result
input_numbers = input()  # 일단 str 형식으로 받아서
numbers_list = list(map(int, input_numbers.split()))  # 
re = sum(numbers_list)
print(re)