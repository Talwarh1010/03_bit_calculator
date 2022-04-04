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

# displays instructions/ information
def instructions():

    statement_generator("Instructions / information" , "=")
    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel).For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("complete as many  calculations as necessary. press <enter> at the end of each calculations or press any key then enter to quit.")
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
            
            
            
# calculates the 3 of bits for text (# of characters x 8)
def text_bits():
    
    print()
    # ask user for a string...
    var_text = input("Enter some text: ")
    
    # calculates # of bits (length of string x 4)
    var_length = len(var_text)
    num_bits = 8 * var_length
    
    # output answer with working
    print()
    print("\'{}\'has {} characters ...". format(var_text, var_length))
    print(" # of bits is {} x 8...  ". format(var_length))
    print("We need {} bits to represent {}". format(num_bits, var_text))
    print()
    
    return ""

# finds number of bits for 24 bit colour
def image_bits():
    
    
    
    # asks the user for the image height and width
    image_height = num_check("Image height: ",1) 
    image_width = num_check("image width: ",1)
    
    # Number of pixels = width x height
    image_pix = image_height * image_width
    
    # number of bits = pixels x 24
    image_bit = image_pix * 24
    
    # output results
    print()
    print("# of pixels = {} x {} = {}". format(image_height,
                                                image_width, image_pix))
    print("# of bits = {} x 24 = {}".format(image_pix, image_bit))
    
    return ""

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




# Main routine goes here

# Heading
statement_generator(" Bit Calculator for integers, Text & Images", "-")

# Display intstructions if user has not used the program before
first_time = input("press <enter> to see the instructions or press any key then enter to continue")
if first_time == "":
    instructions()
# Loop to allow multiple calculations per sessions
keep_going = ""
while keep_going == "":
    
    # ask the user for the file type
    data_type = user_choice()   
    print("You chose", data_type)      

    # For integers, ask for integer
    if data_type =="integer":
        integer_bits()
    
    # For images, ask for width and height    
    # (must be an integer more than / equal to 0)
    elif  data_type == "image":
        image_bits()
        

    # for text, ask for a string
    else:
        text_bits()
        
    print()
    keep_going = input("press <enter> to continue or press any key then enter to quit")
    print()