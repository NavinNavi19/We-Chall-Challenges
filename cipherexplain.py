def decipher(cipher):
    # Create list of potential strings
    results = []
        
    # Create dictionary of alphabet
    alpha = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25 }
    alphaRev = dict(zip(alpha.values(), alpha.keys()))
 
    output = ''
 
    for shift in range(1, 27):
 
            # loop through each character of the cipher
            for char in cipher:
 
                    # make sure the character is not a space.
                    if char!=' ':
			    # convert the character into decimal 0-25
                            char_dec = alpha[char.lower()]
                                
                            # add the shift to our decimal representation of the char
                            # convert this decimal back into our new output character
                            # and add this character to our string
                            char_dec = (char_dec+shift) % 26
                            output += alphaRev[char_dec]
                    else:
                            output += ' '
                
            results.append(output.upper())
            output = ''
 
    return results
 
 
 
cipher = "HVS EIWQY PFCKB TCL XIADG CJSF HVS ZONM RCU CT QOSGOF OBR MCIF IBWEIS GCZIHWCB WG VGCSBBQUQTRG"
results = decipher(cipher)

if results is not []:
        for result in results:
                print ( result+'\n')
