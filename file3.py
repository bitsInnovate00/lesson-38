# program to count number of lines in this file
# opening a file
file = open("codingal.txt","r")
counter = 0

# reading from file
content = file.read()
# splitting content into lines
# and storing them in a list
CoList = content.split("\n")

for i in CoList:
    if i:
        counter+=1

print("this is the number of lines in the file")
print(counter)