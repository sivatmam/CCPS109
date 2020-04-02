import itertools 

def is_ascending_generator(n):
    for i in range(n):
        for seq in itertools.permutations(range(n)):
            yield [seq]

for j in is_ascending_generator(3):
  print(j, end ="|||")