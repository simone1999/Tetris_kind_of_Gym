# Tetris_kind_of_Gym

# Introduction
a super Fast Tetris implementation for Reinforcement Learning

this Projects only goal is execution Speed.
It is intendet for quickly testing and playing around with reinforcement Learning Algorythmns.
on a standard Computer approximately 250.000 Game Steps can be executed in a single Second.
The huge speed gain is because the Game is completely calculatet with Numpy, so nearly no if's, while's and fore's had been used in this Code.
Also the games are hugely parralized, so it is recomendet to run at least 1.000 Games simultanously (can be choosen by an Parameter for the init Function)

# Syntax
if you import this libary as "tetris"

you can simply initialize the Games by

games = tetris.Tetris(field_height, field_width, num_paralel_Games)

and then simply in your loop run

state, reward, done, info = games.step(actions)

you don't have to reset the Enviroment, it does it for every Game, if it is finished by it's own.
remember, that this enviroment is made for multiple paralel games, so all parameters and return Values have an additional
Dimmension (the first), which is the Indexing for every Game.
