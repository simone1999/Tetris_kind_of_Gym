import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='gymTetrisFast',

     version='0.2',

     #scripts=['Code/tetris', 'Code/tetris_moreNumpy'] ,
     #scripts=['Code/tetris_moreNumpy'] ,

    
     author="Klein Simon",

     author_email="simon@klein-homepage.de",

     description="fast paralell Tetris implementation for Reinforcement learning",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/simone1999/Tetris_kind_of_Gym",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
