import sys
from src.StepLadders import StepLadders
from io import StringIO

input_source = '''cat
dig
dog
fig
fin
fine
fog
log
wine
'''

sys.stdin = StringIO(input_source)
a = StepLadders()
sys.stdin = sys.__stdin__