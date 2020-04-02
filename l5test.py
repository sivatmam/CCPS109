


# data structure is taken from w3school
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011,
    "date":[2001,2007,2011,2020,2022]
  }
}
# try printing different values for the children
# update the child info with new key/value pair

#print(myfamily['child1']['year'])

w=dict([(1, 4139), ('guido', 4127), ('jack', 4098)]) #constructor for creating dictionaries
a={'aa':2323,213.11:2324}
print(a.values())

newdict=dict(_s1=4139, guido=4127, jack=4098)
#print(newdict)
for k, v in newdict.items():
    print(k, v)


