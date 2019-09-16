import numpy as np
import pygame

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

        self.window_size = (self.game_width * 26 + 10, self.game_height * 26 + 10)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Tetris")

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
        no_moving_blocks = np.invert(np.any(self.moving_blocks, axis=(-1, -2)))
        num_missing_blocks = np.sum(no_moving_blocks)
        x_s = np.random.randint(low=0, high=self.game_width-4, size=num_missing_blocks)
        y_s = 0
        block_ids = np.random.randint(low=0, high=7, size=num_missing_blocks)
        block_rotations = np.random.randint(low=0, high=4, size=num_missing_blocks)
        self.moving_blocks_informations[no_moving_blocks, 0] = x_s
        self.moving_blocks_informations[no_moving_blocks, 1] = y_s
        self.moving_blocks_informations[no_moving_blocks, 2] = block_rotations
        self.moving_blocks_informations[no_moving_blocks, 3] = block_ids
        self.place_block(no_moving_blocks)
        
        game_overs = np.invert(self.test_validity(self.moving_blocks, self.locked_blocks))
        done[game_overs] = True
        self.reset_games(done)
        score[game_overs] = -100

        #test for full Rows
        score += self.test_full_rows() #tests the whole game because stupid Numpy byValue copyying
        
        mask = actions == 1
        self.moving_blocks[mask, :, :-1] = self.moving_blocks[mask, :, 1:]
        self.moving_blocks[mask, :, -1] = 0
        self.moving_blocks_informations[mask, 0] = self.moving_blocks_informations[mask, 0] - 1

        mask = actions == 2
        self.moving_blocks[mask, :, 1:] = self.moving_blocks[mask, :, :-1]
        self.moving_blocks[mask, :, 0] = 0
        self.moving_blocks_informations[mask, 0] = self.moving_blocks_informations[mask, 0] + 1

        mask = actions == 3
        if np.any(mask):
            self.rotate_block(mask, -1)

        mask = actions == 4
        if np.any(mask):
            self.rotate_block(mask, 1)
        
        invalid = np.invert(self.test_validity(self.moving_blocks, self.locked_blocks))
        self.moving_blocks[invalid] = old_moving_blocks[invalid]
        self.moving_blocks_informations[invalid] = old_moving_blocks_informations[invalid]

        #manual movement was sucessfull, so the reset state is now after this movement
        old_moving_blocks = self.moving_blocks.copy()
        old_moving_blocks_informations = self.moving_blocks_informations.copy()
                
        #move one down every step
        self.moving_blocks[:, 1:] = self.moving_blocks[:, :-1]
        self.moving_blocks[:, 0] = 0
        self.moving_blocks_informations[:, 1] = self.moving_blocks_informations[:, 1] + 1
        now_fixed = np.invert(self.test_validity(self.moving_blocks, self.locked_blocks))
        self.moving_blocks[now_fixed] = old_moving_blocks[now_fixed]
        self.moving_blocks_informations[now_fixed] = old_moving_blocks_informations[now_fixed]
        self.locked_blocks[now_fixed] = np.logical_or(self.locked_blocks[now_fixed], self.moving_blocks[now_fixed])
        self.moving_blocks_informations[now_fixed] = 0
        self.moving_blocks[now_fixed] = 0
        game_field = np.logical_or(self.locked_blocks, self.moving_blocks)
        return game_field, score, done, {
                                         "fixedBlocks":self.locked_blocks,
                                         "movingBlocks":self.moving_blocks}

    def test_validity(self, moving_blocks, fixed_blocks):
        # just test if there are still 4 Blocks
        right_ammount_of_blocks = np.sum(moving_blocks, axis=(-1, -2)) == 4
        dont_overlap = np.invert(np.any(np.logical_and(moving_blocks, fixed_blocks), axis=(-1, -2)))
        return np.logical_and(right_ammount_of_blocks, dont_overlap)

    def rotate_block(self, mask, times):
        self.moving_blocks[mask, :, :] = False
        self.moving_blocks_informations[mask, 2] += times
        self.moving_blocks_informations[mask, 2] %= 4
        self.place_block(mask)

    def place_block(self, mask):
        tetrises = self.blocks[self.moving_blocks_informations[mask, 3], self.moving_blocks_informations[mask, 2]]
        self.moving_blocks[mask] = False
        self.moving_blocks[mask, :4, :4] = tetrises
        for i in range(self.game_width):
            movement_mask = self.moving_blocks_informations[:, 0] > i
            movement_mask = np.logical_and(movement_mask, mask)
            self.moving_blocks[movement_mask, :, 1:] = self.moving_blocks[movement_mask, :, :-1]
            self.moving_blocks[movement_mask, :, 0] = False
            
        for i in range(self.game_height):
            movement_mask = self.moving_blocks_informations[:, 1] > i
            movement_mask = np.logical_and(movement_mask, mask)
            self.moving_blocks[movement_mask, 1:] = self.moving_blocks[movement_mask, :-1]
            self.moving_blocks[movement_mask, 0] = False

    def reset_games(self, mask):
        self.moving_blocks[mask] = False
        self.moving_blocks_informations[mask] = False
        self.locked_blocks[mask] = 0

    def test_full_rows(self):
        reward = np.zeros(len(self.locked_blocks))
        broken_rows = np.zeros(len(self.locked_blocks))
        for i in range(self.game_height):
            brokens = np.all(self.locked_blocks[:, i, :], axis=(-1))
            broken_rows[brokens] += 1
            if i > 0:
                self.locked_blocks[brokens, 1:i+1] = self.locked_blocks[brokens, 0:i]
            self.locked_blocks[brokens, 0] = 0
        reward[broken_rows == 1] = 1
        reward[broken_rows == 2] = 3
        reward[broken_rows == 3] = 5
        reward[broken_rows == 4] = 10
        return reward

    def render(self, id):
        moving_blocks = self.moving_blocks[id]
        fixed_blocks = self.locked_blocks[id]

        surface = pygame.image.load(r'sprites/tetris_head.jpg')
        pygame.display.set_icon(surface)

        self.screen.fill((150, 150, 150))

        yellow = pygame.image.load(r'sprites/yellow_block.jpg')
        green =  pygame.image.load(r'sprites/green_block.jpg')

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:
                exit(88)

        for y in range(self.game_height):
            for x in range(self.game_width):
                x_cord = x * 26 + 5
                y_cord = y * 26 + 5
                if fixed_blocks[y, x]:
                    self.screen.blit(yellow, (x_cord, y_cord))
                elif moving_blocks[y, x]:
                    self.screen.blit(green, (x_cord, y_cord))
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), [x_cord, y_cord, 25, 25], 0)

        pygame.display.flip()





