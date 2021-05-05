# decode and encode a binary substituion cipher

#Get the key
input1 = input("Enter your first input here ")
input2 = input ("Enter your second input here ")

def binarySubCipher(input1, input2):
        
        outputTemp = ""

        x = 0

        while len(input1) > x:
            if input1[x] == input2[x]:
                outputTemp += "0"
                x +=1
            elif input1[x] != input2[x]:
                outputTemp += "1"
                x += 1

        return outputTemp


if __name__ == "__main__":
    print(binarySubCipher(input1, input2))