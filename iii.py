#readline and readlines.
f=open("2.txt")
data=f.readline() #Prints one line at a time.
print(data)

content=f.readlines()
print(content) #Prints all the lines in the file.
f.close()


#We can also automate the printing of all the lines one 
#by one using readline along with a loop.
g=open("2.txt")
content=g.readline()
while(content!=""):
    print(content)
    content=g.readline()

g.close()