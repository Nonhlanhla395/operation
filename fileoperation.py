names = "C:/Users/admin/Desktop/names.txt"
output = "C:/Users/admin/Desktop/empy.txt"

with open(names, 'r') as file:
    text = file.read()
    wordCount = len(text.split())
    print(text)
    print("word Count", wordCount)

    #writing a file 
with open (output, 'w') as file:
    line1 = file.write('Careers IT\n')
    line2 = file.write('System Developers\n')
    line3 = file.write('Assessor - Mr Masiya')
    file.close()