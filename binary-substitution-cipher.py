# decode and encode a binary substituion cipher

#decode
plaintext = input("Enter your plaintext here ")
ciphertext = input ("enter your ciphertext here ")

key = ""
x = 0
lenPlain = len(plaintext)

while lenPlain > x:
    if plaintext[x] == ciphertext[x]:
        key = key + "0"
        x +=1
    elif plaintext[x] != ciphertext[x]:
        key = key + "1"
        x += 1


print(key)