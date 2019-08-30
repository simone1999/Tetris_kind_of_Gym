import Code.tetris as tetris
from tqdm import tqdm
from time import sleep
from matplotlib import pyplot as plt

game = tetris.Tetris(20, 10, 1)
prev_state = None

for i in tqdm(range(100_000_000)):
    state, reward, done, info = game.step([0,0])

    if reward[0] > 0:
        plt.imshow(state[0], interpolation='nearest')
        plt.show()
        plt.imshow(prev_state[0], interpolation='nearest')
        plt.show()

    prev_state = state
