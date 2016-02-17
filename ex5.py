name = 'Jose A Mora'
age = 37
height = 1.88 # Meters
weight = 105 # Kilos
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r meters tall." % height
print "He's %1.2f killos heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height, weight,
    age + height + weight)
