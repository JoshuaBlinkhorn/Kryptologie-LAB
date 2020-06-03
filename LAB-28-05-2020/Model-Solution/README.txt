additive.py -- an additive cryptosystem supporting encryption, decryption and brute force attack
Joshua Blinkhorn, May 2020
FSU Kryptologie-LAB, summer semester

DESCRIPTION

this is a command line tool written in python3
ensure python3 is installed on your system
text files should consist of all capital letters (encypted) and punctuation (unencrypted)

USAGE

1) to encypt a text file `plaintext-text' with key k (integer between 0 and 25) and save as `cryptotext-file':

   python3 additive.py -e plaintext-file cryptotext-file k

2) to decrypt, just use encrypt with the negative key:

   python3 additive.py -e cryptotext-file plaintext-file -k

3) to run brute force on `cryptotext-file':

   python3 additive.py -b cryptotext-file
