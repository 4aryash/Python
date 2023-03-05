#!bin/python3

import numpy as np

UID =  119222119
Last_Name = 'Aaryash Raj'
First_Name = 'Sinha'

def vigenere_enc(plaintext, keyword):
    # Converts the plaintext to uppercase and remove spaces
    plaintext = plaintext.upper().replace(' ', '')
    keyword = keyword.upper().replace(' ','')    
    # Repeating the keyword to match the length of the plaintext
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)] 
    # Encrypts the plaintext using the Vigenere cipher
    ciphertext = ''
    for i in range(len(plaintext)):
        pi = ord(plaintext[i])
        ki = ord(keyword[i])
        ci = ((pi + ki) % 26)
        ciphertext += chr(ci+65)
    
    return ciphertext

def vigenere_dec(ciphertext, keyword):
    # Repeating the keyword to match the length of the ciphertext
    keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    ciphertext = ciphertext.upper().replace(' ','')
    keyword = keyword.upper().replace(' ', '')
    # Decrypt the ciphertext using the Vigenere cipher
    plaintext = ''
    for i in range(len(ciphertext)):
        ci = ord(ciphertext[i]) - 65
        ki = ord(keyword[i]) - 65
        pi = (ci - ki) % 26
        plaintext += chr(pi + 65) 
    return plaintext

def hill_enc(M, plaintext):
    # Convert the plaintext to uppercase and remove spaces
    plaintext = plaintext.upper().replace(' ', '')
    # Pad the plaintext with 'X' characters to make its length a multiple of 3
    if len(plaintext) % 3 == 1:
        plaintext += 'XX'
    elif len(plaintext) % 3 == 2:
        plaintext += 'X'
    
    # Convert the plaintext to a matrix of numbers
    P = []
    for i in range(0, len(plaintext), 3):
        P.append([ord(plaintext[i]) - 65, ord(plaintext[i+1]) - 65, ord(plaintext[i+2]) - 65])
  
    # Encrypt the plaintext using the Hill cipher
    C = []
    for i in range(len(P)):
        Pi = np.array(P[i]).T
        Ci = np.matmul(Pi, M) % 26 
        C.append(Ci)
    
    # Convert the ciphertext to a string
    ciphertext = ''
    for i in range(len(C)):
        ciphertext += chr(C[i][0] + 65) + chr(C[i][1] + 65) + chr(C[i][2] + 65)
    return ciphertext

if __name__ == "__main__":

    #BANNER
    print("\n\t _     _                                     _        ______  ")
    print("\t| |   | |                                   | |      (_____ \ ")
    print("\t| |__ | | ___  ____   ____ _ _ _  ___   ____| |  _     ____) )")
    print("\t|  __)| |/ _ \|    \ / _  | | | |/ _ \ / ___| | / )   /_____/ ")
    print("\t| |   | | |_| | | | ( (/ /| | | | |_| | |   | |< (    _______ ")
    print("\t|_|   |_|\___/|_|_|_|\____)\____|\___/|_|   |_| \_)  (_______)")                                                          
    print("\n\tAaryash Raj Sinha 119222119")

    # Part 1: Vigenere Cipher
    input_key = input("\n\n\tEnter a KEY Value: ")
    input_str = input("\tEnter a String to Encrypt: ")
    encstr = vigenere_enc(input_str, input_key)
    print(f"\n\tVignere Cipher generated Ciphertext:\t{encstr}")
    decstr = vigenere_dec(encstr, input_key)
    print(f"\tVignere Cipher generated Decryptedtext:\t{decstr}") 

    # Part 2: Hill Cipher
    input_matrix = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]]) 
    input_plaintext = 'Test String'                    
    ciphertext = hill_enc(input_matrix, input_plaintext)
    print(f"\n\tHill Cipher generated Ciphertext:\t{ciphertext}\n\n")
