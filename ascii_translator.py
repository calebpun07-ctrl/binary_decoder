
with open('binary.txt', 'r') as f:
    lines = f.readlines() 

with open('translation.txt', 'r') as f:
    translation = f.readlines() #gets lines from both

binary_dict = {}
for i in range(len(lines)-1):
    binary_dict[lines[i]] = translation[i]

with open('binary_sheet.csv', 'w') as f:
    for item in binary_dict:
        
        f.write(f"{item.replace("\n", "")}, {binary_dict[item].replace("\n", "")}\n")
input()

alphabet = {}
for i in range(len(lines)-1): #and the reverse for alphabet
    alphabet[translation[i]] = lines[i]

def check_only(check_str):
    string = ""
    list_bin =[]
    # first remove spaces and non 1s and 0s
    for char in check_str:
        if char == "1" or char == "0":
            string = string + char
        else:
            continue
    # then loop though and cut off every 8th char from the string
    while len(string) >=8:
        a = string[:8]
        list_bin.append(a)
        string = string[8:]

    # return a list
    return list_bin

def binary_to_text(bin_str: str) -> str:
    list_o_bin = check_only(bin_str)
        
    final = ""
    char = ""
    for bin in list_o_bin:
        if len(bin) == 8:
            if "00100000" in bin:
                char = " "
            else:    
                char =(binary_dict.get(bin + "\n"))
                char = char[0] # type: ignore

                final += char
        else:
            return("ERROR, BAD ASCII NUMBER")
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

    