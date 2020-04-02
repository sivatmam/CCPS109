

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


