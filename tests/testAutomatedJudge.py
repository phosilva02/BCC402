import sys
from src.AutomatedJudge import AutomatedJudge
from io import StringIO

input_source = '''2
The answer is: 10
The answer is: 5
2
The answer is: 10
The answer is: 5
2
The answer is: 10
The answer is: 5
2
The answer is: 10
The answer is: 15
2
The answer is: 10
The answer is: 5
2
The answer is: 10
The answer is:  5
3
Input Set #1: YES
Input Set #2: NO
Input Set #3: NO
3
Input Set #0: YES
Input Set #1: NO
Input Set #2: NO
1
1 0 1 0
1
1010
1
The judges are mean!
1
The judges are good!
0
'''

sys.stdin = StringIO(input_source)
judge = AutomatedJudge()
sys.stdin = sys.__stdin__