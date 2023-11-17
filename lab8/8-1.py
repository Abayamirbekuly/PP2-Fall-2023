def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

my_list =list(map(int, input(":" ).split()))
result = multiply(my_list)
print(result)
