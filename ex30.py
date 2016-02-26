people = 252
cars = 100
buses = 300

# These are nested if since we are using elif to ask a second question.
if cars > people:
    print "We should take cars."
elif cars < people:
    print "We should not take cars."
else:
    print "We can'd decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

# This is a single if-then-else structure.
if people > buses:
    print "Alright, let's just take the busses."
else:
    print "Fine, let's stay at home then."

# Just my own contribution with a semi-complex condition.
if people < cars and cars < buses:
    print "Let's go by bus to home."
else:
    print "There are too many people, so we should take the bus."