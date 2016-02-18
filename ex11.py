# Putting the coma at the end of the print statement will read the input
# without adding a line break and going to the next command.
# raw_input() read the data "as is" despite its format, whereas input() just
# reads strings.
#print "How old are you?",
#age = raw_input()
age = input("How old are you?")
# print "How tall are you?",
# This is another way to use raw_input(), however, no space next to the string
# will be added, if you like it just add it.
height = raw_input("How tall are you?")
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r, tall and %r heavy." % (age, height, weight)
