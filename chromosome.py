from random import randint

from utils import generateRandomPerm


class Chromosome:

    def __init__(self, problParams=None):
        self.__problParams = problParams
        self.__repres = generateRandomPerm(self.__problParams['dim'])
        self.__fitness = 0.0

    @property
    def fitness(self):
        return self.__fitness

    @property
    def repres(self):
        return self.__repres

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, parent2):
        #ordered crossover
        pos1 = randint(-1, self.__problParams['dim'] - 1)
        pos2 = randint(-1, self.__problParams['dim'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in parent2.__repres[pos2:] + parent2.__repres[:pos2]:
            if el not in newrepres:
                if len(newrepres) < self.__problParams['dim'] - pos1:
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__problParams)
        offspring.repres = newrepres
        return offspring

    def mutate(self):
        #swap mutation
        pos1 = randint(0, self.__problParams['dim'] - 1)
        pos2 = randint(0, self.__problParams['dim'] - 1)
        self.__repres[pos1], self.__repres[pos2] = self.__repres[pos2], self.__repres[pos1]

    def __str__(self):
        return '\nChromosome: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
