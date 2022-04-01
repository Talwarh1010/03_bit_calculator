# checks input is a number more than a given value
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
            
            
            