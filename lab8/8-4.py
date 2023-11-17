
import math
import time

def calculate_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000.0)  
    result = math.sqrt(number)
    return result

def main():
    number = float(input(" number: "))
    delay_milliseconds = int(input("Enter the delay in milliseconds: "))
    result = calculate_square_root(number, delay_milliseconds)
    print(f"Square root of {number} after {delay_milliseconds} milliseconds is {result}")
if __name__ == "__main__":
    main()
