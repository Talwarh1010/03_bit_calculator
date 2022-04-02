# checks input is more than given value
def num_check(question, low):
    valid = False
    while not valid:
        
        error = "Please enter an integer that is more than"
        "(or equal to)". format(low)
            
        try:
            
            # asks the user to enter a number
            response = int(input(question))
            
            # checks number  is more than zero
            if response >= low:
                return response
                
            # outputs error if input is invalid
            else:
                print(error)
                print()
            
        except ValueError:
            print(error)
            
            
            
# converts decimal to binary and states how
# many bits are needed to represent the original integer
def integer_bits():
    
    # get integer (must be >= 0)    
    var_integer = num_check("Please enter an integer: ", 0)
    
    # converting integr to binary
    var_binary = "{0:b}". format(var_integer)
    
    # calculates # of bits (length of string above)
    num_bits = len(var_binary)
    
    # output answers with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits  is {}".format(num_bits))
    
    return ""

# Main routine
integer_bits()