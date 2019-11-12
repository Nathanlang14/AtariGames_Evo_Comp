import population as popu


MAX_GEN = 1000

def main():
    
    # Initialize
    gen = 1
    pop = popu.Population([])
    
    while gen < MAX_GEN:
        children = []

        # Print statistics of population
        print("Generation : {}".format(gen))
        pop.statistics()

        # Get elites
        elites = pop.get_elites()
        
        # Get parents
        parents = pop.get_parents()

        # Make children
        children = pop.get_children(parents.copy())

        # Make next population
        next_pop = children.copy()
        for elite in elites:
            next_pop.append(elite)

        # Make new population
        new_pop = popu.Population(next_pop.copy())
        pop = new_pop

        gen += 1


    # Termination code here
    print("\n\n\n\n")
    print("Done!")
    print("Generation : {}".format(gen))
    pop.statistics()

    return gen

main()
