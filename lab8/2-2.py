def check_path_access(path):
    # Check if the path exists
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    # Check readability
    if os.access(path, os.R_OK):
        print(f"Read access to '{path}' is allowed.")
    else:
        print(f"No read access to '{path}'.")

    # Check writability
    if os.access(path, os.W_OK):
        print(f"Write access to '{path}' is allowed.")
    else:
        print(f"No write access to '{path}'.")

    # Check executability
    if os.access(path, os.X_OK):
        print(f"Execute access to '{path}' is allowed.")
    else:
        print(f"No execute access to '{path}'.")


path_to_check = input("Enter the path: ")
check_path_access(path_to_check)
    


