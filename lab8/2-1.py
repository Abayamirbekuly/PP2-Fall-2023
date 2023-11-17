def list_directories(path):
    print("Directories:")
    for dir_name in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir_name)):
            print(dir_name)

def list_files(path):
    print("\nFiles:")
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            print(file_name)

def list_all_contents(path):
    print("\nAll Directories and Files:")
    for item_name in os.listdir(path):
        item_path = os.path.join(path, item_name)
        print(item_name, "(Directory)" if os.path.isdir(item_path) else "(File)")

specified_path = 'C:\\Users\\Daniyar\\Desktop\\pp2'

list_directories(specified_path)

list_files(specified_path)

list_all_contents(specified_path)

