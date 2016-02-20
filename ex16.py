from sys import argv

script, filename = argv

print "We're goint to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# Opening the file in write mode
print "Opening file..."
target = open(filename, 'w')

# Erasing all the file contents.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# Reading three lines of text to save in the file.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write there to the file."

# Bellow we write to the file each line of text we read followed by a line
# break to write the text lines one per text file line.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
