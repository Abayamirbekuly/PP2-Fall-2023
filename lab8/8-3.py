def palindrome(input_string):
    cleaned_string = input_string.lower()
    cleaned_string = cleaned_string.replace(" ", "")
    return cleaned_string == cleaned_string[::-1]
user_input = input(": ")
if palindrome(user_input):
    print(" палиндром")
else:
    print(" не палиндром.")
