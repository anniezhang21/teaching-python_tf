# BEST TIME: 2:46



#Import statements
import gym
import universe
import random

# Loading the game (Neon Race) you want to play using AI:
env = gym.make("flashgames.NeonRace-v0")

# Loading a list of observations of the environment's initial state into observation_n
observation_n = env.reset()
reward_n = 0

goleft = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True),
        ('KeyEvent', 'ArrowRight', False)]
goright = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False),
         ('KeyEvent', 'ArrowRight', True)]
gostraight = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False),
        ('KeyEvent', 'ArrowRight', False)]

time = 0
length = 100
avg_reward = 0
fast = False
action = gostraight
lastrewards = []

#Starting the Game Loop
while True:
    #If the car has been going straight a long time, it probably needs to turn.
    if avg_reward > 6:
        fast = True
    else:
        fast = False

    if fast:
        print("fast!")
        probstraight = 99
        probleft = 0.5
    else:
        probstraight = 0.8
        probleft = 0.1

    action_n = [action for observation in observation_n]

    if observation_n != [None]:
        if time % length == 0 and time > 700:
            rand_num = random.random()
            if rand_num > probstraight:
                action = gostraight
                length = 100
            elif rand_num > probleft:
                action = goleft
                length = 30
            else:
                action = goright
                length = 30
        time += 1

    # Do the action
    observation_n, reward_n, done_n, info = env.step(action_n)

    # Resetting average rewards and printing important information
    if time % 10 == 0:
        lastrewards.append(reward_n[0])

        if time % 500 == 0:
            avg_reward = sum(lastrewards) / len(lastrewards)
            lastrewards = []
        # print("time: ", time)
        # print("reward: ", reward_n)
        print("avg_reward: ", avg_reward)



    # Render the environment
    env.render()
