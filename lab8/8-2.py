def count(input_string):
    upper_count = 0
    lower_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print(upper_count)
    print(lower_count)
user_input = input("Введите строку: ")
count(user_input)
