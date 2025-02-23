import igraph as ig
import Levenshtein

class StepLadders:
    def __init__(self):
        self.graph = ig.Graph()
        self.run()

    def isConnected(self, w1, w2):
        dist = Levenshtein.distance(w1, w2)
        if dist <= 1:
            return True
        return False

    def insertIntoGraph(self, word):
        if len(self.graph.vs) == 0:
            self.graph.add_vertex(word)
            return
        conections = []
        for i in self.graph.vs['name']:
            if self.isConnected(word, i):
                conections.append((word, i))
        self.graph.add_vertex(word)
        for i in range(len(conections)):
            # Peso é negativo para calcular qual caminho utilizar via algoritmos de menor caminho, que possuem complexidade polinomial (Jonhson vai ser usado caso tenha menos de 100 vertices. Bellman-Ford caso contrario)
            # Calcular qual o maior caminho de um grafo não possui complexidade polinomial para grafos em geral (existem tipos de grafos especificos que possuem algoritmos
            # especificos capazes de fazerem esse calculo em tempo polinomial, mas nao vem ao caso)
            self.graph.add_edge(conections[i][0], conections[i][1], weight=-1)

    def run(self):
        while True:
            try:
                word = input()
                self.insertIntoGraph(word)
            except EOFError:
                break
        result = [x for sublist in self.graph.shortest_paths(mode='all') for x in sublist]
        result = filter(lambda x: x not in [float('inf'), -float('inf')], result)
        print(max(result))
            
            
            