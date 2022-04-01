# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5
    
    # add decoration to start and end of statement
    statement = "{} {} {}". format(ends, text, ends)
    
    print()
    print(statement)
    print()
    
    return ""

# Checks if user choice is 'integer', 'text' or 'image'
def user_choice():
    
    # Lists of valid responses
    text_ok = ["text", "t", "txt" ]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]
    
    valid = False
    while not valid:
            
        # asks user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()
        
        # Checks for valid responses and returns text, integer or image
        
        if response in text_ok:
            return "text"
            
        elif response in integer_ok:
            return "integer"
            
        elif response in image_ok:
            return "image"
            
        elif response == "i":
            want_integer = input("Press enter for an integer or  press any key then enter for image")
            if want_integer == "":
                return "integer"
            else:
                return "image"
            
            
        else:
            # if response is not valid output an error
            print("Please choose a valid file type!")
            print()

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
            
            
            

# Main routine goes here

# Heading
statement_generator(" Bit Calculator for integers, Text & Images", "-")

# Display intstructions if user has not used the program before

# Loop to allow multiple calculations per sessions
keep_going = ""
while keep_going == "":
    
    # ask the user for the file type
    data_type = user_choice()   
    print("You chose", data_type)      

    # For integers, ask for integer
    if data_type =="integer":
        var_integer = num_check("Enter a integer: ", 0)
    
    # For images, ask for width and height    
    # (must be an integer more than / equal to 0)
    elif  data_type == "image":
        image_width = num_check("image width? ", 1)
        print()
        image_height = num_check("image height? ", 1)

    # for text, ask for a string
    else:
        var_text = input("enter some text: ")
        