from random import randint
from random import shuffle
from math import sqrt

from Source.Algorithms.Pathfinding import AStar


class Individual:

    def __init__(self, genes : list = []):

        self.genes : list = genes
        self.fixedPoints : list = []
        self.fitness : float = 0.0

    
    def setFitness(self, fitness : float):

        self.fitness = fitness


class EvoAlgo():

    def __init__(self, populationCount : int = 10, points : list = [(0,0)], fixedStart : tuple = (0,0), bestEstimate : float = 100000, maxIterations : int = 1000, metric : str = "AStar") -> None:
        '''
        metric -> Manhatten | AStar
        '''
        self.population : list = []
        self.populationCount = populationCount

        self.bestEstimate : float = bestEstimate
        self.iter : int = 0
        self.maxIter : int = maxIterations

        self.fixedStart : tuple = fixedStart
        self.fixedEnd : tuple = (0,0)

        self.points : list = points.copy()

        self.setPopulation(points)

        self.viewSpace : list = None
        self.distances : list = []

        #for individual in self.population:
            #self.fitness(individual)
        
        gb = Individual([])
        gb.fitness = 100000
        self.globalBest : list = [gb, 0]

        self.metric = metric
    

    def reset(self) -> None:
        
        self.population = []
        self.viewSpace = []
        self.distances = []
        self.iter : int = 0


    def setPopulation(self, points) -> None:

        for _ in range(self.populationCount):
            self.population.append(Individual(points.copy()))
            shuffle(points)


    def crossoverNPoint(self, individuals : list) -> list:
        '''
        Uniformly crossover individuals at 2 points at 
        est. 1/3 and 2/3 of the length of the genome.
        '''
        parent1 = Individual(individuals[0].genes)

        parent2 = Individual(individuals[1].genes)

        nPoint1 = int(len(parent1.genes) * (0.33))
        nPoint2 = int(len(parent1.genes) * (0.66))

        newIndividual1 = Individual([0 for _ in range(len(parent1.genes))])
        newIndividual2 = Individual([0 for _ in range(len(parent2.genes))])

        for i in range(nPoint1):
            newIndividual1.genes[i] = parent1.genes[i]
            newIndividual2.genes[i] = parent2.genes[i]
        for i in range(nPoint1, nPoint2):
            newIndividual1.genes[i] = parent2.genes[i]
            newIndividual2.genes[i] = parent1.genes[i]
        for i in range(nPoint2, len(parent1.genes)):
            newIndividual1.genes[i] = parent1.genes[i]
            newIndividual2.genes[i] = parent2.genes[i]
        
        return [newIndividual1, newIndividual2]


    def crossover(self, individuals : list, pX) -> list:
        '''
        Uniformly ordered Crossover.
        Probability measure x >= pX? -> change genes with pX in [0;10]
        '''
        offSpring1 = Individual(individuals[0].genes)
        #offSpring1.fitness = individuals[0].fitness

        offSpring2 = Individual(individuals[1].genes)
        #offSpring2.fitness = individuals[1].fitness
        
        changedGenesIndex : list = [] #What genes should be exchanged with respect to prob. pX
        changedGenesP1 : list = []
        changedGenesP2 : list = []

        changeVar : int = randint(0, len(offSpring1.genes)-1)
        while len(changedGenesIndex) < changeVar:
            choice = randint(0,len(offSpring1.genes)-1)
            if choice not in changedGenesIndex:
                changedGenesIndex.append(choice)
        
        for i in range(len(offSpring1.genes)):
            if randint(0,10) <= pX and i not in changedGenesIndex:
                changedGenesIndex.append(i)
        
        changedGenesIndex.sort()
        for index in changedGenesIndex:
            changedGenesP1.append(offSpring1.genes[index])
            changedGenesP2.append(offSpring2.genes[index])
        
        genesP1InOrder = list(filter(lambda x : x in changedGenesP2, offSpring1.genes))
        genesP2InOrder = list(filter(lambda x : x in changedGenesP1, offSpring2.genes))

        for i in range(len(changedGenesIndex)):
            offSpring1.genes[changedGenesIndex[i]] = genesP2InOrder[0]
            genesP2InOrder.remove(genesP2InOrder[0])
            offSpring2.genes[changedGenesIndex[i]] = genesP1InOrder[0]
            genesP1InOrder.remove(genesP1InOrder[0])
        
        return [offSpring1, offSpring2]
    

    def mutate(self, individual : Individual, pX) -> None:

        if randint(0,10) <= pX:
            choice = [randint(0, len(individual.genes))-1, randint(0, len(individual.genes))-1]
            individual.genes[choice[0]], individual.genes[choice[1]] = individual.genes[choice[1]], individual.genes[choice[0]]


    def fitness(self, individual : Individual, penalty = 5) -> None:

        individual.fitness = 0.0
        
        
        if len(individual.genes) > 0:
            first = individual.genes[0]
            individual.fitness += sqrt( (self.fixedStart[0] - first[0])**2 + (self.fixedStart[1] - first[1])**2 ) * 3
            #last = individual.genes[-1]
            #individual.fitness += sqrt( (self.fixedEnd[0] - last[0])**2 + (self.fixedEnd[1] - last[1])**2 ) * 3
        

        for i in range(len(individual.genes)-1):
            current = individual.genes[i]
            succ = individual.genes[i+1]

            #Manhatten distance
            if self.metric == "Manhatten":
                individual.fitness += abs(succ[0] - current[0]) + abs(succ[1] - current[1])

            #AStar Distance
            elif self.metric == "AStar":
                for i in range(0, len(self.distances), 2):
                    if self.distances[i] == (current, succ) or self.distances[i] == (succ, current):
                        individual.fitness += self.distances[i+1]

            #Reward for taking Coins in itselfs Boardhalf
            distToEnd = abs(self.fixedEnd[0] - current[0]) + abs(self.fixedEnd[1] - current[1])
            distToStart = abs(self.fixedStart[0] - current[0]) + abs(self.fixedStart[1] - current[1])

            if i < len(individual.genes) // 2:
                if distToEnd < distToStart:
                    individual.fitness += penalty


    def selection(self, count = 2, turnamentSize = 10, preselected : int = 1) -> list:

        selected : list = []

        while len(selected) < turnamentSize:

            individual1 = self.population[randint(0,len(self.population)-1)]
            individual2 = self.population[randint(0,len(self.population)-1)]

            if individual1.fitness <= individual2.fitness and individual1 not in selected:
                selected.append(individual1)
            elif individual2 not in selected:
                selected.append(individual2)
        
        selected.sort(key=lambda x:x.fitness)

        return selected[0:count]


    def update(self) -> bool:
        
        #Options for evoAlgo
        probMutation = 2
        probCrossover = 8
        fitnessPenalty = 5

        #Interupt if there are only 2 points
        if len(self.population[0].genes) < 2:
            return True
        
        #update iteration count
        self.iter += 1

        #save population size
        populationSize : int = len(self.population)

        #Recombination
        parents = [self.selection(2,10,0) for _ in range(int(len(self.population)*0.5))]

        for pair in parents:
            for newMember in self.crossover(pair, probCrossover):
                self.population.append(newMember)
        
        #Environmental selection
        self.population.sort(key=lambda x : x.fitness, reverse=False)
        newGeneration : list = self.selection(count = populationSize-3, preselected = 3)
 
                #Elitism
        newGeneration.append(self.population[0])
        newGeneration.append(self.population[1])
        newGeneration.append(self.population[2])

        #newGeneration = self.population[0::populationSize]
        self.population = newGeneration

        #Mutation
        for individual in self.population:
            self.mutate(individual, probMutation)

            #Update fitness
            self.fitness(individual, fitnessPenalty)

            if individual.fitness <= self.globalBest[0].fitness:
                self.globalBest[0] = Individual(individual.genes.copy())
                self.globalBest[0].fitness = individual.fitness
                self.globalBest[1] = self.iter

            print(self.globalBest[0].fitness)

            if self.bestEstimate != None:
                if individual.fitness <= self.bestEstimate:
                    #print("Optimal individual : ", individual.genes, " f: ", individual.fitness)
                    #print("Global Best   at :", self.globalBest[0].genes, " f: ", self.globalBest[0].fitness, " after ", self.globalBest[1], " iterations")
                    return True

        if self.iter >= self.maxIter:
            bestIndividual = min(self.population, key= lambda x : x.fitness)
            #print("Best solution at :", bestIndividual.genes, " f: ", bestIndividual.fitness, " after ", self.iter, " iterations")
            #print("Global Best   at :", self.globalBest[0].genes, " f: ", self.globalBest[0].fitness, " after ", self.globalBest[1], " iterations")
            return True
        
        self.update()

    
    def setUp(self, viewSpace_ : list = [[]], symbols : dict = {}) -> None:
        '''
        Setup should be executed after the population is set (Constructor or manually). 
        Here the AStar calculations are made.
        '''
        print("Starting Setup...")
        
        if self.metric == "Manhatten":
            print("Finished Setup")
            return
        
        self.viewSpace = []
        self.symbols = symbols

        for line in viewSpace_:
            self.viewSpace.append(line.copy())

        for i in range(len(self.points)):
            for j in range(len(self.points)):
                point1 = self.points[i]
                point2 = self.points[j]

                if point1 == point2:
                    continue

                if (point1, point2) not in self.distances and (point2, point1) not in self.distances:
                    distance : int = len(self.getPath(point1, point2))
                    self.distances.append((point1, point2))
                    self.distances.append(distance)
        
        print("Finished Setup")


    def getPath(self, start_, end_) -> list:

        aStar = AStar(symbols=self.symbols)

        viewSpace = []

        for element in self.viewSpace:
            viewSpace.append(element.copy())

        viewSpace[start_[1]][start_[0]] = self.symbols["Start"]
        viewSpace[end_[1]][end_[0]] = self.symbols["End"]

        aStar.viewSpace = viewSpace

        aStar.execRoutine()
        path = aStar.getPath().copy()

        path.remove(path[-1])
        aStar.__del__()

        return path