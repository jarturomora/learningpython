# Here we define a function that receive two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Function call with two numbres
print "We can just give the function numbres directly:"
cheese_and_crackers(20, 30)

# Definition of two variables to pass them as arguments to the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Calling the function with two script variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calling the function with some math inside
print "We can even do math inside too:"
cheese_and_crackers(10 + 2, 5 + 6)

# Calling the function combining variables, math and numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)