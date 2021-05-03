# to run this (lol)
# export FLASK_APP=main.py
# export FLASK_ENV=development
# flask run


from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    input1 = request.args.get("input1", "")
    input2 = request.args.get("input2", "")

    if input1 and input2:
        output = two_inputs(input1, input2)
    elif input1:
        output = one_input(input1)
    else:
        output = ""

    return render_template("index.html", output=output)

@app.route("/<input1>/<input2>")
def two_inputs(input1, input2):
    # english to binary dictionary
    binaryTable =   {
    "a" : "01100001",
    "b" : "01100010",
    "c" : "01100011",
    "d" : "01100100",
    "e" : "01100101",
    "f" : "01100110",
    "g" : "01100111",
    "h" : "01101000",
    "i" : "01101001",
    "j" : "01101010",
    "k" : "01101011",
    "l" : "01101100",
    "m" : "01101101",
    "n" : "01101110",
    "o" : "01101111",
    "p" : "01110000",
    "q" : "01110001",
    "r" : "01110010",
    "s" : "01110011",
    "t" : "01110100",
    "u" : "01110101",
    "v" : "01110110",
    "w" : "01110111",
    "x" : "01111000",
    "y" : "01111001",
    "z" : "01111010",
    "A" : "01000001",
    "B" : "01000010",
    "C" : "01000011",
    "D" : "01000100",
    "E" : "01000101",
    "F" : "01000110",
    "G" : "01000111",
    "H" : "01001000",
    "I" : "01001001",
    "J" : "01001010",
    "K" : "01001011",
    "L" : "01001100",
    "M" : "01001101",
    "N" : "01001110",
    "O" : "01001111",
    "P" : "01010000",
    "Q" : "01001111",
    "R" : "01010010",
    "S" : "01010011",
    "T" : "01010100",
    "U" : "01010101",
    "V" : "01010110",
    "W" : "01010111",
    "X" : "01011000",
    "Y" : "01011001",
    "Z" : "01011010"
    }


    # change to output through binary sub cipher
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

    # change to english from binary
    def englishToBinary(string):
        tempBinary = ""

        n = 1

        stringSplit = [string[i:i+n] for i in range(0, len(string), n)]

        for i in stringSplit:
            for key, value in binaryTable.items():
                if i == key:
                    tempBinary += value

        return tempBinary

    # repeat string to amtch a desired length
    def repeatString(string, targetLength):
        number_of_repeats = targetLength // len(string) + 1
        a_string_repeated = string * number_of_repeats
        a_string_repeated_to_target = a_string_repeated[:targetLength]
        return a_string_repeated_to_target
    
    # change binary to english
    def binaryToEnglish(string):
        englishTranslation = ""

        n = 8

        binaryStringSplit = [string[i:i+n] for i in range(0, len(string), n)]

        for i in binaryStringSplit:
            for key, value in binaryTable.items():
                if i == value:
                    englishTranslation += key

        return englishTranslation

    if "0" in input1 and "0" in input2:
        # change to strings
        input1 = str(input1)
        input2 = str(input2)

        # replace spaces
        input1= input1.replace(" ", "")
        input2 = input2.replace(" ", "")

        # binary substituion cipher
        output = binarySubCipher(input1, input2)

        # print final output
        return output

    elif "0" in input1 and input2[0] in binaryTable.keys():
        # change to strings
        input1 = str(input1)
        input2 = str(input2)

        # replace spaces
        input1= input1.replace(" ", "")
        input2 = input2.replace(" ", "")

        # change input 2 to binary
        input2 = englishToBinary(input2)

        # make input 2 the same length as input 1
        input2 = repeatString(input2, len(input1))

        # binary substitution cipher
        binaryOutput = binarySubCipher(input1, input2)
        
        # convert to english
        output = binaryToEnglish(binaryOutput)

        # return final output
        return output

    elif "0" in input2 and input1[0] in binaryTable.keys():
        # change to strings
        input1 = str(input1)
        input2 = str(input2)

        # replace spaces
        input1= input1.replace(" ", "")
        input2 = input2.replace(" ", "")
        
        # change input 1 to binary
        input1 = englishToBinary(input1)

        # make input1 the same length as input 2
        input1 = repeatString(input1, len(input2))

        # binary substitution cipher
        binaryOutput = binarySubCipher(input1, input2)

        # convert to english
        output = binaryToEnglish(binaryOutput)

        # return final output
        return output

    else:
        #change inputs to strings
        input1 = str(input1)
        input2 = str(input2)

        # replace spaces
        input1 = input1.replace(" ", "")
        input2 = input2.replace(" ", "")

        #make the english input 2 the same length as the english input 1
        input2 = repeatString(input2, len(input1))

        # run code to convert to binary
        input1 = englishToBinary(input1)
        input2 = englishToBinary(input2)

        # run binary substitution cipher
        output = binarySubCipher(input1, input2)

        # return final output
        return output

@app.route("/<input1>")
def one_input(input1):
    binaryTable =   {
    "a" : "01100001",
    "b" : "01100010",
    "c" : "01100011",
    "d" : "01100100",
    "e" : "01100101",
    "f" : "01100110",
    "g" : "01100111",
    "h" : "01101000",
    "i" : "01101001",
    "j" : "01101010",
    "k" : "01101011",
    "l" : "01101100",
    "m" : "01101101",
    "n" : "01101110",
    "o" : "01101111",
    "p" : "01110000",
    "q" : "01110001",
    "r" : "01110010",
    "s" : "01110011",
    "t" : "01110100",
    "u" : "01110101",
    "v" : "01110110",
    "w" : "01110111",
    "x" : "01111000",
    "y" : "01111001",
    "z" : "01111010",
    "A" : "01000001",
    "B" : "01000010",
    "C" : "01000011",
    "D" : "01000100",
    "E" : "01000101",
    "F" : "01000110",
    "G" : "01000111",
    "H" : "01001000",
    "I" : "01001001",
    "J" : "01001010",
    "K" : "01001011",
    "L" : "01001100",
    "M" : "01001101",
    "N" : "01001110",
    "O" : "01001111",
    "P" : "01010000",
    "Q" : "01001111",
    "R" : "01010010",
    "S" : "01010011",
    "T" : "01010100",
    "U" : "01010101",
    "V" : "01010110",
    "W" : "01010111",
    "X" : "01011000",
    "Y" : "01011001",
    "Z" : "01011010"
    }

    if "0" in input1:
        
        binaryString = input1.replace(" ", "")
        englishTranslation = ""
        n = 8

        binaryStringSplit = [binaryString[i:i+n] for i in range(0, len(binaryString), n)]

        for i in binaryStringSplit:
            for key, value in binaryTable.items():
                if i == value:
                    englishTranslation += str(key)

        return englishTranslation
        
    else:
        binaryString = input1.replace(" ", "")
        binaryTranslation = ""
        n = 1

        englishStringSplit = [input1[i:i+n] for i in range(0, len(input1), n)]

        for i in englishStringSplit:
            for key, value in binaryTable.items():
                if i == key:
                    binaryTranslation += value

        return binaryTranslation