with open('binary.txt', 'r') as f:
    lines = f.readlines() # or content = f.read()

adder = []

# Example: Replace a word on a specific line
for i, line in enumerate(lines):
    
    adder.append(line[:8]+"\n")

# Example: Add a new line

with open('binary.txt', 'w') as f:
    f.writelines(adder) # or f.write(content)