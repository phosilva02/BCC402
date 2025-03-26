import igraph as ig
        
class War:
    def __init__(self):
        self.run()
    
    def run(self):
        people = int(input())
        self.friendsGraph = ig.Graph(n=people)
        self.enemiesGraph = ig.Graph(n=people)
        while True:
            command, p1, p2 = input().split(" ")
            if command == "0":
                break
            if command == "1":
                result = self.setFriends(int(p1), int(p2))    
            elif command == "2":
                result = self.setEnemies(int(p1), int(p2))
            elif command == "3":
                result = self.areFriends(int(p1), int(p2))
            elif command == "4":
                result = self.areEnemies(int(p1), int(p2))
            else:
                raise Exception("Invalid command")
            self.propagate()
            if result is not None:
                print(int(result))
    
    def setFriends(self, p1, p2):
        if self.enemiesGraph.are_adjacent(p1, p2):
            return -1
        self.friendsGraph.add_edge(p1, p2)
        return
    def setEnemies(self, p1, p2):
        if self.friendsGraph.are_adjacent(p1, p2):
            return -1
        self.enemiesGraph.add_edge(p1, p2)
        return
    def areFriends(self, p1, p2):
        return self.friendsGraph.are_adjacent(p1, p2)
    def areEnemies(self, p1, p2):
        return self.enemiesGraph.are_adjacent(p1, p2)
    #Funcao que serve para propagar as relações, preservando suas propriedades
    def propagate(self):
        matFriends = self.friendsGraph.shortest_paths(mode='all')
        for i in range(len(matFriends)):
            for j in range(len(matFriends[i])):
                if matFriends[i][j] in [float('inf'), - float('inf'), 0] or self.friendsGraph.are_adjacent(i, j):
                    continue
                #Amigo do meu amigo é meu amigo
                self.friendsGraph.add_edge(i, j)

        for vertex in self.enemiesGraph.vs:
            enemies = self.enemiesGraph.neighbors(vertex.index)
            friends = self.friendsGraph.neighbors(vertex.index)
            for enemy in enemies:
                for friend in friends:
                    if self.enemiesGraph.are_adjacent(friend, enemy):
                        continue
                    #Amigo do meu inimigo é meu inimigo
                    self.enemiesGraph.add_edge(friend, enemy)
                for enemy2 in enemies:
                    if self.friendsGraph.are_adjacent(enemy2, enemy) or enemy2 == enemy:
                        continue
                    #Inimigo do meu inimigo é meu amigo
                    self.friendsGraph.add_edge(enemy2, enemy)

        


            
            
            