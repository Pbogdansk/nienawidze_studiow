class Node:
    id = 0
    x = 0
    y = 0
    bc = 0

    def __init__(self, id, x, y, bc):
        self.id = int(id)
        self.x = float(x)
        self.y = float(y)
        self.bc = bc
