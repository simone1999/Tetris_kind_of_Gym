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
        x und y geben die koordinaten des bewegenden Blockes an, die Koorinaten sind hierbei die Position des linken obenen Blockes
        Koordinaten fangen bei (0, 0) an
        der 3. Wert gibt die Rotation des Blockes an
        und der 4. Wert die Block ID
        '''
        self.moving_blocks_informations = np.zeros((games, 4), dtype=int)

        self.blocks = np.array(
            [
                [
                    [
                        [0, 0, 0, 0],
                        [1, 1, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                    ],
                    [
                        [0, 0, 0, 0],
                        [1, 1, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                    ],
                ],
                
                [
                    [
                        [0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 1, 0],
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
                        [0, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                    ],
                ],
                
                [
                    [
                        [0, 0, 0, 0],
                        [0, 1, 1, 1],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 1, 0],
                    ],
                    [
                        [0, 0, 0, 0],
                        [0, 0, 1, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                    ],
                ],
                
                [
                    [
                        [0, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                    ],
                ],
                
                [
                    [
                        [0, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 0, 1, 0],
                        [0, 0, 1, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                    ],
                ],
                
                [
                    [
                        [0, 0, 1, 0],
                        [0, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 1, 0],
                        [0, 0, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 0, 1, 0],
                        [0, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 1, 0],
                        [0, 0, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                ],
                
                [
                    [
                        [0, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 0, 1, 1],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 0, 1, 1],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
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
        
        #first test if there is a moving Block at all, otherwise create one
        no_moving_blocks = np.invert(np.anny(self.moving_blocks, axis=(-1, -2)))
        num_missing_blocks = np.sum(no_moving_blocks)
        x_s = np.random.randint(low=0, high=self.game_width-4, size=num_missing_blocks)
        y_s = 0
        block_ids = np.random.randint(low=0, high=7, size=num_missing_blocks)
        block_rotations = np.random.randint(low=0, high=4, size=num_missing_blocks)
        self.moving_blocks_informations[no_moving_blocks, 0] = x_s
        self.moving_blocks_informations[no_moving_blocks, 1] = y_s
        self.moving_blocks_informations[no_moving_blocks, 2] = block_rotations
        self.moving_blocks_informations[no_moving_blocks, 2] = block_ids
        self.place_block(self.moving_blocks[no_moving_blocks], self.moving_blocks_informations[no_moving_blocks])
        
        game_overs = test_validity(self, self.moving_blocks, self.fixed_blocks)
        done[game_overs] = True
        reset_games(self.moving_blocks[done], self.moving_blocks_informations[done], self.fixed_blocks[done])
        score[game_overs] = -100
        
        mask = actions == 1
        changing_moving_blocks_informations = self.moving_blocks_informations[mask]
        changing_moving_blocks = self.moving_blocks[mask]
        changing_moving_blocks[:, :, :-2] = changing_moving_blocks[:, :, 1:]
        changing_moving_blocks[:, :, -1] = 0
        changing_moving_blocks_informations[0] = changing_moving_blocks_informations[0] - 1

        mask = actions == 2
        changing_moving_blocks_informations = self.moving_blocks_informations[mask]
        changing_moving_blocks = self.moving_blocks[mask]
        changing_moving_blocks[:, :, 1:] = changing_moving_blocks[:, :, :-2]
        changing_moving_blocks[:, :, 0] = 0
        changing_moving_blocks_informations[0] = changing_moving_blocks_informations[0] + 1

        mask = actions == 3
        changing_moving_blocks_informations = self.moving_blocks_informations[mask]
        changing_moving_blocks = self.moving_blocks[mask]
        self.moving_blocks[mask] = self.rotate_block(changing_moving_blocks, changing_moving_blocks_informations, -1)

        mask = actions == 4
        changing_moving_blocks_informations = self.moving_blocks_informations[mask]
        changing_moving_blocks = self.moving_blocks[mask]
        self.moving_blocks[mask] = self.rotate_block(changing_moving_blocks, changing_moving_blocks_informations, 1)
        
        invalid = np.invert(self.test_validity(self.moving_blocks, self.locked_blocks))
        self.moving_blocks[invalid] = old_moving_blocks[invalid]
        self.moving_blocks_informations[invalid] = old_moving_blocks_informations[invalid]
                
        #move one down every step
        self.moving_blocks[:, 1:] = self.moving_blocks[:, :-2]
        self.moving_blocks[:, 0] = 0
        self.moving_blocks_informations[1] = self.moving_blocks_informations[1] + 1
        now_fixed = np.invert(self.test_validity(self.moving_blocks, self.locked_blocks))
        self.moving_blocks[now_fixed] = old_moving_blocks[now_fixed]
        self.moving_blocks_informations[now_fixed] = old_moving_blocks_informations[now_fixed]
        self.locked_blocks[now_fixed] = np.logical_or(self.locked_blocks[now_fixed], self.moving_blocks[now_fixed])
        self.moving_blocks_informations[now_fixed] = 0
        self.moving_blocks[now_fixed] = 0
        #test for full Rows
        score[now_fixed] += test_full_rows(self.locked_blocks[now_fixed])
        
        game_field = np.logical_or(self.locked_blocks, self.moving_blocks)
        
        return game_field, score, done, None


    def test_validity(self, moving_blocks, fixed_blocks):
        # just test if there are still 4 Blocks
        right_ammount_of_blocks = np.sum(moving_blocks, axis=(-1, -2)) == 4
        dont_overlap = np.anny(np.logical_and(moving_blocks, fixed_blocks), axis=(-1, -2))
        return np.and(right_ammount_of_blocks, dont_overlap)
    
    def rotate_block(self, moving_blocks, blocks_informations, times):
        moving_blocks = False
        blocks_informations[2] += times
        blocks_informations[2] %= 4
        self.place_block(moving_blocks, blocks_informations)


    def place_block(self, moving_blocks, blocks_informations):
        moving_blocks = False
        tetrises = self.blocks[blocks_informations[3], blocks_informations[2]]
        moving_blocks[:4, :4] = tetrises
        for i in range(self.game_width):
            movement_mask = blocks_informations[0] < i
            moving_blocks[movement_mask, :, 1:] = moving_blocks[movement_mask, :, :-2]
            moving_blocks[movement_mask, :, 0] = False
            
        for i in range(self.game_height):
            movement_mask = blocks_informations[1] < i
            moving_blocks[movement_mask, 1:] = moving_blocks[movement_mask, :-2]
            moving_blocks[movement_mask, 0] = False
    
    def reset_games(self, moving_blocks, blocks_informations, locked_blocks):
        moving_blocks = False
        locked_blocks = False
        blocks_informations = 0
        
    def test_full_rows(self, locked_blocks):
        reward = np.zeros(len(locked_blocks))
        broken_rows = np.zeros(len(locked_blocks))
        for i in range(self.game_height):
            brokens = np.all(locked_blocks[:, i, :], axis=(-1))
            broken_rows[brokens] += 1
            locked_blocks[brokens, 1:i] = locked_blocks[brokens, 0:i-1]
            locked_blocks[brokens, 0] = 0
        reward[broken_rows==1] = 1
        reward[broken_rows==2] = 3
        reward[broken_rows==3] = 5
        reward[broken_rows==4] = 10
        return reward
        
        
        
        
        
    
    
    
    
    
