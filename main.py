from random import randint
import networkx as nx
import tsplib95 as tsp
import numpy as np
from ga import GA


def readFileHard(filename):
    network = {}
    tsp_file = tsp.load_problem(filename)
    g = tsp_file.get_graph()
    nrCities = len(g.nodes())
    network['nrCities'] = nrCities
    matrix = nx.to_numpy_matrix(g)
    graph = []
    for i in range(nrCities):
        graph.append([])
        for j in range(nrCities):
            value = matrix.item((i, j))
            if value == 0:
                value += 1
            graph[i].append(value)
    print(nrCities)
    print(graph)
    network['mat'] = graph
    return network


def readFile(filename):
    f = open(filename, "r")
    network = {}
    nrCities = int(f.readline())
    network['nrCities'] = nrCities
    matAd = []
    for i in range(nrCities):
        matAd.append([])
        line = f.readline()
        elements = line.split(',')
        for j in range(nrCities):
            matAd[i].append(int(elements[j]))
    network['mat'] = matAd

    return network


def main():
    net = readFile("date2.txt")
    # print(net['mat'])
    dim = net['nrCities']

    problParams = {'dim': dim}
    gaParams = {'dimPop': 100, 'nrGen': 200}
    ga = GA(net['mat'], problParams, gaParams)
    ga.initPopulation()
    ga.evaluateFitness()

    maxFitness = -1
    bestRepres = []
    filename = "hardE_out.txt"
    f = open(filename, "w")

    for gen in range(gaParams['nrGen']):
        bestChrom = ga.bestChromosome()
        bestSolution = ga.bestChromosome().repres
        bestSolutionFitness = ga.bestChromosome().fitness

        if bestSolutionFitness > maxFitness:
            maxFitness = bestSolutionFitness
            bestRepres = bestSolution
        f.write("best chromosome in generation " + str(gen) + " is " + str(bestSolution) + " with distance = " + str(
            ga.getDistance(bestChrom))
                + " with fitness = " + str(bestSolutionFitness) + "\n")
        # ga.oneGeneration()
        ga.oneGenerationElitism()

    bestChromo = ga.bestChromosome()
    repres = bestChromo.repres
    repres.append(bestChromo.repres[0])
    # for i in range(len(repres)):
    #  repres[i] += 1

    f.write("best solution over all: " + str(repres) + " with distance = " + str(
        ga.getDistance(bestChromo)) + " and fitness = " + str(bestChromo.fitness) + "\n")
    f.close()


main()

main()
