class Element:
    id = 0

    def __init__(self, id):
        self.id = int(id)
        self.nodes = []

    def addNode(self, wezel):
        self.nodes += [wezel]
