import time
from datetime import datetime, timezone             # Current Time Items
import random
import binascii
import os
import sys



# Generic wrapper to f.write which logs messages nicely with timestamp
def writeToFile(fileName, transactionString):
    #timePST = updateDateTime()           # Grab Date and Time
    
    f = open(fileName, "a")  # Open File
    #f.write('\n')                        # New log line 
    #f.write("|{}:{}:{}|".format(timePST.hour, timePST.minute, timePST.second))      
    f.write(transactionString)           
    f.close()
     
    
def readFile(fileNameString):
    #filepath = 'vigerene_easy_encrypted.txt'
    with open(fileNameString, encoding="utf8") as fp:
        return fp.read()
        
def readFileBinary(fileNameString):
    #filepath = 'vigerene_easy_encrypted.txt'
    with open(fileNameString, 'rb') as fp:
        return fp.read()

def readFileBytes(fileNameString, numBytes):
    with open (fileNameString, 'rb') as fp:
        return fp.read(numBytes)
        
        
def writeToFileBytes(fileName, payload):
    #timePST = updateDateTime()           # Grab Date and Time
    
    f = open(fileName, "wb")  # Open File    
    f.write(payload)           
    f.close()

def getRandomNumber():
    #return random.randrange(-1000,1000)
    #return "four"
    #return 4
    #return random.random();
    return os.urandom(1)
    
def getRandomBytes(size):
    randomBytes = os.urandom(size)
    #print("Size in Bytes: ", sys.getsizeof(randomBytes))
    return randomBytes


def expandKeyString(fileLength, originalKey):
    expandedKey = ""
    #expandedKey = 0
    
    print("OriginalKey: ", originalKey)
    print("fileLength: ", fileLength)
    while len(expandedKey) < fileLength:
        expandedKey = expandedKey + str(getRandomNumber())

    expandedKey = expandedKey[:fileLength]
    print("ExpandedKey: ", expandedKey)
    print("Length of Expanded Key: ", len(expandedKey))
    return expandedKey
    
def expandKeyBytes(file):
    fileSizeBytes = os.stat(file).st_size
    print("fileSizeBytes: ", fileSizeBytes)
    randomBytes = getRandomBytes(100)
    
    #writeToFileBytes("keyfile", key)
    f = open("keyfile", "ab")  # Open File    
    f.write(randomBytes)           
    
    keySizeBytes = os.stat("keyfile").st_size
    while (keySizeBytes < fileSizeBytes):
        randomBytes = getRandomBytes(100)
        f.write(randomBytes)
        keySizeBytes = os.stat("keyfile").st_size
    
    keyFileContentsTrimmed = readFileBytes("keyfile", fileSizeBytes)
    f.close()
    f = open("keyfile", "wb")
    f.write(keyFileContentsTrimmed) 
    f.close
    print("keySizeBytes", keySizeBytes)
    
    return keyFileContentsTrimmed

def main():

    a = ""
    b = ""
    options = ["E", "D", "Q", "X"]
    print("Options:")
    print("X - XOR")
    print("Q - quit")
    while True:
        uInput = input("Enter an option: ").upper()
        if uInput not in options:
            print("invalid option")

        if uInput == "X":
        
            print("XOR option Selected")
                    ### part 1 ###
            #str1 = "Darlin dont you go"
            #str2 = "and cut your hair!"         
            #t1Encrypt = Stringxor(str1, str2)
            #print("Encrypted: ", t1Encrypt)
                    ##############

                    ### part 2 ###
            #fileToBeEncrypted = input("Enter file to encrypt: ")
            #fileContents = readFile(fileToBeEncrypted)
            # print("fileContents: ", fileContents)
            # lengthFileContents = len(fileContents)
            # originalKey = getRandomNumber()
            # expandedKey = expandKey(lengthFileContents, originalKey)
            # t2Encrypt = Stringxor2(fileContents, expandedKey)
            # print("Encrypted: ", t2Encrypt)
            # t2Decrypted = Stringxor2(t2Encrypt, expandedKey)
            # print("Decrypted: ", t2Decrypted)
                    ###############
            
            
            
                    ## Part 3 ###
            # fileToBeEncrypted = input("Enter file to encrypt: ")
            # #fileContents = readFile(fileToBeEncrypted)
            # fileContents = readFileBinary(fileToBeEncrypted)
            # bmpFileHeader = readFileBytes(fileToBeEncrypted, 54)

            # originalKey = getRandomNumber()
            # lengthFileContents = len(fileContents)
            
            # keyFileBytes = expandKeyBytes(fileToBeEncrypted)       # keyfile now contains random bytes exact same size
            # #print("Size in Bytes keyFileBytes: ", sys.getsizeof(keyFileBytes))
            # keyContents = readFileBinary("keyfile")
            
            
            # #encrypt = bxor(fileContents, keyContents) # made pink logo
            
            # fileSizeBytes = os.stat(fileToBeEncrypted).st_size
            # xord_byte_array = bytearray(fileSizeBytes)
            # print("fileSizeBytes: ", fileSizeBytes)
            # for i in range(fileSizeBytes):
                # xord_byte_array[i] = fileContents[i] ^ keyContents[i]
                
            # encrypt = xord_byte_array
                


            # #expandedKeyBytes = expandedKey.encode('utf-8')
            # #expandedKeyBytes = expandedKey
            # #encrypt = bxor(fileContents, keyFileBytes)
            # #print("encrypt: ", encrypt)

            # encryptedFileName = fileToBeEncrypted + "encrypted.bmp"
            # writeToFileBytes(encryptedFileName, encrypt)

            # # now replace .bmp header
            # f = open(encryptedFileName, 'rb')
            # s = f.read()
            # f.close()

            # bmpFileHeaderEncrypted = readFileBytes(encryptedFileName, 54)
            # s = s.replace(bmpFileHeaderEncrypted, bmpFileHeader)
            # writeToFileBytes(encryptedFileName, s)
                    ################
                    
                    
                    
                    # ### Part 4 ###
            fileToBeEncrypted = input("Enter file to xor: ")
            #fileContents = readFile(fileToBeEncrypted)
            fileContents = readFileBinary(fileToBeEncrypted)
            bmpFileHeader = readFileBytes(fileToBeEncrypted, 54)
            fileToBeEncrypted2 = input("Enter file2 to xor: ")
            #fileContents = readFile(fileToBeEncrypted)
            fileContents2 = readFileBinary(fileToBeEncrypted2)
            #encrypt = bxor(fileContents, fileContents2)
            #print("encrypt: ", encrypt)
            
            fileSizeBytes = os.stat(fileToBeEncrypted).st_size
            xord_byte_array = bytearray(fileSizeBytes)
            print("fileSizeBytes: ", fileSizeBytes)
            for i in range(fileSizeBytes):
                xord_byte_array[i] = fileContents[i] ^ fileContents2[i]
                
            encrypt = xord_byte_array
            
            encryptedFileName = "XORbothencrypted.bmp"
            writeToFileBytes(encryptedFileName, encrypt)
            
            # now replace .bmp header
            f = open(encryptedFileName, 'rb')
            s = f.read()
            f.close()
            
            bmpFileHeaderEncrypted = readFileBytes(encryptedFileName, 54)
            s = s.replace(bmpFileHeaderEncrypted, bmpFileHeader)
            writeToFileBytes(encryptedFileName, s)
                        # #################
           
        
        elif uInput == "Q":
            exit()



# performs XOR on strings and leaves as string
def Stringxor2(s1, s2):
    return ''.join(chr(ord(c1)^ord(c2)) for c1,c2 in zip(s1,s2))


# performs XOR on two bytearray objects
def bxor(b1, b2):
    result = bytearray()
    for b1, b2 in zip(b1, b2):
        result.append(b1 ^ b2)
    return result

    
# performs XOR on the string but turns into hex and chops 0x
def Stringxor(s1,s2):    
    return ''.join(hex(ord(c1) ^ ord(c2))[2:] for c1,c2 in zip(s1,s2))
    

    
if __name__ == '__main__':
    main()