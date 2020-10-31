myFile = open("filename.txt", "a")
myFile.write("Now the file has more content!")
myFile.close()

#open and read the file after the appending:
myReadFile = open("filename.txt", "r")
print(myReadFile.read()) 
myReadFile.close()

# Context Manager
with open("filename.txt", "r") as myReadFile:
    print(myReadFile.read())
