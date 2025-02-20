import copy

class TugOfWar:
    def __init__(self):
        self.weights = []
        self.bestSolution = []
        self.diff = -1
        self.run()
    
    def isViable(self, newSolution):
        teamA = []
        teamB = []
        for i in newSolution:
            if i is None:
                continue
            if i == 1:
                teamA.append(True)
            else:
                teamB.append(True)
        half = len(self.weights) // 2
        return max(half, len(self.weights) - half) - max(len(teamA), len(teamB)) >= 0
    
    def processSolution(self, newSolution):
        teamA = []
        teamB = []
        for k,v in enumerate(newSolution):
            if v is None:
                return
            if v == 1:
                teamA.append(self.weights[k])
            else:
                teamB.append(self.weights[k])
        diff = abs(sum(teamA) - sum(teamB))
        if diff <= self.diff:
            self.bestSolution = copy.deepcopy(newSolution)
            self.diff = diff

    def backTracking(self, depth, solution=[]):
        if depth == len(self.weights):
            self.processSolution(solution)
        else:
            depth +=1
            candidates = [1, 2]
            for candidate in candidates:
                if len(solution) >= depth:
                    solution[depth-1] = candidate
                else:
                    solution.append(candidate)
                if self.isViable(solution):
                    self.backTracking(depth, solution)
                solution[depth-1] = None
        

    def run(self):
        cases = int(input())
        for case in range(cases):
            n = input()
            if n == '':
                n = input()
            n = int(n)
            self.weights = []
            for i in range(n):
                self.weights.append(int(input()))
            self.diff = sum(self.weights)
            self.backTracking(0)
            teamA = []
            teamB = []
            for k,v in enumerate(self.bestSolution):
                if v == 1:
                    teamA.append(self.weights[k])
                else:
                    teamB.append(self.weights[k])
            print(f"{min(sum(teamA), sum(teamB))} {max(sum(teamA), sum(teamB))}")
            
            
            