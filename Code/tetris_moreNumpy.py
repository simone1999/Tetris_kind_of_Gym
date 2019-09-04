import numpy as np
import random


class Tetris:

    def __init__(self, game_height, game_width, games):
        self.game_height = game_height
        self.game_width = game_width
        self.games = games
        self.locked_blocks = np.zeros((games, game_height, game_width), dtype=bool)
        self.moving_blocks = np.zeros((games, game_height, game_width), dtype=bool)
        '''
        x und y geben die koordinaten des bewegenden Blockes an, relativ zu der Mitte des Spielfeldes (auch halbe)
        die Koordinaten sind hierbei diejenigen der Mitte von blocks, also blocks[1.5, 1.5]
        '''
        self.moving_blocks_informations = np.zeros((games, 2), dtype=float)
        self.moving_blocks_informations[:, 1] = game_height/2-2

        self.blocks = np.array(
            [
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [1, 0, 0, 0],
                    [0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0],
                ],
                [
                    [0, 0, 1, 0],
                    [0, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0],
                ],
                [
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0],
                ]
            ], dtype=bool)

    def step(self, actions):
        score = np.zeros(self.games)
        done = np.zeros(self.games, dtype=bool)

        old_moving_blocks = self.moving_blocks.copy()
        old_moving_blocks_informations = self.moving_blocks_informations.copy()

        '''
        0: do nothing
        1: to the left
        2: to the right
        3: turn left
        4: turn right
        '''

        mask = actions == 1
        changing_moving_blocks_informations = self.moving_blocks_informations[mask]
        changing_moving_blocks = self.moving_blocks[mask]
        changing_moving_blocks[:, :-2] = changing_moving_blocks[:, 1:]
        changing_moving_blocks[:, -1] = 0
        changing_moving_blocks_informations[0] = changing_moving_blocks_informations[0] - 1

        mask = actions == 2
        changing_moving_blocks_informations = self.moving_blocks_informations[mask]
        changing_moving_blocks = self.moving_blocks[mask]
        changing_moving_blocks[:, 1:] = changing_moving_blocks[:, :-2]
        changing_moving_blocks[:, 0] = 0
        changing_moving_blocks_informations[0] = changing_moving_blocks_informations[0] + 1

        mask = actions == 3
        changing_moving_blocks_informations = self.moving_blocks_informations[mask]
        changing_moving_blocks = self.moving_blocks[mask]
        self.moving_blocks[mask] = self.rotate_block(changing_moving_blocks, changing_moving_blocks_informations, 3)

        mask = actions == 4
        changing_moving_blocks_informations = self.moving_blocks_informations[mask]
        changing_moving_blocks = self.moving_blocks[mask]
        self.moving_blocks[mask] = self.rotate_block(changing_moving_blocks, changing_moving_blocks_informations, 1)


        #return game_field, score, done, None



    def rotate_block(self, blocks, blocks_informations, times):
        failed = np.zeros(self.games, dtype=bool)
        blocks = np.rot90(blocks, times, axes=(-2, -1))
        x = blocks_informations[:, 0].copy()
        y = blocks_informations[:, 1].copy()
        for _ in range(times):
            x_tmp = x.copy()
            y_tmp = y.copy()
            x = -y_tmp
            y = x_tmp
        x_offset = x - blocks_informations[:, 0]
        y_offset = y - blocks_informations[:, 1]

        '''
        we know that a moving block always have 4 pieces, so we can just move the Block without anny cheching and simply test afterwards, if there are still 4 pieces!!!
        '''




        return (blocks, failed)
