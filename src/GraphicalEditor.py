class Command:
    def __init__(self, command):
        self.validIds = ['I', 'C', 'L', 'V', 'H', 'K', 'F', 'S', 'X']
        s = command.upper().strip().split()
        self.id = s[0]
        self.parameters = s[1:]
    
    def validateCommand(self):
        if self.id not in self.validIds:
            raise Exception("Command not found")
        if self.id == 'I':
            if len(self.parameters) != 2:
                raise Exception(f"I command expect 2 parameters instead of {len(self.parameters)}")
            m = int(self.parameters[0])
            n = int(self.parameters[1])
            if (m < 1 or m > 250) or (n < 1 or n > 250):
                raise Exception("1 <= M, N <= 250")
        if self.id == 'L':
            if len(self.parameters) != 3:
                raise Exception(f"L command expect 3 parameters instead of {len(self.parameters)}")
        if self.id == 'V':
            if len(self.parameters) != 4:
                raise Exception(f"V command expect 4 parameters instead of {len(self.parameters)}")
        if self.id == 'H':
            if len(self.parameters) != 4:
                raise Exception(f"H command expect 4 parameters instead of {len(self.parameters)}")
        if self.id == 'K':
            if len(self.parameters) != 5:
                raise Exception(f"K command expect 5 parameters instead of {len(self.parameters)}")
        if self.id == 'F':
            if len(self.parameters) != 3:
                raise Exception(f"F command expect 3 parameters instead of {len(self.parameters)}")
        if self.id == 'S':
            if len(self.parameters) != 1:
                raise Exception(f"S command expect 1 parameters instead of {len(self.parameters)}")

class GraphicalEditor:
    def __init__(self):
        self.table = []
        self.run()
    def run(self):
        endOfProgram = False
        while not endOfProgram:
            try:
                c = input("Enter a command ")
                command = Command(c)
                command.validateCommand()
                if command.id == 'I':
                    self.createTable(command.parameters)
                if command.id == 'C':
                    self.clearTable()
                if command.id == 'L':
                    self.colorPixel(command.parameters)
                if command.id == 'V':
                    self.drawVerticalLine(command.parameters)
                if command.id == 'H':
                    self.drawHorizontalLine(command.parameters)
                if command.id == 'K':
                    self.drawRetangle(command.parameters)       
                if command.id == 'F':
                    self.fillPixels(command.parameters)
                if command.id == 'S':
                    self.printTable(command.parameters)
                if command.id == 'X':
                    endOfProgram = True
            except Exception as e:
                print("Error: ", e)
                continue

    def createTable(self, parameters):
        self.table = []
        lines = int(parameters[1])
        columns = int(parameters[0])
        for i in range(lines):
            line = []
            for j in range(columns):
                line.append('0')
            self.table.append(line)

    def clearTable(self):
        for line in self.table:
            for pixel in line:
                pixel = '0'
    
    def colorPixel(self,parameters):
        x = int(parameters[0])
        y = int(parameters[1])
        c = parameters[2]
        if x <= 0 or y <= 0 or x > len(self.table[0]) or y > len(self.table):
            raise Exception("Pixel out of bounds")
        self.table[y-1][x-1] = c

    def drawVerticalLine(self,parameters):
        x = int(parameters[0])
        
        if int(parameters[1]) <= int(parameters[2]):
            y1 = int(parameters[1])
            y2 = int(parameters[2])
        else:
            y1 = int(parameters[2])
            y2 = int(parameters[1])
        
        c = parameters[3]

        if x <= 0 or y1 <= 0 or y2 <= 0 or x > len(self.table[0]) or y1 > len(self.table) or y2 > len(self.table):
            raise Exception("Pixel out of bounds")

        for i in range((y2-y1+1)):
            self.table[y1-1+i][x-1] = c

    def drawHorizontalLine(self, parameters):
        y = int(parameters[2])
        
        if int(parameters[0]) <= int(parameters[1]):
            x1 = int(parameters[0])
            x2 = int(parameters[1])
        else:
            x1 = int(parameters[1])
            x2 = int(parameters[0])
        
        c = parameters[3]

        if y <= 0 or x1 <= 0 or x2 <= 0 or x1 > len(self.table[0]) or x2 > len(self.table[0]) or y > len(self.table):
            raise Exception("Pixel out of bounds")

        for i in range((x2-x1+1)):
            self.table[y-1][x1-1+i] = c

    def drawRetangle(self, parameters):
        x1 = min(int(parameters[0]), int(parameters[1]))
        x2 = max(int(parameters[0]), int(parameters[1]))

        y1 = min(int(parameters[2]), int(parameters[3]))
        y2 = max(int(parameters[2]), int(parameters[3]))
        
        c = parameters[4]

        for i in range(y2-y1 + 1):
            self.drawHorizontalLine([x1, x2, y1+i, c])

    def fillPixels(self, parameters, regionColor=''):
        x = int(parameters[0])
        y = int(parameters[1])
        c = parameters[2]
        #print(f"AVAL d({y},{x})")
        if x <= 0 or y <= 0 or x > len(self.table[0]) or y > len(self.table):
            #print(f"({y},{x}) Out of bonds")
            return
        if regionColor != '' and regionColor != self.table[y-1][x-1]:
            #print(f"({y},{x}) -> {self.table[y-1][x-1]} != {regionColor}")
            return
        oldColor = self.table[y-1][x-1]
        self.table[y-1][x-1] = c
        self.fillPixels([x-1,y,c], oldColor)
        self.fillPixels([x+1,y,c], oldColor)
        self.fillPixels([x,y-1,c], oldColor)
        self.fillPixels([x,y+1,c], oldColor)


    def printTable(self, parameters):
        filename = parameters[0]
        print(filename)
        s = ''
        for line in self.table:
            for pixel in line:
                s += (pixel + " ")
            s += "\n"
        print(s)
        



    