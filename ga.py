from random import randint

from chromosome import Chromosome


class GA:
    def __init__(self, mat, problParams=None, gaParams=None):
        self.__mat = mat
        self.__problParams = problParams
        self.__gaParams = gaParams
        self.__population = []

    @property
    def population(self):
        return self.__population

    def functionEval(self, c):

        if c.fitness == 0:
            return 1 / float(self.getDistance(c))
        # costTotal = 0
        # for i in range(0, len(repres) - 1):
        #   costTotal += self.__mat[repres[i]][repres[i + 1]]
        # fitness = 1 / costTotal
        else:
            return c.fitness

    def getDistance(self, c):
        costTotal = 0
        for i in range(0, self.__problParams['dim']):
            from_chromo = c.repres[i]
            if i + 1 < self.__problParams['dim']:
                dest_chromo = c.repres[i + 1]
            else:
                dest_chromo = c.repres[0]

            costTotal += self.__mat[from_chromo][dest_chromo]
        return costTotal


    def initPopulation(self):
        for _ in range(0, self.__gaParams['dimPop']):
            c = Chromosome(self.__problParams)
            self.__population.append(c)

    def evaluateFitness(self):
        for c in self.__population:
            c.fitness = self.functionEval(c)

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def tournamentSelection(self):
        tournament = []
        for i in range(0, 3):
            random = randint(0, self.__problParams['dim'] - 1)
            tournament.append(self.__population[i])

        fittest = tournament[0]
        for cromo in tournament:
            if cromo.fitness > fittest.fitness:
                fittest = cromo
        return fittest

    def oneGeneration(self):
        newPopulation = []
        for _ in range(self.__gaParams['dimPop']):
            parent1 = self.tournamentSelection()
            parent2 = self.tournamentSelection()
            offspring = parent1.crossover(parent2)
            offspring.mutate()
            newPopulation.append(offspring)
        self.__population = newPopulation
        self.evaluateFitness()

    def oneGenerationElitism(self):
        newPopulation = [self.bestChromosome()]
        for _ in range(self.__gaParams['dimPop'] - 1):
            parent1 = self.tournamentSelection()
            parent2 = self.tournamentSelection()
            offspring = parent1.crossover(parent2)
            offspring.mutate()
            newPopulation.append(offspring)
        self.__population = newPopulation
        self.evaluateFitness()
