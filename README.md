# GameOfLife
INSTRUCTIONS TO INSTALL:

-If you dont have pip:\
-Download get-pip.py from https://bootstrap.pypa.io/get-pip.py, enter into command line: python get-pip.py

-Enter into command line:\
python -m pip install numpy\
python -m pip install opencv-python

-Download GameOfLife.py for complete code\
-Download GameOfLife_Template.py for code without rules function

INSTRUCTIONS TO RUN:\
-Go to directory where you installed GameOfLife.py and GameOfLife_Template.py\
-Enter into command Line: python FILE_NAME

RULES:\
-0 corresponds to a Dead Cell\
-1 corresponds to an Alive cell

-If Cell is Alive and has 2 or 3 neighbors: Cell remains Alive\
-If Cell is Dead and has 3 neighbors: Cell becomes Alive\
-Otherwise: Cell becomes Dead

RULES FUNCTION:\
-The rules function takes as input:\
grid - 2d array of size 40 rows and 40 columns that represents the current grid\
y - the row of the cell to be updated\
x - the column of the cell to be updated

-It is suppose to output:\
1 if the cell becomes or stays alive\
0 if the cell becomes or stays dead
