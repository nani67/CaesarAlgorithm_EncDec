SIZE = 26

def getMode():
    print("Brute Force for Caesar Cipher")
    mode = input().lower()
    return mode
            
def getMessage():
    print("Enter message")
    return input()
    
def getConvertedMessage(mode, message, key):
    if mode[0] == 'd':
    	key = -key
    translated = ''
    
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                        
            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()    
message = getMessage()

print("Translated")
for key in range(1, SIZE + 1):
    print(key, getConvertedMessage(mode, message, key))