sum = 0
for i in range(7, 10):  
    sum =sum + i
    print('my sum:',sum)
#=============

sum = 0
for i in range(7, 10):  
    sum =sum + i
print('my sum:',sum)

#=================
sum = 0
for i in range(5, 11, 2):  
	sum += i
print("my sum:*",sum)

#----------------

numbr = [ 5, 3, 8, 4, 2, 6, 9, 11]
sum=0
for val in numbr:	
    sum = sum+val
    print("The sum is", sum)

#----------------
fruits = ['Apple', 'Banana','Papaya','Durian','Mango','Peach','Organge']

for val in fruits:
    if val=='Durian':
        print('My favourite:'+val)
    else:
        print('meh:'+val)
#----------------
fruits = ['Apple', 'Banana','Papaya','Durian','Mango','Peach','Organge']

for x in fruits:
    if x == "Durian":
	    break
    print(x)
#----------------	
#error  student: fix it
fruits = ['Apple', 'Banana','Papaya','Durian','Mango','Peach','Organge']

for x in fruits:
    if x == "Banana":
        break
print(x)



#----------------	
	
#;p	*
fruit_num=[3,4,2,24]
fruit_name=['Apple','Banana','Papaya','Durian','Mango','Peach','Orange']
for x in fruit_num:
  for y in fruit_name:
    print(x* y)
#----------------
def my_function(*ffruits):
    print("my 3rd fruit " + ffruits[2])

my_function('Apple', 'Banana','Papaya','Durian','Mango','Peach','Organge') 

#----------------

def my_function(*ffruits):
    for fruit in ffruits:
        print('fruit item: '+fruit)
    
my_function('Apple', 'Banana','Papaya','Durian','Mango','Peach','Organge') 

#----------------
#1  challenge  create a star pyramid program base on user input value
#2  challenge create a function that sum up all values of n numbers of lists, return total sum.
