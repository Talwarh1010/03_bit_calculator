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
    # (must be an integer more than / equal to 0)
    
    # for images, ask for width and height
    