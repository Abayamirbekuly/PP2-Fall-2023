def check(elements):
    return all(elements)

def main():
    
    elements_str = input("True False True): ")
    elements = tuple(map(str.capitalize, elements_str.split()))  
    try:
        
        result = check(elements)
        print("true: ", result )
    except ValueError:
        print("Invalid input. ")

if __name__ == "__main__":
    main()

