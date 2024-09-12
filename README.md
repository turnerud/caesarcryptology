EncodeCaesar takes the message and the shift for the rotation, and gives the ciphertext or encrypted message.
DecodeCaesarShift takes a ciphertext and key and decodes it to the plaintext.
DecodeCaesar takes a cyphertext encoded and decodes the plaintext. It takes the plaintext as an input, and will ask for a shift, but the user input for shift is irrelevant. It only asks because I call DecodeCaesarShift. The program doesn't know the user input and instead uses an algorithm to match the cipher text with the plain text and gives the probable shift/key.

DecodeCaesar is a verification for the plain text message. The plain text and cipher text are both given as parameters. The difference is, this method doesn't know the shift. So, it finds the shift, and if it is consistent with the entire plain text and matches with the verification input, it will return success.
