from sys import argv

script, from_file, to_file = argv

print "Copying from %r to %r" % (from_file, to_file)
out_file = open(to_file, "w").write(open(from_file).read())
print "Alright, al done."
