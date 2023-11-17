def check_path_exists(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exist.")

path_to_check = r"C:\Users\Daniyar\Desktop\pp2"

check_path_exists(path_to_check)


    


