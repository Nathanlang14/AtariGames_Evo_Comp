import gym
import random

def main():

    delta_ram_count = [0] * 128
    delta_ram_values = [0] * 128

    env = gym.make('Breakout-ram-v0')
        
    last_observation = env.reset()
    t = 0
    while True:
        env.render()
        action = make_action(last_observation) #env.action_space.sample()
        
        observation, reward, done, info = env.step(action)

        for i in range(128):
            diff = last_observation[i] - observation[i]
            if diff > 0:
                delta_ram_count[i] += 1
                delta_ram_values[i] += diff
        last_observation = observation
        
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
        t+=1
        env.close()


    print("Delta Ram")
    for i in range(128):
        if delta_ram_count[i] > 0:
            print("RAM[{}] : Changed {} time(s) summing to {}.".format(i, delta_ram_count[i], delta_ram_values[i]))


def make_action(ram):
    paddle_x = ram[70]
    ball_x = ram[99]
    ball_y = ram[101]
    ball_in_play = ram[103]
    # lives =

    print(paddle_x)
    print(ball_x)
    print()

    if not ball_in_play:
        return 1

    diff = ball_x - paddle_x
    if diff > 0: # Ball is to the right, move right
        return 3
    elif diff < 0: # Ball is to the left, move left
        return 2

    return 0

    
main()
