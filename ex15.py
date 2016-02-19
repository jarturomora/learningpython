# Enable to read arguments from script's call
from sys import argv

# Unpack the arguments
script, filename = argv

# Open the file passed as argument in the 'filename' variable.
txt = open(filename)

print "Here's your file %r:" % filename
# Read the file contents and print it on the console.
#print txt.readline()
#print txt.read()
x = txt.readlines()
print x[1]

# Playing with the file
print "Curren file position: %r" % txt.tell()
# print txt.readline()

# We ask the user to write the name of a file to open.
#print "Type the filename again:"
#file_again = raw_input("> ")

# Open the file
#txt_again = open(file_again)

# Print the file contents on the console.
#print txt_again.read()
