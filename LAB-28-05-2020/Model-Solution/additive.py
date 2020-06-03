# additive.py -- an additive cryptosystem supporting encryption, decryption and brute force attack
# Joshua Blinkhorn May 2020
# FSU Kryptologie-LAB summer semester

# LIBRARIES

import sys

# GLOBAL VARIABLES

alph_size = 26
read_filename = sys.argv[2]
input_file = open(read_filename, "r")
input_text = input_file.read()

# FUNCTION DEFINITIONS

# main: handles the high level execution

def main():
    # switch on command line option
    if (sys.argv[1] == "-e"): encrypt()
    elif (sys.argv[1] == "-b"): bruteforce()
    else: print("Bad arguments. See README for usage.") # minimal error handling

    # cleanup    
    input_file.close()
    
# shift: takes a string and a key, returns the string shifted by the key.
# the key should be an integer between 0 and 25
# integers outside this range are treated modulo 26

def shift(text,key):
    # setup
    input = list(text) # convert string to list - easier handling
    output = [] # initially empty 
    input_length = len(input) - 1
    min_value = ord("A")
    max_value = ord("Z")

    # cycle through each character in the input
    for char in input:
        value = ord(char)
        # shift the relevant characters
        if (value >= min_value and value <= max_value):
            shifted_char = chr(((value - min_value + key) % alph_size) + min_value)
        #  ignore the irrelevant characters
        else:
            shifted_char = char
        # add (shifted) character to the output
        output.append(shifted_char)
    # output shifted list as string
    return "".join(output)

# encrypt: performs encryption and decryption
# decryption is obtained as `encryption with the negative key';
# i.e. to decrypt with key k, encypt with key -k

def encrypt():
    # setup
    write_filename = sys.argv[3]
    output_file = open(write_filename,"w")
    input_key_string = sys.argv[4] 
    input_key = int(input_key_string,10) # converts key (string) to base 10 integer
    
    # encrypt
    output_file.write(shift(input_text,input_key))
    
    # conclude
    output_file.close()
    print("Encrypted `" + read_filename + "' with key " + input_key_string + ", saved as `" + write_filename + "'.")


# bruteforce: lists all possible plaintext with keys 0 through 25

def bruteforce():
    print("Brute forcing `" + read_filename + "'.")
    for which_key in range (alph_size):
        print("key: " + str(which_key) + "\n")
        print(shift(input_text, -which_key)) # take the negative key; we are trying to decrypt here
        print("")

# EXECUTION ENTRY POINT

main()
