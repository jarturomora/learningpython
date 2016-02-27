def the_while(limit, step):
    i = 0
    the_list = []
    while i < limit:
        print "At the top i is %d" % i
        the_list.append(i)

        i = i + step
        print "Numbers now: ", the_list

        print "At the bottom i is %d" % i
    return the_list

the_limit = input("Give me the limit for the while loop > ")
the_step = input("Give the step for the while loop > ")
numbers = the_while(the_limit, the_step)

print "The numbers"

for num in numbers:
    print num,