import random
import individual as ind

MAX_POP = 50
ELITES = 6


class Population:

    def __init__(self, members):
        self.members = members

        if len(members) == 0:
            self.populate()

        if len(members) > MAX_POP:
            print("ERROR : POPULATION OVERFLOW")
            self.members = members[:MAX_POP]

            
    # Fill population with random individuals
    def populate(self):
        while len(self.members) < MAX_POP:
            self.members.append(ind.make_rand_individual())

    def get_elites(self):
        parents = self.get_parents()
        return parents[0:ELITES]

    # Returns best half of the population
    def get_parents(self):
        members = self.members
        n = len(members)
        for i in range(n):

            for j in range(0,n-i-1):
            
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if members[j].fitness < members[j+1].fitness : 
                    members[j], members[j+1] = members[j+1], members[j]
        
        return members[:int(MAX_POP/2)]

    # Create and return children from the parents
    def get_children(self, parents):
        # calculate pop. size
        pop_size = len(parents)

        # calculate sum fitness
        sum_fitness = 0
        for parent in parents:
            sum_fitness += parent.fitness

        # Mate until children is full
        children = []
        while len(children) < MAX_POP - ELITES:
            parent_1 = self.select_parent(parents, sum_fitness)
            parent_2 = self.select_parent(parents, sum_fitness)

            childs = self.crossover(parent_1, parent_2)
            children.append(childs[0])
            children.append(childs[1])

        return children[0:MAX_POP]


    def select_parent(self, parents, sum_fit):
        # spin roulette wheel
        roulette = random.randint(0, sum_fit)
        temp = roulette

        # select corresponding member
        index = 0
        for parent in parents:

            if parent.fitness >= roulette: # Select this member
                return parent

            else: # Don't select this member
                roulette -= parent.fitness
                index += 1
                
        print("{},{},{}".format(sum_fit, temp, roulette))
        return parents[0]

    
    # From two parents, return two children
    def crossover(self, parent_1, parent_2):
        children = []

        # 1-point crossover
        max_string = len(parent_1.chrom_a)
        pcross_a = random.randint(0, max_string)
        pcross_b = random.randint(0, max_string)

        # Chromosomes for child 1
        chrom_1a = parent_1.chrom_a[:pcross_a] + parent_2.chrom_a[pcross_a:]
        chrom_1b = parent_1.chrom_b[:pcross_b] + parent_2.chrom_b[pcross_b:]

        chrom_2a = parent_2.chrom_a[:pcross_a] + parent_1.chrom_a[pcross_a:]
        chrom_2b = parent_2.chrom_b[:pcross_b] + parent_1.chrom_b[pcross_b:]

        child_1 = ind.Individual(chrom_1a, chrom_1b)
        child_2 = ind.Individual(chrom_2a, chrom_2b)

        child_1.mutate()
        child_2.mutate()

        children.append(child_1)
        children.append(child_2)

        return children


    def statistics(self):
        best_memb = self.members[0]
        worst_memb = self.members[0]
        sum_fitness = 0
        
        for member in self.members:
            # check best
            if member.fitness > best_memb.fitness:
                best_memb = member

            # check worst
            if member.fitness < worst_memb.fitness:
                worst_memb = member

            # sum
            sum_fitness += member.fitness

        avg_fitness = sum_fitness / len(self.members)

        print("Pop. Size : {} \nBest : {} \nWorst : {} \nAvg : {} \nSum : {}".format(len(self.members), best_memb.fitness, worst_memb.fitness, avg_fitness, sum_fitness ))
        print()
        return
    



        
