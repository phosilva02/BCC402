class Answer:
    def __init__(self, answer):
        self.answer = answer
        self.numbers = []
        self.initAnswer()
    def initAnswer(self):
        for character in self.answer:
            try:
                n = int(character)
                self.numbers.append(n)
            except:
                continue

class AutomatedJudge:
    def __init__(self):
        self.start()
    def start(self):
        cont = 1
        while True:
            n = int(input())
            if n <= 0:
                break
            standardSolution = []
            for i in range(n):
                answer = Answer(input())
                standardSolution.append(answer)
            m = int(input())
            teamOutput = []
            for i in range(m):
                answer = Answer(input())
                teamOutput.append(answer)
            JudgeAnwsers = []
            for i in range(n):
                correctAnswer = standardSolution[i]
                teamAnswer = teamOutput[i]
                if correctAnswer.answer == teamAnswer.answer:
                    JudgeAnwsers.append("Accepted")
                elif correctAnswer.numbers == teamAnswer.numbers:
                    JudgeAnwsers.append("Presentation Error")
                else:
                    JudgeAnwsers.append("Wrong Answer")
            JudgeAnwsers = list(set(JudgeAnwsers))
            finalAnwser = f"Run #{cont}: "
            if "Wrong Answer" in JudgeAnwsers:
                finalAnwser += "Wrong Answer"
            elif "Presentation Error" in JudgeAnwsers:
                finalAnwser += "Presentation Error"
            else:
                finalAnwser += "Accepted"
            print(finalAnwser)
            cont += 1


            
