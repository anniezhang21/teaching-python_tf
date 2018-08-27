# Fun examples of games played using AI
# https://blog.openai.com/universe/
# https://www.youtube.com/watch?v=qv6UVOQ0F44
import universe
import gym
import random

# Loading the game (Neon Race) you want to play using AI:
# To play a different game, replace the string 'flashgames.NeonRace-v0' with your desired game
env = gym.make("flashgames.NeonRace-v0")

# Loading a list of observations of the environment's initial state into observation_n
observation_n = env.reset()

go_left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True),
        ('KeyEvent', 'ArrowRight', False)]
go_right = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False),
         ('KeyEvent', 'ArrowRight', True)]
go_straight = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False),
        ('KeyEvent', 'ArrowRight', False)]

action = go_straight
time = 0
delay = 200
# Starts the game loop
while True:
    if time % delay == 0:
        rand_num = random.randint(1, 100)
        if rand_num < 50:
            action = go_straight
            delay = 200
        elif rand_num < 75:
            action = go_left
            delay = 50
        else:
            action = go_right
            delay = 50
    # Setting our agent: Pressing the up arrow
    # More keys: "ArrowLeft" and "ArrowRight" to turn
    action_n = [action for observation in observation_n]

    # Do the action
    observation_n, reward_n, done_n, info = env.step(action_n)

    if observation_n != [None]:
        time += 1
        if time % 10 == 0:
            print(time)

    # Render the environment
    env.render()
