class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "PARENT override()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()" # Inherited method behaviour
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()" # overrided altered() method

dad = Parent()
son = Child()

dad.altered()
son.altered()