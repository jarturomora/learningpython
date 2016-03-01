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

    def altered(self): # This overrides the Parent altered() method.
        print "CHILD, BEFORE PARENT altered()" 
        super(Child, self).altered() # Here I call the original parent method.
        print "CHILD, AFTER PARENT altered()" 

dad = Parent()
son = Child()

dad.implicit()
son.implicit() # This object will use the inherited implicit() method.

dad.override()
son.override() # This object overrides the method, so it'll call its own method.

dad.altered()
son.altered() # Here a special call to the parent method will be presented.