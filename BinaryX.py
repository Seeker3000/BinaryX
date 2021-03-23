"""Transform a binary value in the following values:
   decimal
   hexadecimal
   octal
   unicode"""

def binaryX(arg):
        return int(arg,2)

user_binary = input('Binary:      ')
decimal = binaryX(user_binary)
hexadecimal = hex(decimal)      # transforms a number in a hexadecimal number
octal = oct(decimal)            # transforms a number in a octal number
 
print("Decimal:    ", decimal) 
print("Hexadecimal:", hexadecimal)
print("Octal:      ", octal)
try:
        unicode = chr(decimal)          # transforms a number in a unicode character
        print("Unicode:    ", unicode)
except:
        print('Unicode:     BINARY IS TOO BIG')


