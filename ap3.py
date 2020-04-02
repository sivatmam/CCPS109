x=''
type(x)
x=x+'c'
print(x)
x=x+'b'
print('x again: '+x)

#scope
def g(x):
	def h():
		x='abc'
	x=x+1
	print('gx:=', x)
	h()
	return x

x=3
z=g(x)
print('global :x=',x)	
	




def maximum(L):
    print(L)
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))

l= [3,5,6,43,7,52,9]
print (maximum(l))



def fact(n):
    if n == 1:
        print('Last n: ',n)
        return n
    else: 
        print('n: ',n)
        return n * fact(n-1)

print(fact(4))



C = [1, 9, 2, ['red', 'blue', 'green'], 8, ['lego', [abs, int], 'cell phone']]
# ------------------------------------------------
# Exercise: Define a function printlist(L) that prints the list like
# ------------------------
# : element0
# :: element1
# ::: element2
# :::: element3
# ------------------------------------------------
def printlist(L) :
    print('----------------------------------')
    for i in range(len(L)) :
        element = L[i]
        print((i + 1) * ':' + ' ' + str(element))
print(C)
printlist(C)
# ------------------------------------------------
# Exercise: define printlist2(L) so that if it comes to a list in the list
#   then it prints the individual elements in a similar way
# ------------------------------------------------

C = [1, 9, 2, ['red', 'blue', 'green'], 8, ['lego', [abs, int], 'cell phone']]

def printlist2(L) :
    print('----------------------------------')
    print('----------------------------------')
    for i in range(len(L)) :
        element = L[i]
        if type(element) == list :
            for j in range(len(element)) :
                print((j + 1) * ':' + ' ' + str(element[j]))
        else :
            print((i + 1) * ':' + ' ' + str(element))

print(C)
printlist2(C)
# 
# ------------------------------------------------
# Exercise: define printlist3(L) so that it carries
# the concept deeper, as deeply nested as the lists go
# use recursion
# ------------------------------------------------
def printlist3(L) :
    print('----------------------------------')
    for i in range(len(L)) :
        element = L[i]
        if type(element) == list :
            printlist3(element)
        else :
            print((i + 1) * ':' + ' ' + str(element))
print(C)
printlist3(C)
