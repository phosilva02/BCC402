import sys
from src.War import War
from io import StringIO

input_source = '''10
1 0 1
1 1 2
2 0 5
3 0 2
3 8 9
4 1 5
4 1 2
4 8 9
1 8 9
1 5 2
3 5 2
0 0 0
'''

sys.stdin = StringIO(input_source)
Guerra = War()
sys.stdin = sys.__stdin__