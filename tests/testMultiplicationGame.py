import sys
from src.MultiplicationGame import MultiplicationGame
from io import StringIO

input_source = '''162
17
34012226
'''

sys.stdin = StringIO(input_source)
game = MultiplicationGame()
sys.stdin = sys.__stdin__