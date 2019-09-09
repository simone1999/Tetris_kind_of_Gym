#import Code.tetris as tetris
import Code.tetris_moreNumpy as tetris
import numpy as np
from tqdm import tqdm
from time import sleep
from matplotlib import pyplot as plt

num_games = 250_000
game = tetris.Tetris(20, 10, num_games)
prev_states = np.zeros((6, num_games, 20, 10))
prev_rewards = np.zeros((6, num_games))


for i in tqdm(range(100_000_000)):
    actions = np.random.randint(0, 5, num_games)
    state, reward, done, info = game.step(actions)

    '''
    #plt.imshow(state[0], interpolation='nearest')
    #plt.show()
    '''

    '''
    lineBreakers = prev_rewards[2] >= 1
    if np.any(lineBreakers):
        print(f"Line was broken and we scored!!!!")
        for old_state in prev_states[:, lineBreakers][:, 0]:
            plt.imshow(old_state, interpolation='nearest')
            plt.show()
        sleep(5)

    prev_states[1:] = prev_states[:-1]
    prev_states[0] = state
    prev_rewards[1:] = prev_rewards[:-1]
    prev_rewards[0] = reward
    '''
