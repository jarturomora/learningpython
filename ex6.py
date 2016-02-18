# String definition concatenated with a number.
x = "There are %d types of people." % 10
# Strings definition.
binary = "binary"
do_not = "don't"
# String definition concatenated with two other string variables.
y = "Those who know %s and those who %s" % (binary, do_not)

# Printing two string variables.
print x
print y

# Printing the concatenation of two variables with '%' a space among them will
# be added.
print "I said: %r" % x
print "I also said: '%s'." % y

# Two variables definition, first a Booleand, second a String.
hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

# Printing the concatenation for two variables, one boolean and othe string.
print joke_evaluation % hilarious

# Definition of two string variables.
w = "This is the left side of..."
e = "a string with a right side."

# Concatenation of two string variables with a '+' so no space among them will
# be added.
print w + e
