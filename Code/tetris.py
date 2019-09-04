import numpy as np
import random


class Tetris:

    def __init__(self, game_height, game_width, games):
        self.game_height = game_height
        self.game_width = game_width
        self.games = games
        self.locked_blocks = np.zeros((games, game_height, game_width), dtype=bool)
        '''
        x und y geben die koordinaten des bewegenden Blockes an
        die koordinate ist hier der Block ganz links oben, also [0, 0] und dieser rotiert auch nicht mit!
        block_ID ist der Index in blocks
        '''
        self.moving_blocks_informations = [{
            "block_ID" : random.choice(range(7)),
            "rotation" : random.choice(range(4)),
            "x" : random.choice(range(self.game_width-4)),
            "y" : 0
        } for _ in range(games)]

    def step(self, actions):
        def reset_block(block_info, old_x, old_y, old_rotation):
            block_info["x"] = old_x
            block_info["y"] = old_y
            block_info["rotation"] = old_rotation

        score = np.zeros(self.games)
        done = np.zeros(self.games, dtype=bool)

        for id, (action, block_info, locked_blocks_this_game) in enumerate(zip(actions, self.moving_blocks_informations, self.locked_blocks)):
            '''
            0: do nothing
            1: to the left
            2: to the right
            3: turn left
            4: turn right
            '''
            old_x = block_info["x"]
            old_y = block_info["y"]
            old_rotation = block_info["rotation"]

            if action == 0:
                pass

            elif action == 1:
                block_info["x"] -= 1
                if self.would_overlap(block_info, locked_blocks_this_game):
                    reset_block(block_info, old_x, old_y, old_rotation)

            elif action == 2:
                block_info["x"] += 1
                if self.would_overlap(block_info, locked_blocks_this_game):
                    reset_block(block_info, old_x, old_y, old_rotation)

            elif action == 3:
                block_info["rotation"] -= 1
                if self.would_overlap(block_info, locked_blocks_this_game):
                    reset_block(block_info, old_x, old_y, old_rotation)

            elif action == 4:
                block_info["rotation"] += 1
                if self.would_overlap(block_info, locked_blocks_this_game):
                    reset_block(block_info, old_x, old_y, old_rotation)

            block_info["y"] += 1
            if self.would_overlap(block_info, locked_blocks_this_game):
                reset_block(block_info, old_x, old_y, old_rotation)
                score[id] += self.fix_block(block_info, self.locked_blocks[id])
                block_info["rotation"] = random.choice(range(4))
                block_info["y"] = 0
                block_info["x"] = random.choice(range(self.game_width-4))
                block_info["block_ID"] = random.choice(range(7))
                if self.would_overlap(block_info, locked_blocks_this_game):
                    done[id] = True
                    score[id] -= 20
                    self.locked_blocks[id] = 0


        game_field = self.locked_blocks.copy()

        Xes = np.array([x["x"] for x in self.moving_blocks_informations])
        Yes = np.array([x["y"] for x in self.moving_blocks_informations])
        block_IDs = np.array([x["block_ID"] for x in self.moving_blocks_informations])
        rotations = np.array([x["rotation"] for x in self.moving_blocks_informations])

        blocks = self.blocks[block_IDs]
        for i in range(len(blocks)):
            blocks[i] = self.rotate_block(blocks[i], rotations[i])

        Xes_start = 0 - Xes
        Xes_end = (self.game_width - 1) - Xes
        Yes_start = 0 - Yes
        Yes_end = (self.game_height - 1) - Yes

        Xes_start[Xes >= 0] = 0
        Xes_end[Xes + 3 <= self.game_width - 1] = 3
        Yes_start[Yes >= 0] = 0
        Yes_end[Yes + 3 <= self.game_height - 1] = 3

        for i in range(self.games):
            original = game_field[i, Yes[i]+Yes_start[i]:Yes[i]+Yes_end[i]+1, Xes[i]+Xes_start[i]:Xes[i]+Xes_end[i]+1]
            modifier = blocks[i, Yes_start[i]:Yes_end[i]+1, Xes_start[i]:Xes_end[i]+1]
            modified = np.bitwise_or(original, modifier)
            game_field[i, Yes[i] + Yes_start[i]:Yes[i] + Yes_end[i] + 1, Xes[i] + Xes_start[i]:Xes[i] + Xes_end[i] + 1] = modified
            pass

        #return observation/state, reward, done, info
        return game_field, score, done, None


    def fix_block(self, block_info, locked_blocks_this_game):
        score = 0
        block = self.blocks[block_info["block_ID"]]
        block = self.rotate_block(block, block_info["rotation"])

        x_start = 0 if block_info["x"] >= 0 else 0 - block_info["x"]
        x_end = 3 if block_info["x"] + 3 <= self.game_width - 1 else (self.game_width - 1) - block_info["x"]
        y_start = 0 if block_info["y"] >= 0 else 0 - block_info["y"]
        y_end = 3 if block_info["y"] + 3 <= self.game_height - 1 else (self.game_height - 1) - block_info["y"]

        critical_locked_blocks = locked_blocks_this_game[block_info["y"] + y_start:block_info["y"] + y_end + 1, block_info["x"] + x_start:block_info["x"] + x_end + 1]
        critical_moving_blocks = block[y_start:y_end + 1, x_start:x_end + 1]
        combined_block = np.bitwise_or(critical_locked_blocks, critical_moving_blocks)
        locked_blocks_this_game[block_info["y"] + y_start:block_info["y"] + y_end + 1, block_info["x"] + x_start:block_info["x"] + x_end + 1] = combined_block

        blocks_in_rows = np.sum(locked_blocks_this_game, axis=-1)
        max_in_one_row = np.max(blocks_in_rows)
        if max_in_one_row == self.game_width:
            fullRows = []
            for id, row_blocks in enumerate(blocks_in_rows):
                if row_blocks == self.game_width:
                    fullRows.append(id)
            for row_id in fullRows:
                for i in range(row_id, 0, -1):#0 wird nicht durchloopt
                    locked_blocks_this_game[i] = locked_blocks_this_game[i - 1]
                locked_blocks_this_game[0] = 0
            num_full_rows = len(fullRows)
            if num_full_rows == 1:
                score = 1
            if num_full_rows == 2:
                score = 3
            if num_full_rows == 3:
                score = 5
            if num_full_rows == 4:
                score = 10
        return score


    def would_overlap(self, block_info, locked_blocks_this_game):
        block = self.blocks[block_info["block_ID"]]
        block = self.rotate_block(block, block_info["rotation"])
        x = block_info["x"]
        y = block_info["y"]
        space_till_bottom = self.game_height - 1 - y
        if x <= -1:
            if x == -1:
                if np.any(block[:, 0]):
                    return True
            elif x == -2:
                if np.any(block[:, 0:2]):
                    return True
            else:
                return True
        if x >= self.game_width-3:
            if x == self.game_width-3:
                if np.any(block[:, 3]):
                    return True
            elif x == self.game_width-2:
                if np.any(block[:, 2:4]):
                    return True
            else:
                return True

        if space_till_bottom <= 2:
            if space_till_bottom == 2:
                if np.any(block[3, :]):
                    return True
            elif space_till_bottom == 1:
                if np.any(block[2:4, :]):
                    return True
            else:
                return True


        x_start = 0 if x >= 0 else 0 - x
        x_end = 3 if x + 3 <= self.game_width - 1 else (self.game_width - 1) - x
        y_start = 0 if y >= 0 else 0 - y
        y_end = 3 if y + 3 <= self.game_height - 1 else (self.game_height - 1) - y

        critical_locked_blocks = locked_blocks_this_game[y + y_start:y + y_end + 1, x + x_start:x + x_end + 1]
        critical_moving_blocks = block[y_start:y_end + 1, x_start:x_end + 1]

        if np.any(np.bitwise_and(critical_moving_blocks, critical_locked_blocks)):
            return True

        return False

    def rotate_block(self, block, times):
        return np.rot90(block, times, axes=(-2, -1))








    blocks = np.array(
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
                [0, 1, 1, 1],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0],
                [0, 1, 1, 1],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ],
            [
                [1, 1, 1, 0],
                [0, 0, 1, 0],
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
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ]
        ], dtype=bool)

