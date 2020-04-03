from random import randint


def generateRandomPerm(dim):
      perm = [i for i in range(0, dim)]
      pos1 = randint(1,dim-1)
      pos2 = randint(1,dim-1)
      perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
      return perm