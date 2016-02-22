from sys import argv

script, input_file = argv

# Here all the file is printed on the screen
def print_all(f):
    print f.read()

# File pointer is set to the begining of the file
def rewind(f):
    f.seek(0)

# A line is printed, the one passed in the line_count parameter
def print_a_line(line_count, f):
    print line_count, f.readline()

# Opening the file
current_file = open(input_file)

# The following lines play with the functions.
print "Firts let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line +=1
print_a_line(current_line, current_file)