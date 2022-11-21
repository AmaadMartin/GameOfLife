# GameOfLife
INSTRUCTIONS TO INSTALL:

-If you dont have pip:\
-Download get-pip.py from https://bootstrap.pypa.io/get-pip.py, enter into command line: python get-pip.py

-Enter into command line:\
python -m pip install numpy\
python -m pip install -U matplotlib\
python -m pip install opencv-python

-Download GameOfLife.py for complete code\
-Download GameOfLife_Template.py for code without rules function

INSTRUCTIONS TO RUN:\
-Go to directory where you installed GameOfLife.py and GameOfLife_Template.py\
-Enter into command Line: python FILE_NAME

RULES:\
0 corresponds to a Dead Cell\
1 corresponds to an Alive cell\
If Cell is Alive and has 2 or 3 neighbors: Cell remains Alive\
If Cell is Dead and has 3 neighbors: Cell becomes Alive\
Otherwise: Cell becomes Dead


