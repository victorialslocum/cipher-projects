def one_input(ASCtype, input1):
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

    if ASCtype == "7bit":
        for key, value in binaryTable.items():
            binaryTable[key] = value[1:]
    else:
        binaryTable = binaryTable

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

print(one_input("7bit", 'a'))