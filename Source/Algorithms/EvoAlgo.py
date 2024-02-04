from Pathfinding import AStar
from random import randint

class Timer:

    def __init__(self, time = 1.0):

        self.count = 0
        self.TICKMAX = time

    
    def tick(self) -> bool:

        self.count += 1

        if self.count >= self.TICKMAX:
            self.count = 0
            return True
        
        return False


class pointDist:

    def __init__(self):

        self.nextPoints : list = []
        self.distances : list = []


class Individual:

    def __init__(self, genes : list = []):

        self.genes : list = genes
        self.fitness : float = 0.0

    
    def setFitness(self, fitness : float):

        self.fitness = fitness


class EvoAlgo(AStar):

    def __init__(self, populationCount = 10, fitnessFunc = None, fitnessParam = [],  symbols: dict = ...):

        super().__init__(symbols)

        self.population : list = [Individual([randint(0,1) for __ in range(10)]) for _ in range(populationCount)]
        self.fitnessFunc = fitnessFunc
        self.fitnessParam = fitnessParam

        for individual in self.population:
            self.fitness(individual)

        self.timer = Timer(0.04) #40ms


    def crossover(self, individuals : list, pX) -> Individual:
        '''
        Uniformly ordered Crossover.
        Probability measure x >= pX? -> change genes with pX in [0;10]
        '''
        parent1 = individuals[0]
        parent2 = individuals[1]
        
        changedGenesIndex : list = [] #What genes should be exchanged with respect to prob. pX
        changedGenesP1 : list = []
        changedGenesP2 : list = []

        while len(changedGenesIndex) < 2:
            choice = randint(0,len(parent1.genes)-1)
            if choice not in changedGenesIndex:
                changedGenesIndex.append(choice)
        
        for i in range(len(parent1.genes)):
            if randint(0,10) >= pX and i not in changedGenesIndex:
                changedGenesIndex.append(i)
        
        changedGenesIndex.sort()
        for index in changedGenesIndex:
            changedGenesP1.append(parent1.genes[index])
            changedGenesP2.append(parent2.genes[index])

        print(changedGenesIndex, "\n")
        
        genesP1InOrder = list(filter(lambda x : x in changedGenesP2, parent1.genes))
        genesP2InOrder = list(filter(lambda x : x in changedGenesP1, parent2.genes))

        print(genesP1InOrder)
        print(genesP2InOrder, "\n")
        for i in range(len(changedGenesIndex)):
            parent1.genes[changedGenesIndex[i]] = genesP2InOrder[0]
            genesP2InOrder.remove(genesP2InOrder[0])
            parent2.genes[changedGenesIndex[i]] = genesP1InOrder[0]
            genesP1InOrder.remove(genesP1InOrder[0])
        

    def mutate(self, individual : Individual, pX) -> None:

        if randint(0,10) > pX:
            choice = [randint(0, len(individual.genes)), randint(0, len(individual.genes))]
            individual.genes[choice[0]], individual.genes[choice[1]] = individual.genes[choice[1]], individual.genes[choice[0]]


    def fitness(self, individual : Individual) -> None:
        
        #return self.fitnessFunc(*self.fitnessParam)
        pass

    def selection(self, count = 2) -> list:

        selected : list = []

        while len(selected) < count:

            individual1 = self.population[randint(0,len(self.population)-1)]
            individual2 = self.population[randint(0,len(self.population)-1)]

            if individual1.fitness >= individual2.fitness and individual1 not in selected:
                selected.append(individual1)
            elif individual2 not in selected:
                selected.append(individual2)
        
        return selected


    def update(self) -> bool:
        
        #save population size
        populationSize : int = len(self.population)

        #Recombination
        parents = [self.selection(2) for _ in range(5)]

        for pair in parents:
            self.population.append(self.crossover(pair))
        
        #Environmental selection
        self.population.sort(key=lambda x : x.fitness, reverse=True)
        newGeneration : list = self.selection(populationSize-3)

                #Elitism
        newGeneration.append(self.population[0])
        newGeneration.append(self.population[1])
        newGeneration.append(self.population[2])

        self.population = newGeneration.copy()

        #Mutation
        for individual in self.population:
            if randint(0,10) >= 6:
                self.mutate(individual)

        #Update fitness
        for individual in self.population:
            self.fitness(individual)
            if individual.fitness >= 10:
                return True
            

#Testing
            
algo = EvoAlgo(10)
epoch = 1

p1 = Individual([0,1,2,3,4])
p2 = Individual([4,3,2,1,0])

algo.crossover([p1,p2], 7)
print(p1.genes)
print(p2.genes)

print("\n iter 2 \n")

algo.crossover([p1,p2], 7)
print(p1.genes)
print(p2.genes)

print("\ntest mutation with p1 : ", p1.genes)
algo.mutate(p1, 7)
print("result : ", p1.genes)