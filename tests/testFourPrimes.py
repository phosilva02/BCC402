import sys
from src.FourPrimes import FourPrimes
from io import StringIO

input_source = '''24
36
46
10000000
'''

sys.stdin = StringIO(input_source)
sum = FourPrimes()
sys.stdin = sys.__stdin__