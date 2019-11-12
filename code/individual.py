import random
import gym

# Actions
# 0 : do nothing?
# 1 : shoot ball
# 2 : move right
# 3 : move left

MAX_STRING = 7
MUT_PROB = 0.25

class Individual:

    def __init__(self, chrom_ball, chrom_paddle):
        # chromosome : bit string
        self.chrom_a = chrom_ball
        self.chrom_b = chrom_paddle
        
        self.bx = self.decode( chrom_ball )
        self.px = self.decode( chrom_paddle )
        
        self.mut_prob = MUT_PROB
        self.fitness = self.fitness(False)

    def decode(self, chromosome ):
        """ Convert bit string to integer """
        numb = int(chromosome, 2)

        return numb

    def mutate(self):
        # set threshold : mut_prob = float
        threshold = self.mut_prob

        # generate random number [0-1]
        numb = random.uniform(0, 1)

        # check if we should mutate chromosome a
        mutate = (numb <= threshold)

        # mutate if necessary
        if mutate:
            # get chromosome
            chrom = self.chrom_a
            
            # invert a random bit of the chromosome
            mut_index = random.randint(0, MAX_STRING - 1)
            bit = chrom[mut_index]
            if bit == '1':
                bit = '0'
            else:
                bit = '1'
            chrom_list = list(chrom)
            chrom_list[mut_index] = bit
            chrom = ''.join(chrom_list)

            # assign mutation
            self.chrom_a = chrom
            self.x = self.decode( chrom )

        # generate random number [0-1]
        numb = random.uniform(0, 1)

        # check if we should mutate chromosome b
        mutate = (numb <= threshold)

        # mutate if necessary
        if mutate:
            # get chromosome
            chrom = self.chrom_b
            
            # invert a random bit of the chromosome
            mut_index = random.randint(0, MAX_STRING - 1)
            bit = chrom[mut_index]
            if bit == '1':
                bit = '0'
            else:
                bit = '1'
            chrom_list = list(chrom)
            chrom_list[mut_index] = bit
            chrom = ''.join(chrom_list)

            # assign mutation
            self.chrom_b = chrom
            self.y = self.decode( chrom )

        # do nothing

    def fitness(self, render):
        # start game
        fitness = 0
        env = gym.make('Breakout-ram-v0')
        observation = env.reset()
        
        # game loop
        t = 0
        while 1:
            # increment time
            t += 1
            # render
            if render:
                env.render()            
            # get actions
            action = self.make_action(observation)
            # take action
            observ, reward, done, info = env.step(action)
            observation = observ
            # update fitness
            fitness += reward
            # check done
            lives = observ[57]
            if done or lives < 4 or fitness > 100:
                #print("Episode finished after {} timesteps".format(t))
                break
            
        return fitness

    def make_action(self, ram):

        ball_x = int(ram[self.bx])
        paddle_x = int(ram[self.px])
        
        # Check if we should fire new ball
        if ram[103] == 0:
            return 1

        # Otherwise, check what move (L/R) should be made
        diff = ball_x - paddle_x
        if diff > 0: # move right
            return 2
        elif diff < 0: # move left
            return 3

        # Otherwise, do nothing
        return 0

    def print(self):
        print("Individual : chrom_a = {}, chrom_b = {}".format(self.chrom_a, self.chrom_b))
        print("           : ball pos = [{}], paddle pos = [{}]".format(self.bx, self.px))
        print("           : fitness = {}".format(self.fitness))
        
            
def make_rand_individual(): 
    chromosome_a = ""
    while len(chromosome_a) < MAX_STRING:
        rand_bit = str( random.randint(0,1) )
        chromosome_a += rand_bit
        
    chromosome_b = ""
    while len(chromosome_b) < MAX_STRING:
        rand_bit = str( random.randint(0,1) )
        chromosome_b += rand_bit

    individual = Individual(chromosome_a, chromosome_b)
    
    return individual
            
        
        
