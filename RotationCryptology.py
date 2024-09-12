#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 09:23:55 2024

@author: simon

EncodeCaesar done 
DecodeCaesarShift done 
DecodeCaesar done 

Take plain text and cipher text as a parameter.

Print both
Cipher each list
See if cipher text matches plain text. If not,shift a letter
run the guess, see if it matches 

Return the plain text 'guess'




"""

plainText = "Hi my name is Simon";
codeText = "Kl pb qdph lv Vlprq";

global alphabet;
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

global upperAlphabet;
upperAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def EncodeCaesar():
    originalText = input("What is your plaintext? ");
    shift = int(input("What is your shift? "))
    
    list_of_chars = list(originalText);
    
    cipherTextChars = [];
    
    for x in list_of_chars:
        
        if x in alphabet:
            
            index_of_x = alphabet.index(x);
            
            cipherTextChars.append(alphabet[(index_of_x + shift) % 26]);
        
        elif x in upperAlphabet:
            
            index_of_x = upperAlphabet.index(x);
            
            cipherTextChars.append(upperAlphabet[(index_of_x + shift) % 26]);
            
        else:
            
            cipherTextChars.append(x);
            
    cipherText = ''.join([str(item) for item in cipherTextChars])
    print(cipherText)



def DecodeCaesarShift():
    
    global shift;
    cipherText = input("What is your cipher text? ")
    shift = int(input("What is your shift? "))

    global list_of_cipher_chars;
    
    list_of_cipher_chars = list(cipherText);
    originalTextChars = [];
    for x in list_of_cipher_chars:
        
        if x in alphabet:
            
            index_of_x = alphabet.index(x);
            originalTextChars.append(alphabet[(index_of_x - shift) % 26]);
            
        elif x in upperAlphabet:
            
            index_of_x = upperAlphabet.index(x); 
            originalTextChars.append(upperAlphabet[(index_of_x - shift) % 26]);
        
        else:
            
            originalTextChars.append(x);
            
    originalText = ''.join([str(item) for item in originalTextChars])
    
    print(originalText);
    return list_of_cipher_chars;
    return shift;


def DecodeCaesar(plainText, codeText):
    
    list_of_plain_chars = list(plainText);
    list_of_cipher_chars = list(codeText);  
    elementNumber = 0;
    decoded_cipher_chars = [];
    plainTextVerification = input("What is your plain text? ");
    

    for x in list_of_cipher_chars:
        
        if x in alphabet:
            
            index_of_cipher_char = alphabet.index(x);
            index_of_plain_char = alphabet.index(list_of_plain_chars[elementNumber])
            probableShift = index_of_cipher_char - index_of_plain_char
            decoded_cipher_chars.append(alphabet[index_of_cipher_char - probableShift % 26])
        
            elementNumber += 1;                            
    
        elif x in upperAlphabet:
            
            index_of_cipher_char = upperAlphabet.index(x);
            index_of_plain_char = upperAlphabet.index(list_of_plain_chars[elementNumber])
            probableShift = index_of_cipher_char - index_of_plain_char
            decoded_cipher_chars.append(upperAlphabet[index_of_cipher_char - probableShift % 26])
        
            elementNumber += 1;
            
        else:
            
            decoded_cipher_chars.append(x);
            elementNumber += 1;
            
        decodedCipher = ''.join([str(item) for item in decoded_cipher_chars])
        
    if decodedCipher == plainTextVerification:
        
        print("Success");
        
    else:
        
        print("Failed");
        
    return decodedCipher;

"""
EncodeCaesar();
DecodeCaesarShift();
"""
DecodeCaesar(plainText, codeText);




    
    