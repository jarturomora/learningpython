from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on line, how?
in_file = open(from_file).read()
#indata = in_file.read()

print "Copying %r bytes from %r to %r" % (len(in_file), from_file, to_file)

print "Does the output file exists? %r" % exists(to_file)

out_file = open(to_file, "w")
out_file.write(in_file)

print "Alright, al done."

out_file.close()
