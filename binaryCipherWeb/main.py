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
    if "0" in input1 and "0" in input2:
         # change to strings
        input1 = str(input1)
        input2 = str(input2)

        # change to output
        def getKey(input1, input2):
            
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

        # run code
        output = getKey(input1, input2)

        # print final output
        return output
    else:
        # dictionary from english to output 
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

        input1 = str(input1)
        input2 = str(input2)

        input1String = input1.replace(" ", "")
        input2String = input2.replace(" ", "")

        def repeatString(englishString, targetLength):
            number_of_repeats = targetLength // len(englishString) + 1
            a_string_repeated = englishString * number_of_repeats
            a_string_repeated_to_target = a_string_repeated[:targetLength]
            return a_string_repeated_to_target

        input2String = repeatString(input2String, len(input1String))

        # function that turns english to output and outputs it as a string
        def englishTooutput(englishString):
            tempoutput = ""

            n = 1

            stringSplit = [englishString[i:i+n] for i in range(0, len(englishString), n)]

            for i in stringSplit:
                for key, value in binaryTable.items():
                    if i == key:
                        tempoutput += value

            return tempoutput

        # run code to convert to output 
        input1output = englishTooutput(input1String)
        input2output = englishTooutput(input2String)

        # change to output
        def getKey(input1, input2):
            
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

        # run code
        output = getKey(input1output, input2output)

        # print final output
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
        
        outputString = input1.replace(" ", "")
        englishTranslation = ""
        n = 8

        outputStringSplit = [outputString[i:i+n] for i in range(0, len(outputString), n)]

        for i in outputStringSplit:
            for key, value in binaryTable.items():
                if i == value:
                    englishTranslation += str(key)

        return englishTranslation
    else:
        returnoutput = ""

        n = 1

        stringSplit = [input1[i:i+n] for i in range(0, len(input1), n)]

        for i in stringSplit:
            for key, value in binaryTable.items():
                if i == key:
                    returnoutput += value

        return returnoutput