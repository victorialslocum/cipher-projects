# decode and encode a binary substituion cipher

#Get the key
plaintext = input("Enter your plaintext here ")
ciphertext = input ("enter your ciphertext here ")

key = ""
x = 0
lenPlain = len(plaintext)

def getKey():
    global x, key, lenPlain
    while lenPlain > x:
        if plaintext[x] == ciphertext[x]:
            key = key + "0"
            x +=1
        elif plaintext[x] != ciphertext[x]:
            key = key + "1"
            x += 1


if __name__ == "__main__":
    getKey()
    print(key)