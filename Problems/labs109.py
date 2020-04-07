

"""
Ryerson letter grade  
 
def ryerson_letter_grade(pct): 
 
Given the percentage grade for the course, calculate and return the letter grade that would appear
in the Ryerson grades transcript, as defined on the page ​Ryerson Grade Scales​. The letter grade 
should be returned as a string that consists of the uppercase letter followed by the possible 
modifier ​'+'​ or ​'-'​. The function should work correctly for all values of ​pct​ from 0 to 150. 
 
(Same as all other programming problems that follow this problem, this can be solved in various 
different ways. At this point ofyourstudies,thesimplestwaytosolvethisproblemwouldprobably 
be just to use an ​if-else ladder​.) 
 
pct     Expected result 
45          'F' 
62          'C-' 
89          'A' 
107         'A+' 

"""

def ryerson_letter_grade(pct):

  if type(pct) is float or type(pct) is int:
    if pct >= 0 and pct < 50:
      return 'F'
    elif pct >= 50 and pct < 53: 
      return 'D-'
    elif pct >= 53 and pct < 57: 
      return 'D'
    elif pct >= 57 and pct < 60: 
      return 'D+'
    elif pct >= 60 and pct < 63: 
      return 'C-'
    elif pct >= 63 and pct < 67: 
      return 'C'
    elif pct >= 67 and pct < 70: 
      return 'C+'
    elif pct >= 70 and pct < 73: 
      return 'B-'
    elif pct >= 73 and pct < 77:
      return 'B'
    elif pct >= 77 and pct < 80: 
      return 'B+'
    elif pct >= 80 and pct < 85: 
      return 'A-'
    elif pct >= 85 and pct < 90: 
      return 'A'
    elif pct >= 90 and pct <= 150:
      return 'A+'
    else:
      return None
  else:
    return None

"""
Ascending list 
 
def is_ascending(items): 

Determine whether the sequence of ​items is ​ascending so that its each element is​ strictly larger 
than (and not merely equal to) the element that precedes it. Return ​True if that is the case, and 
return ​False​ otherwise. 
  
Note that the empty sequence is ascending, as is every one-element sequence, so be careful that 
your function returns the correct answers also in these seemingly insignificant​ edge cases of this 
problem. (If these sequences were not ascending, pray tell, what would be the two elements that 
violate the requirement of that particular sequence being ascending?) 
 
items Expected result 
[-5, 10, 99, 123456] True 
[2, 3, 3, 4, 5] False 
[-99] True 
[] True 
[4, 5, 6, 7, 3, 7, 9] False 
[1, 1, 1, 1] False 
 
(In the same spirit, note how every possible universal claim made about the elements of an empty 
sequence is trivially true.For example,if​ seq is the empty sequence,the two claims"All elements of
 seq are odd" and "All elements of ​seq are even" are both equally true, which seems highly 
 counterintuitive.) 
"""
def is_ascending(items):
  if len(items) < 2:
    return True
  else:
    largest = items[0]
    for i in range(len(items)):
      if i == 0:
        continue
      if items[i] > largest:
        largest = items[i]
        continue
      else:
        return False
    return True


"""
Riffle 
 
def riffle(items, out = True): 

Given a list of ​items that is guaranteed to contain an even number of elements (note that the
integer zero is an even number), create and return a list produced by performing a perfect ​riffle to
the ​items​ by interleaving the items of the two halves of the list in an alternating fashion. 

When performing a perfect riffle, also known as the ​Faro shuffle​, the list of​ items is split in two
equal sized halves, either conceptually or in actuality. The first two elements of the result are then
the first elements of those halves. The next two elements of the result are the second elements of
those halves, followed by the third elements of those halves, and so on up to the last elements of
those halves. The parameter ​out determines whether this function performs an​ out shuffle or an​ in
shuffle​, that is, from which half of the list the alternating card is taken first. 
 
items                     out     Expected result 
[1, 2, 3, 4, 5, 6, 7, 8]  True    [1, 5, 2, 6, 3, 7, 4, 8] 
[1, 2, 3, 4, 5, 6, 7, 8]  False   [5, 1, 6, 2, 7, 3, 8, 4] 
[]                        True    [] 
['bob', 'jack']           True    ['bob', 'jack'] 
['bob', 'jack']           False   ['jack', 'bob']  
"""

def riffle(items, out = True):
  items_halflength = int(len(items) / 2)
  first_half = items[:items_halflength]
  second_half = items[items_halflength:]

  riffled_items = []
  
  for index in range(items_halflength):
    if out:
      riffled_items.append(first_half[index])
      riffled_items.append(second_half[index])
    else:
      riffled_items.append(second_half[index]) 
      riffled_items.append(first_half[index])

  return riffled_items     


"""
Only odd digits 
 
def only_odd_digits(n): 

Check that the given positive integer​ n contains only odd digits (1, 3, 5, 7 and 9)
when it is written out. Return ​True if this is the case, and ​False otherwise. Note that this 
question is not asking whether the number ​n itself is odd or even. You therefore will have to 
look at every digit of the given number before you can claim that the number contains no odd digits. 
 
Hint: to extract the lowest digit of a positive integer ​n​, use the expression​n % 10​. 
To extract all other digits except the lowest one, use the expression ​n // 10​. 
Or, if you don't want to be this fancy, first convert the number into a string and work there.  
 
n               Expected result 
8               False 
1357975313579   True 
42              False 
71358           False 
0               False   
"""

def only_odd_digits(n):
  str_n = str(n)
  for index in str_n:
    if int(index) % 2 == 0:
      return False
  return True
"""
# Implemented using floor division and modulus of 10
# Runs the test 0.001s slower than the string iteration function above

def only_odd_digits(n):
    while n > 0:
        if (n%10)%2 == 0:
            return False
        n = n // 10
    return True
"""


"""
Blocks in pyramid 
 
def pyramid_blocks(n, m, h): 

A pyramid structure (although here in the ​ancient Meso-american than the more famous ancient 
Egyptian style) is built from layers, each layer consisting of a rectangle of identical cubic blocks. 
The top layer of the pyramid consists of ​n rows and ​m columns of such blocks. The layer immediately 
below each layer contains one more row and one more column, all the way to the bottom layer of 
the pyramid. If the entire pyramid consists of ​h such layers, how many blocks does this pyramid 
contain in total? 
 
Here you can solve this problem in a straight forward fashion by simply looping through the​ h layers 
and adding up all the blocks along the way in each layer. However, if you happen to know some 
discrete math and combinatorics, you can come up with an analytical closed form formula for the 
result and compute the answers much faster that way. (There is an important general principle in 
this for you to ponder later on your own.) 
 
n     m     h     Expected result 
2     3     1     6 
2     3     10    570 
10    11    12    3212 
100   100   100   2318350 
10**6 10**6 10**6 2333331833333500000 

summation of  n+h-1 * m+h-1
"""

def pyramid_blocks(n,m,h):
  total = 0
  for index in range(h):
    total += (n+index)*(m+index)
  return total