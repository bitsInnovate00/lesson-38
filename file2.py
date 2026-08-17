# open file in read mode
file_read = open('Codingal.txt','r')
print("file in read mode-")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Codingal.txt','w')
# write in the file
file_write.write("file in write mode.....")
file_write.write("hi! i am penguin.I am 1yr old")
file_write.close()

# open the file in append mode
file_append = open('Codingal.txt','a')
# append in the file
file_append.write("\n file in append mode.....")
file_append.write("hi! i am penguin.I am 1yr old")
file_append.close()
