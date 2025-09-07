with open('binary.txt', 'r') as f:
    lines = f.readlines()

adder = []

for i, line in enumerate(lines):
    
    adder.append(line[:8]+"\n")

with open('binary.txt', 'w') as f:
    f.writelines(adder)