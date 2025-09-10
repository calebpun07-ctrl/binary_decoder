
with open('binary.txt', 'r') as f:
    lines = f.readlines() 

with open('translation.txt', 'r') as f:
    translation = f.readlines() #gets lines from both

binary_dict = {}
for i in range(len(lines)-1):
    binary_dict[lines[i]] = translation[i]

alphabet = {}
for i in range(len(lines)-1): #and the reverse for alphabet
    alphabet[translation[i]] = lines[i]

def binary_to_text(str: str) -> str:
    string = str
    list = []
    # while len(string)> 6:
    #         stringA = string[:8]
    #         string = string[9:]
    #         list.append(stringA)
    
    while " " in string:
        a, b = string.split(" ")
        list.append(a)
        string = b

    final = ""
    char = ""
    for bin in list:
        if len(bin) == 8:

            if "00100000" in bin:
                char = " "
            else:    
                char =(binary_dict.get(bin + "\n"))
                char = char[0] # type: ignore

                final += char
        else:
            return("ERROR, BAD BIN NUMBER")
    return(final)
    

def text_to_binary(str: str) -> str:
    string = str
    final = ""
    for char in string:
        final +=((alphabet.get(char + "\n")[:8])+" ")
    
    return final
    

while True:
    what_to_be_translated = input("\nTranslate BIN to Text (1) or Text to BIN (2): ")
    if what_to_be_translated == "1":
        get_input = input("Enter Binary code: ")
        print(binary_to_text(get_input))
    elif what_to_be_translated == "2":
        get_alphbet = input("Enter text to be translation: ")
        print(text_to_binary(get_alphbet))
    else:
        print("try again")

    