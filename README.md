EncodeCaesar takes the message and the shift for the rotation, and gives the ciphertext or encrypted message.
DecodeCaesarShift takes a ciphertext and key and decodes it to the plaintext.
DecodeCaesar takes a cyphertext encoded and decodes the plaintext. It takes the plaintext as an input, and will ask for a shift, but the user input for shift is irrelevant. It only asks because I call DecodeCaesarShift. The program doesn't know the user input and instead uses an algorithm to match the cipher text with the plain text and gives the probable shift/key.

