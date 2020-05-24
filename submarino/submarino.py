import itertools

class Submarino:

    def __init__(self):
        self.position = [0, 0, 0, 0]
        self.CARDINALS = ['NORTE', 'LESTE', 'SUL', 'OESTE'] # going clockwise (right)


    def move(self, command):
        direction = self.position[3]
        x = self.position[0]
        y = self.position[1]
        z = self.position[2]

        if command == 'R':
            direction = direction + 1
            if direction > 3:
                direction = 0
        if command == 'L':
            direction = direction - 1
            if direction < 0:
                direction = 3
        if command == 'U':
            z = z -1
            if z < 0:
                z = 0
        if command == 'D':
            z = z + 1

        if command == 'M':
            if direction == 0:
                y = y + 1
            if direction == 1:
                x = x + 1
            if direction == 2:
                y = y - 1
            if direction == 3:
                x = x - 1

        self.position[0] = x
        self.position[1] = y
        self.position[2] = z
        self.position[3] = direction
        print(self.position)

    def run(self, commands):
    
        if isinstance(commands, str):
            commands = list(commands)
            for c in commands:
                self.move(c)
        self.position[3] = self.CARDINALS[self.position[3]]
        return self.position
    

       
