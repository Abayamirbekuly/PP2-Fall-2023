def copy_path2_in_path1(path1,path2):
    with open(path2,'r') as path2:
        file = path2.read()
        
    with open(path1, 'w') as res_file:
        res_file.write(file)
    print(res_file)
path1 = "path.txt"
path2 = "path2.txt"
copy_path2_in_path1(path1,path2)








    


