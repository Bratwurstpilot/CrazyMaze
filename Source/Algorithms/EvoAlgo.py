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


class Individual:

    def __init__(self, genes : list = []):

        self.genes = genes
        self.fitness = 0.0

    
    def setFitness(self, fitness : float):

        self.fitness = fitness


class EvoAlgo(AStar):

    def __init__(self, populationCount = 10,  symbols: dict = ...):

        super().__init__(symbols)

        self.population : list = [Individual([randint(0,1) for __ in range(10)]) for _ in range(populationCount)]

        for individual in self.population:
            self.fitness(individual)

        self.timer = Timer(0.04) #40ms


    def crossover(self, individuals : list) -> Individual:
        '''
        Uniform Crossover - Choose each bit from parents
        with equal probability
        '''
        child : Individual = Individual([0 for _ in range(len(individuals[0].genes))])
        for i in range(len(individuals[0].genes)):
            choice = randint(0,len(individuals)-1)
            child.genes[i] = individuals[choice].genes[i]
        
        self.fitness(child)
        return child


    def mutate(self, individual : Individual) -> None:

        choice = randint(0,len(individual.genes)-1)
        individual.genes[choice] = 1 - individual.genes[choice]
        self.fitness(individual)


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

    
    def fitness(self, individual : Individual) -> None:

        expected = [1 for _ in range(10)]

        fitness : int = 0
        for indx, bit in enumerate(individual.genes):
            if bit == expected[indx]:
                fitness += 1
        
        individual.fitness = fitness
            

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

while not algo.update():

    print("\nEpoch ", epoch, " : ")
    epoch += 1

    for individual in algo.population:
        print(individual.genes, " : ", individual.fitness)

print("\nEpoch ", epoch, " : ")
epoch += 1
    
for individual in algo.population:
    print(individual.genes, " : ", individual.fitness)