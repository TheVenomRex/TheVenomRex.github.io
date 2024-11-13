with open(r"C:\Users\jd\OneDrive - ShowTech ApS\Dokumenter\77 - dvs. excel\Camilo Fyrværkeri\to be formatted.txt", 'r') as file:
    lines = file.readlines()

with open('output.txt', 'w') as file:
    for line in lines:
        file.write(line.strip() + ';\n')