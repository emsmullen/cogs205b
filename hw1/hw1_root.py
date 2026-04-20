def root(number):
    """Manually returns the square root of a number."""
    return number ** 0.5

def test_root(number):
    """Tests the root function."""
    root_result = root(number)
    if root_result*root_result == number:
        bool_result = True
    else:        
        bool_result = False
    return bool_result

def main():
    """Tests the root function."""
    
    number = input("Enter a number to test the root function:\n")
    number = float(number)
    print("Testing the root function with the number ", number,"\n")
    print("The square root of ", number, " is ", root(number), "\n")
    if test_root(number):
        print("Test passed!")
    else:
        print("Test failed.")
        
if __name__ == "__main__":
    main()