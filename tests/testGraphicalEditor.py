import sys
from src.GraphicalEditor import GraphicalEditor
from io import StringIO

input_source = '''I 5 6
L 2 3 A
S one.bmp
G 2 3 J
F 3 3 J
V 2 3 4 W
H 3 4 2 Z
S two.bmp
X
'''

sys.stdin = StringIO(input_source)
GE = GraphicalEditor()
sys.stdin = sys.__stdin__