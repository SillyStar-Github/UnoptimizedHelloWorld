import requests

def get(url):
    r = requests.get(url)
    return r

def returnRequestText(response):
    r = response
    rt = r.text
    return rt

def getAlphabet():
    req = get("https://raw.githubusercontent.com/SillyStar-Github/UnoptimizedHelloWorld/main/alphabet.txt")
    print(req)
    alphabet = returnRequestText(req)
    return alphabet

alphabet = getAlphabet()

alphabetObj = dict()

alphabetObj = {
    "a": "",
    "b": "",
    "c": "",
    "d": "",
    "e": "",
    "f": "",
    "g": "",
    "h": "",
    "i": "",
    "j": "",
    "k": "",
    "l": "",
    "m": "",
    "n": "",
    "o": "",
    "p": "",
    "q": "",
    "r": "",
    "a": "",
    "s": "",
    "t": "",
    "u": "",
    "v": "",
    "w": "",
    "x": "",
    "y": "",
    "z": "",
    "A": "",
    "B": "",
    "C": "",
    "D": "",
    "E": "",
    "F": "",
    "G": "",
    "H": "",
    "I": "",
    "J": "",
    "K": "",
    "L": "",
    "M": "",
    "N": "",
    "O": "",
    "P": "",
    "Q": "",
    "R": "",
    "S": "",
    "T": "",
    "U": "",
    "V": "",
    "W": "",
    "X": "",
    "Y": "",
    "Z": ""
}

alphabetObj["a"] = alphabet[0]

alphabetObj["b"] = alphabet[1]

alphabetObj["c"] = alphabet[2]

alphabetObj["d"] = alphabet[3]

alphabetObj["e"] = alphabet[4]

alphabetObj["f"] = alphabet[5]

alphabetObj["g"] = alphabet[6]

alphabetObj["h"] = alphabet[7]

alphabetObj["i"] = alphabet[8]

alphabetObj["j"] = alphabet[9]

alphabetObj["k"] = alphabet[10]

alphabetObj["l"] = alphabet[11]

alphabetObj["m"] = alphabet[12]

alphabetObj["n"] = alphabet[13]

alphabetObj["o"] = alphabet[14]

alphabetObj["p"] = alphabet[15]

alphabetObj["q"] = alphabet[16]

alphabetObj["r"] = alphabet[17]

alphabetObj["s"] = alphabet[18]

alphabetObj["t"] = alphabet[19]

alphabetObj["u"] = alphabet[20]

alphabetObj["v"] = alphabet[21]

alphabetObj["w"] = alphabet[22]

alphabetObj["x"] = alphabet[23]

alphabetObj["y"] = alphabet[24]

alphabetObj["z"] = alphabet[25]

alphabetObj["A"] = alphabet[26]

alphabetObj["B"] = alphabet[27]

alphabetObj["C"] = alphabet[28]

alphabetObj["D"] = alphabet[29]

alphabetObj["E"] = alphabet[30]

alphabetObj["F"] = alphabet[31]

alphabetObj["G"] = alphabet[32]

alphabetObj["H"] = alphabet[33]

alphabetObj["I"] = alphabet[34]

alphabetObj["J"] = alphabet[35]

alphabetObj["K"] = alphabet[36]

alphabetObj["L"] = alphabet[37]

alphabetObj["M"] = alphabet[38]

alphabetObj["N"] = alphabet[39]

alphabetObj["O"] = alphabet[40]

alphabetObj["P"] = alphabet[41]

alphabetObj["Q"] = alphabet[42]

alphabetObj["R"] = alphabet[43]

alphabetObj["S"] = alphabet[44]

alphabetObj["T"] = alphabet[45]

alphabetObj["U"] = alphabet[46]

alphabetObj["V"] = alphabet[47]

alphabetObj["W"] = alphabet[48]

alphabetObj["X"] = alphabet[49]

alphabetObj["Y"] = alphabet[50]

alphabetObj["Z"] = alphabet[51]

def getLetter(char):
    for letter in alphabetObj:
        if letter == char:
            selectedChar = alphabetObj[letter]
    return selectedChar

hello = ""

hello += getLetter("H")

hello += getLetter("e")

hello += getLetter("l")

hello += getLetter("l")

hello += getLetter("o")

hello += ", "

world = ""

world += getLetter("w")

world += getLetter("o")

world += getLetter("r")

world += getLetter("l")

world += getLetter("d")

def printTogether(arrayOfStrings):
    finishedString = ""

    for string in arrayOfStrings:
        finishedString += string

    print(finishedString)

printTogether([hello, world])