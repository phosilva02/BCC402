class Shoemaker:
    def __init__(self):
        self.run()
    def run(self):
        numCases = int(input())
        for i in range(numCases):
            n = input()
            if n == '':
                n = input()
            n = int(n)
            orders = []
            for j in range(n):
                order = input().split(" ")
                orders.append([int(order[0]), int(order[1]), j+1])
            #Regra de ordenação: Ordenando pelo pedido que paga mais por dia   
            orders.sort(key= lambda order : order[0] / order[1])
            finalAnswer = ""
            for order in orders:
                finalAnswer += f"{order[2]} "
            print(finalAnswer.rstrip())
            