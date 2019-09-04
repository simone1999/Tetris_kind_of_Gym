#import Code.tetris as tetris
import Code.tetris_moreNumpy as tetris
import numpy as np
from tqdm import tqdm
from time import sleep
from matplotlib import pyplot as plt

num_games = 80_000
game = tetris.Tetris(20, 10, num_games)
prev_state = None

for i in tqdm(range(100_000_000)):
    actions = np.full(num_games, 0)
    state, reward, done, info = game.step(actions)

    #plt.imshow(state[0], interpolation='nearest')
    #plt.show()
    #sleep(0.25)

    prev_state = state
