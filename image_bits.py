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
    
# Main routine goes here
image_bits()    