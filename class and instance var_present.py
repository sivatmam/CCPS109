class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

#--------------------
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y



p = Point(4, 2)
q = Point(6, 3)
r = Point()       # r represents the origin (0, 0)
print(p.x, q.y, r.x)


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, a_name):
        self.name = a_name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)

#list and disctionary are mutables and will create problem
class Dog:

    tricks = []             # 

    def __init__(self, a_name):
        self.name = a_name

    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
#print tricks for d and e and see that problem


----

class Dog:
   
    def __init__(self, a_name):
        self.name = a_name
        self.tricks = []    # creates a new empty list for each dog
     

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks

e.tricks

----

class Dog:
    tag=1
    def __init__(self, a_name):
        self.name = a_name
        self.tricks = []    # creates a new empty list for each dog
        self.id=Dog.tag     # unique id for each instance
        Dog.tag+=1

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
# print out id for each intance  

# inheritance
class Pet(object):
    tag=1
    def __init__(self, a_name):
        self.name = a_name
        self.tricks = []    # 
        self.id=Pet.tag
        Pet.tag+=1

    def add_trick(self, trick):
        self.tricks.append(trick)


class Feline(Pet):
  def __init__(self,aname,mcolour,mweight):
    Pet.__init__(self, aname)
    self.weight=mweight
    self.colour=mcolour
  # create a get trick method that print the tricks list


  
c=Feline('kay','orange',20)
c.add_trick('long nap')

#to show all attributs of the object
#catt=vars(c)
#print(catt.items())




