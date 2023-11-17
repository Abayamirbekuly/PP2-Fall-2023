def delete_file(file_to_delete):
    if(os.path.exists(file_to_delete)):
        if(os.access(file_to_delete, os.W_OK)):
            os.remove(file_to_delete)
        else:
            print("Has no acces to file")
    else:
        print("File does not exist")

file_to_delete = "text.txt"
delete_file(file_to_delete)








    


