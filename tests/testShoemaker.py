import sys
from src.Shoemaker import Shoemaker
from io import StringIO

input_source = '''1

4
3 4
1 1000
2 2
5 5
'''

sys.stdin = StringIO(input_source)
judge = Shoemaker()
sys.stdin = sys.__stdin__