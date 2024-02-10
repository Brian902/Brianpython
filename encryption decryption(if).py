#message encrypted/ decrypted
inputText = input("Enter text: ")

#encryption/ decryption key
key = 5
#encrypt/ decrypt
mode = 'decrypt'
ledger = 'uabcdefghijklmnopqrstuvwxyz  1234567890'
#output message
outputText = ''

for char in inputText:
     # find the index of the charecter in ledger
     inputIndex = ledger .find(char)
     #perform encryption/ decryption
     if mode == 'encrypt':
         outputIndex = inputIndex + key
     elif mode == 'decrypt':
         outputIndex = inputIndex + key
     #handle wraparound
     if outputIndex >= len(ledger):
         outputIndex = outputIndex - len(ledger)
     elif outputIndex < 0:
         outputIndex = outputIndex + len(ledger)

     #output
     outputText = outputText + ledger[outputIndex]
print(outputText)

