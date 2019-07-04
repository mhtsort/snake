class Snake():
    def __init__(self,bodylist=[1,2,3]):
        """
        initiates with a list representing the body of the snake
        """
        self.body=bodylist

    def move(self,x):
        self.body.insert(0,x)
        self.body.pop(-1)
    def grow(self,x):
        self.body.insert(0,x)
    def __repr__(self):
        return str(self.body)
