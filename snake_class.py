class Snake():
    UP=(0,-1)
    DOWN=(0,1)
    LEFT=(-1,0)
    RIGHT=(1,0)
    def __init__(self,bodylist=[1,2,3]):
        """
        initiates with a list representing the body of the snake
        """
        self.body=bodylist
        self.heading=self.RIGHT
        self.HEAD=self.body[0]
    def __repr__(self):
        return str(self.body)
    def add(self,x,y):
        if len(x)==len(y):
            if type(x)  is tuple or type(x) is list:
                xlist=list(x)
                ylist=list(y)
                res=[x[i]+y[i] for i,j in enumerate(x)]
            if type(x) is list:
                return list(res)
            if type(x) is tuple:
                return tuple(res)
        else:raise ValueError('lists and tuples only')
    def head(self):
        ''' 
        Return the head of the snake
        '''
        return self.body[0]  #TODO getters setters
    def direction(self,heading):
        self.heading=heading
    def move(self,x):
        '''
        Move snake to x
        example
        s.move(s.add(s.head(),s.heading))
        moves the snake towards s.heading
        '''
        self.body.insert(0,x)
        self.body.pop(-1)
    def grow(self,x):
        self.body.insert(0,x)

    def next(self):
        pass

    
        

