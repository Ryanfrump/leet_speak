leet_dict = {
    "a": "@",
    "A": "4",
    "b": "8",
    "B": "8",
    "E": "3",
    "e": "3",
    "I": "!",
    "i": "!",
    "L": "1",
    "l": "1",
    "O": "0",
    "o": "0",
    "S": "5",
    "s": "5"

}

def convert(text: str) -> str:
    leet_word = ""
    for letter in text:
        if letter in leet_dict:
            leet_word += leet_dict[letter]
        else:   
            leet_word += letter
    return leet_word
    

print(convert("Appiste"))