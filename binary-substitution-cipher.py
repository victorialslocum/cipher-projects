# decode and encode a binary substituion cipher

#Get the key
plainText = input("Enter your plaintext here ")
cipherText = input ("Enter your ciphertext here ")

key = ""
x = 0
lenPlain = len(plainText)

def getKey():
    global x, key, lenPlain

    while lenPlain > x:
        if plainText[x] == cipherText[x]:
            key += "0"
            x +=1
        elif plainText[x] != cipherText[x]:
            key += "1"
            x += 1


if __name__ == "__main__":
    getKey()
    print(key)