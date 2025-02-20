import sys
from src.TugOfWar import TugOfWar
from io import StringIO

input_source = '''1

3
100
90
200
'''

sys.stdin = StringIO(input_source)
caboDeGuerra = TugOfWar()
sys.stdin = sys.__stdin__