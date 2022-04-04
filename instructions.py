

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
# Main routine
instructions()