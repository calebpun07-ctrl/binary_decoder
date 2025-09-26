from ascii_translator import check_only
# with open('binary.txt', 'r') as f:
#     lines = f.readlines()

# adder = []

# for i, line in enumerate(lines):
    
#     adder.append(line[:8]+"\n")

# with open('binary.txt', 'w') as f:
#     f.writelines(adder)

# string = "0 0"
# a, b = string.split(' ')
# print(a)
# print(b)

string = "12345678911234567890"

print(check_only(string))