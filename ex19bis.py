from datetime import datetime

def age_calculator(user_name, birth_year):
    print """
    Hi %r, I'm going to estimate your age.
    Supposing that you've born in %d
    and we are in the year %d, you are %d years old
    """ % (user_name, birth_year, datetime.today().year,
        datetime.today().year - birth_year)

print "Calling the function using numbers:"
age_calculator("Jams", 1978)

print "Calling the function reading data from the user:"
your_name = raw_input("What is your name? ")
your_year = input("Which year you've born? ")
age_calculator(your_name, your_year)

print "Calling the function using variables:"
your_name = "Aaron"
your_year = 2015
age_calculator(your_name, your_year)