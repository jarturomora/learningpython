from sys import argv

script, filename = argv

# Opening the file in "read-write" mode.
my_file = open(filename, "rw+")

# We show the current contents of the file passed in filename.
print "This is the current content of the file %r." % filename
print my_file.read()

print "Do you want to create new content for this file?"
raw_input("(hit CTRL-C if you don't or hit RETURN if you do) >")

# In order to truncate the file we move the pointer to the first line.
my_file.seek(0)
my_file.truncate()
print "\nThe file %r was deleted..." % filename

print "\nWrite three lines to store in the file %r" % filename
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

my_file.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
my_file.close()
print "The new contents for %r has been saved." % filename
