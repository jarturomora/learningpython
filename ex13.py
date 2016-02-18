# "argv" is the argument variable, it holds the arguments you pass to your
# python scripts when you run it from the terminal, e.g.
# $ python ex13.py apple organge grape
# Above gour parameters are passed to python and this program will use them to
# print it on the screen.
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is", second
print "Your third variable is", third
