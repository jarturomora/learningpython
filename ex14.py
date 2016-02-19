from sys import argv

script, user_name, pet_name = argv
prompt = ":) "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Allrigth, so you said %r about liking me.
You have a pet called %r, that's nice.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, pet_name, lives, computer)
