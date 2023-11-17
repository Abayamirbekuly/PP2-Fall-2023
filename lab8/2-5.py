def write_list_to_file(file_path, my_list):
      with open(file_path, 'w') as file:
        for item in my_list:
                file.write(str(item) + '\n')
        print(file_path)
    


my_list = [1, 2, 3, 4, 5]
file_path = 'output.txt'

write_list_to_file(file_path, my_list)





    


