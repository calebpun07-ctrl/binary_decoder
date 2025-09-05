
with open('binary.txt', 'r') as f:
    lines = f.readlines() # or content = f.read()

with open('translation.txt', 'r') as f:
    translation = f.readlines() # or content = f.read()

binary_dict = {}
for i in range(len(lines)-1):
    binary_dict[lines[i]] = translation[i]

alphabet = {}
for i in range(len(lines)-1): #and teh reverse
    alphabet[translation[i]] = lines[i]

# print(binary_dict["01000001"])

# for item in binary_dict:
#     print(item, binary_dict.get(item))

def binary_to_text(str: str) -> str:
    string = str
    list = []
    while len(string)> 6:
            stringA = string[:8]
            string = string[9:]
            # stringA, stringB = string.split(" ")
            # string = stringB
            list.append(stringA)
            # print(list)
    # list.append(string)
    final = ""
    for bin in list:
        # print(f"|{bin}|")
        if "00100000" in bin:
            char = " "
        else:    
           char =(binary_dict.get(bin + "\n"))
           char = char[0]

        final += char
    
    return(final)

while True:
    get_input = input("Enter Binary code: ")
    print(binary_to_text(get_input))

    