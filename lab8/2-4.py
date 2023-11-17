file_path_to_count = r'C:\Users\Daniyar\Desktop\Ответики.txt'

with open(file_path_to_count, 'r', encoding="utf-8") as file:
    line_count = sum(1 for line in file)

print(f"The number of lines in the file '{file_path_to_count}' is: {line_count}")




    


