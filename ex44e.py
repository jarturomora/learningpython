class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other() # The composition begins here
                             # where Child has-a other

    def implicit(self):
        self.other.implicit() # Call to the implicit() method of
                              # Child's 'other' instance.

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD BEFORE OTHER altered()"
        self.other.altered() # Call to the altered() method of 'other' object.
        print "CHILD AFTER OTHER altered()"

son = Child()

son.implicit() # Call to the method "composed" from "Other" class.
son.override()
son.altered()