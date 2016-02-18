# "argv" is the argument variable, it holds the arguments you pass to your
# python scripts when you run it from the terminal, e.g.
# $ python ex13.py apple organge grape
# Above gour parameters are passed to python and this program will use them to
# print it on the screen.
from sys import argv
# This will helps to work with system time.
from datetime import date

script, name, year = argv

city = raw_input("Which city you get born? ")

# We use the date.today().year to get the current year.
print "Hi %r you bonrn in %r and you are about %r years old." % (name, city,
    date.today().year-int(year))
