import math

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


"""
Cyclops numbers 
 
def is_cyclops(n): 

A non-negative integer is said to be a​ cyclops number if it consists of an odd number of digits so
that the middle (or more poetically, the"eye") digit is a zero, and all other digits of that number are
non-zero. This function should determine whether its parameter integer​ n is a cyclops number, and
accordingly return either ​True​ or ​False​. 
 
n           Expected result 
0           True 
101         True 
98053       True 
777888999   False 
1056        False 
675409820   False 
 
(As an extra challenge, try to solve this problem using only loops, conditions and integer arithmetic
operations, without first converting the integer into a string and working from there. Note that
dividing an integer by 10 effectively chops off its last digit, whereas the remainder operator ​% can
be used to extract the last digit.)
"""

def is_cyclops(n):
  if n == 0:
    return True
  
  isCyclops = False
  count = 0  
  while n > 0:
    remainder = n % 10
    dividend = n // 10
    
    n = dividend  
    count += 1
    
    digits_in_dividend = math.ceil(math.log(dividend+1, 10))
    if ((count-1)==digits_in_dividend) and remainder==0:
      isCyclops = True
    elif ((count-1)!=digits_in_dividend) and remainder==0:
      isCyclops = False
      break
  return isCyclops

"""
Domino cycle 
 
def domino_cycle(tiles): 

A single ​domino tile is represented as a two-tuple of its​ pip values​, for example​ (2, 5) or​ 
(6, 6)​. This function should determine whether the given list of ​tiles forms a​ cycle so that each tile in 
the list ends with the exact same pip value that its successor tile starts with, the success or of the last 
tile being the first tile of the list since this is supposed to be a cycle instead of a chain. Return ​True if 
the given list of domino tiles form such a cycle, and ​False​ otherwise. 
 
tiles                       Expected result 
[(3, 5), (5, 2), (2, 3)]    True 
[(4, 4)]                    True 
[]                          True 
[(2, 6)]                    False 
[(5, 2), (2, 3), (4, 5)]    False 
[(4, 3), (3, 1)]            False 
"""
def domino_cycle(tiles): 
  if len(tiles) == 0:
    return True
  
  first_tile_pip = tiles[0][0]

  for index in range(len(tiles)):
    if index == len(tiles)-1:
      if first_tile_pip == tiles[index][1]:
        return True
      else:
        return False
    if tiles[index][1] == tiles[index+1][0]:
      continue
    else:
      return False


"""
Count dominators 
 
def count_dominators(items): 

An element of ​items is said to be a ​dominator if every element to its right is strictly smaller than it. 
This function should count how many elements in the given list of ​items are dominators, and 
return that count. For example, in the list ​[42, 7, 12, 9, 2, 5]​, the elements 42, 12, 9 and 5 
are dominators. By this definition, the last item of the list is automatically a dominator. 
 
Before starting to write any code for this function, please read and think about the tale of "​Shlemiel 
the painter​" and how this seemingly silly little tale from a far simpler time might relate to today's
computational problems for lists, strings and other sequences. This problem will be the first of
many that you will encounter during and after this course to illustrate the important principle of
using only one loop to achieve in a tiny fraction of time the same end result that Shlemiel needs two
nested full loops to achieve, your workload therefore increasing only ​linearly with respect to the
number of ​items instead of ​quadratically (that is, as a function of the ​square of the number of
items), the same way that Shlemiel's painting and running task will increase as the fence gets
longer. 
 
items                     Expected result 
[42, 7, 12, 9, 2, 5]      4 
[]                        0 
[99]                      1 
[42, 42, 42, 42]          1 
list(range(10**7))        1 
list(range(10**7, 0, -1)) 10000000   
"""
def count_dominators(items): 
  
  dominator = 0
  if len(items) == 0:
    return dominator 

  max_item = items[-1]
  dominator = 1

  for index in range(len(items)-1,-1,-1):
    if (index >= 1) and (items[index-1] > max_item):
      max_item = items[index-1]
      dominator += 1

  return dominator    

"""
Extract increasing integers from digit string 
 
def extract_increasing(digits): 
 
Given a string of digits guaranteed to consist of ordinary integer digit characters 0 to 9 only, create 
and return the list of increasing integers acquired from reading these digits in order. The first 
integer in the result list is made up from the first digit of the string. After that, each element is an 
integer that consists of as many following consecutive digits as are needed to make that integer 
strictly larger than the previous integer. Any leftover digits at the end of the digit string that do not 
together form a sufficiently large integer are discarded. 
 
digits                              Expected result 
'0'                                 [0] 
'045349'                            [0, 4, 5, 34] 
'77777777777777777777777'           [7, 77, 777, 7777, 77777, 777777] 
'122333444455555666666'             [1, 2, 23, 33, 44, 445, 555, 566, 666] 
'1234567890987654321'               [1, 2, 3, 4, 5, 6, 7, 8, 9, 98, 765, 4321] 
'3141592653589793238462643          [3, 14, 15, 92, 653, 5897, 9323, 84626, 433832, 795028]
383279502884' 
 
'​2718281828459045235360287          [2, 7, 18, 28, 182, 845, 904, 5235, 36028,
47135266249775724709369995          74713, 526624, 977572, 4709369, 9959574,
95749669676277240766303535          96696762, 772407663, 3535475945, 7138217852,
47594571382178525166427427          51664274274, 66391932003, 599218174135,
46639193200305992181741359          966290435729] 
6629043572900334295260​' 
    
'123456789' * 100                   A list that contains 75 elements, the last one of which equals 
                                    34567891234567891234567891 
""" 
def extract_increasing(digits):
  list_increasing = []
  int_current_biggest = -1
  str_next_biggest = ""
  for index in range(len(digits)):
    str_next_biggest = str_next_biggest + digits[index]
    int_next_biggest = int(str_next_biggest)
    if int_next_biggest > int_current_biggest:
      list_increasing.append(int_next_biggest)
      int_current_biggest = int_next_biggest
      str_next_biggest = ""
  return list_increasing

"""
Words that contain given letter sequence 
 
def words_with_letters(words, letters): 

Given a list of​ words sorted in alphabetical order, and a string of required ​letters​, find and return
the list of precisely those words that contain the letters inside them in the exact order given, but not
necessarily in consecutive positions. 
 
letters           Expected result (using the wordlist ​words_sorted.txt​) 
'antmneic'        ['antiferromagnetic', 'antimagnetic', 'antimnemonic', 
                   'aquopentamminecobaltic', 'pantomnesic', 'phantasmogenetic'] 
'unskit'          ['underskirt', 'underskirts', 'unshockability', 
                   'unshrinkability', 'unsinkability', 'unskaithd', 'unskaithed', 
                   'unskirted', 'unspeakability'] 
'rupih'           ['frumpish', 'frumpishly', 'frumpishness', 'grumpish', 
                   'grumpishness', 'porcupinish', 'rupiah', 'rupiahs', 
                   'trumpetfish', 'trumpetfishes'] 
'reeomy'          A list of 54 words, the first three of which are ​
                  ['adrenalectomy', 'arteriectomy', 'arteriophlebotomy']​ 
                  and the last three are 
                  ['ureterotomy', 'urethrectomy', 'vertebrectomy']   

"""

def read_words(word_file):
  wordList = [line.rstrip('\n') for line in open(word_file)]
  return wordList

def words_with_letters(words, letters): 
  matchList = []
  for word in words:
    currentIndex = 0
    for letterIndex in range(len(letters)):
      if word.find(letters[letterIndex], currentIndex) > -1:
          currentIndex = word.find(letters[letterIndex], currentIndex) + 1
          if letterIndex == len(letters) - 1:
            matchList.append(word)
      else:
        break

  return matchList

"""
Taxi zum zum 
 
def taxi_zum_zum(moves): 

A Manhattan taxicab starts at the origin point​(0, 0) of the two-dimensional integer grid, initially
heading north. It then executes the given sequence of ​moves​, a string made up of characters​ 'L' ​for
turning 90 degrees left (while standing in place), ​'R' for turning 90 degrees right (ditto), and '​F​' for
moving one step forward according to its current heading. This function should return the final
position of the taxicab in the integer grid coordinates of Manhattan. 
 
moves                   Expected result 
'RFRL'                  (1, 0) 
'LLFLFLRLFR'            (1, 0) 
'FR' * 1000             (0, 0) 
'FFLLLFRLFLRFRLRRL'     (3, 2) 
 
(As an aside, why do these problems always seem to take place in Manhattan instead of, say, Denver
where the street grid is rotated 45 degrees from the main compass axes to equalize the amount of
daily sunlight on streets of both orientations? That should make an interesting variation to many
problems of this spirit. Of course, diagonal moves always maintain the parity of the coordinates,
which makes it impossible to reach any coordinates of the opposite parity, quite like in that old joke
with the punchline "Gee... I don't think that you can get there from here.")    
"""

def taxi_zum_zum(moves): 
  totalheading = 0
  posx = 0
  posy = 0
  for move in moves:
    if move == "R":
      totalheading += 90
    elif move == "L":
      totalheading -= 90
    elif move == "F":
      heading = totalheading % 360
      if heading < 0:
        heading = 360 - heading

      if heading == 0:
        posy += 1
      elif heading == 90:
        posx += 1
      elif heading == 180:
        posy -= 1
      elif heading == 270:
        posx -= 1

  return (posx, posy)

"""
Count growlers 
 
def count_growlers(animals): 

Let the strings ​'cat' and ​'dog' denote that kind of animal facing left, and ​'tac' and ​'god'
denote that same kind of animal facing right. Each individual animal, regardless of its own species,
growls if there are more dogs than cats following that position in the direction that the animal is
facing. Given a list of such ​animals​, return the count of how many of them are growling. 
 
animals                                                   Expected result 
['cat', 'dog']                                            0 
['god', 'cat', 'cat', 'tac', 'tac', 'dog', 'cat', 'god']  2 

['dog', 'cat', 'dog', 'god', 'dog', 'god', 'dog', 'god',  11
'dog', 'dog', 'god', 'god', 'cat', 'dog', 'god', 'cat', 
'tac'] 
 
['god', 'tac', 'tac', 'tac', 'tac', 'dog', 'dog', 'tac',  0
'cat', 'dog', 'god', 'cat', 'dog', 'cat', 'cat', 'tac'] 
 
 
(I admit that I was pretty high when I originally thought up this problem, at least high enough to
perceive the letter 't' as a tail of a happy cat held up high, and 'd' as the snout and stand-up ears of a
curious dog, perhaps some kind of spitz or a similar breed. Yeah, good luck trying to unsee that
now. For some reason, this problem is somehow more tricky than it seems.)   
"""
def count_growlers(animals): 
  growlers = 0
  
  for animalIndex in range(len(animals)):
    if (animals[animalIndex] == "cat") or (animals[animalIndex] == "dog"):  # look left
      countCats = 0
      countDogs = 0
      for subAI in range(0, animalIndex):
        if (animals[subAI] == "cat") or (animals[subAI] == "tac"):
          countCats +=1
        elif (animals[subAI] == "dog") or (animals[subAI] == "god"):
          countDogs +=1
      if (countDogs > countCats):
        growlers += 1    

    elif (animals[animalIndex] == "tac") or (animals[animalIndex] == "god"): # look right
      countCats = 0
      countDogs = 0
      for subAI in range(animalIndex+1, len(animals)):
        if (animals[subAI] == "cat") or (animals[subAI] == "tac"):
          countCats +=1
        elif (animals[subAI] == "dog") or (animals[subAI] == "god"):
          countDogs +=1
      if (countDogs > countCats):
        growlers += 1    

  
  return growlers


"""
Bulgarian solitaire 
 
def bulgarian_solitaire(piles, k): 

You are given a row of ​piles of pebbles and a positive integer ​k so that the total number of pebbles
in these piles equals ​k*(k+1)//2​, a formula that just so happens to equal the sum of all positive
integers from ​1 to ​k​. As if a metaphor for the bleak life behind the Iron Curtain, all pebbles are
identical and you don't have any choice in the moves that you make. Each move must pick up
exactly one pebble from each pile (even if doing so makes that pile disappear), and create a new pile
from these collected pebbles. For example, starting with ​piles = [7, 4, 2, 1, 1]​, the first
move would turn this into ​[6, 3, 1, 5]​. The next move turns this into ​[5, 2, 4, 4]​, which
then turns into ​[4, 1, 3, 3, 4]​, and so on.

This function should count how many moves are needed to convert the given initial ​piles into
some permutation of first ​k integers so that each number from ​1 to ​k appears as the size of ​exactly
one pile in the current configuration, and return that count. (Note how once this goal state has
been reached, the basic move does not change the configuration.) 
 
piles                               k       Expected result 
[1, 4, 3, 2]                        4       0 
[8, 3, 3, 1]                        5       9 
[10, 10, 10, 10, 10, 5]             10      74 
[3000, 2050]                        100     7325 
[2*i-1 for i in range(171, 0, -2)]  171     28418 

(This problem was inspired by the old ​Martin Gardner column "Bulgarian Solitaire and Other
Seemingly Endless Tasks" where it was used as an example of what we would here call a while-loop
where it is not immediately obvious that the loop will ever reach its goal and get to terminate.
However, clever combinatorial proof shows that this one simple move can never get stuck, but will
always reach the goal after at most ​k(​k-1)/2 iterations from any starting configuration.) 
"""  
def bulgarian_solitaire(piles, k): 
  flag = True
  count = 0
  enum_list = [i for i in range(1, k+1)]
  while flag==True:
    for i in enum_list:
      if i not in piles:
        count += 1
        newpile = 0
        tempPiles = []
        for pile in piles:
          adjpile = pile - 1
          newpile += 1
          if adjpile > 0:
            tempPiles.append(adjpile)
        tempPiles.append(newpile)
        piles = tempPiles
        break
      elif i >= len(enum_list):
        flag=False
  return count

