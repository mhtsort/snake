# SNAKE GAME BY mhtsort 2019
import tkinter as tk
import snake_class as sn

 
class App():
    def __init__(self,root,width=600,height=400):
        self.root=root
        self._STOP=True
        self.speed=200
        #Application width and hegth
        self.width=width
        self.height=height
        self.root.geometry("{}x{}".format(self.width,self.height))
        #Create a Frame on top for buttons and info
        self.frame=tk.Frame (self.root)
        self.frame.pack(fill="x")
        #Create restart button
        self.restart=tk.Button(self.frame,text="restart",command=self.restartgame)
        self.restart.pack(side="left")
        #Create status label and button for development info
        self.debug=tk.Button(self.frame,text="Print status",command=self.printstatus)
        self.debug.pack(side="left")
        self.statuslabel=tk.Label(self.frame,text="Press s to start",background="lightgreen")
        self.statuslabel.pack(side="bottom")
        self.board=Board(20,20)
        self.snake=sn.Snake([(3,5),(4,5),(5,5)])
        self.keybindings()
        print(self.snake)
        #Create canvas based on Board size
        self.canvas=tk.Canvas(root,width=20*20,height=20*20,background="lightblue")
        self.canvas.pack()
    def restartgame(self):
        pass
    def printstatus(self):
        txt=self.board._str_print_board()
        #self.statuslabel.configure(text=txt)
        self.statuslabel.configure(text=self.snake)
        #self.canvas.create_polygon(20,20,20,40,40,40,40,20,outline="red",tag="snake")
        self.drawsnake(self.snake)
    def drawsnake(self,snake):
        self.canvas.delete("snake")
        for tile in snake.body:
            self.drawpart(tile)
            print("Draw {}".format(snake.body))
    def drawpart(self,tile):
        x, y=tile
        x*=20
        y*=20
        self.canvas.create_polygon(x-10,y-10,x+10,y-10,x+10,y+10,x-10,y+10,outline="red",fill="blue",tag="snake")
    def keybindings(self):
        self.root.bind("<Up>",self._up_pressed)
        self.root.bind("<Down>",self._down_pressed)
        self.root.bind("<Left>",self._left_pressed)
        self.root.bind("<Right>",self._right_pressed)
        self.root.bind("s",self.callrun)
        self.root.bind("<space>",self.grow)
    def _up_pressed(self,event):
        self.statuslabel.configure(text="UP PRESSED")
        self.snake.direction(self.snake.UP)
        self.snake.move(self.snake.add(self.snake.head(),self.snake.heading))
    def _down_pressed(self,event):
        self.statuslabel.configure(text="DOWN PRESSED")
        self.snake.direction(self.snake.DOWN)
        self.snake.move(self.snake.add(self.snake.head(),self.snake.heading))
    def _left_pressed(self,event):
        self.statuslabel.configure(text="LEFT PRESSED")
        self.snake.direction(self.snake.LEFT)
        self.snake.move(self.snake.add(self.snake.head(),self.snake.heading))
    def _right_pressed(self,event):
        self.statuslabel.configure(text="RIGHT PRESSED")
        self.snake.direction(self.snake.RIGHT)
        self.snake.move(self.snake.add(self.snake.head(),self.snake.heading))
    def callrun(self,event):
        self._STOP= not self._STOP
        self.run()
    def run(self):
        if self._STOP:return print("stop")
        else:
            self.snake.move(self.snake.add(self.snake.head(),self.snake.heading))
            print("Before lose \n HEAD:   {} \n SNAKE:{}".format(self.snake.head(),self.snake.body))
            if self.lose():
                print("Lose: {}".format(self.lose()))
            else:
                self.drawsnake(self.snake)
                self.root.after(self.speed,self.run)

    def grow(self,event):
        print("EAT")
        self.snake.grow(self.snake.add(self.snake.head(),self.snake.heading))
    def lose(self):
        if self.loseconditions():
            print("Lose conditions True")
            self.statuslabel.configure(text="YOU LOSE",fg="red")
            self.STOP=True
            return True
        else:
            print("Lose conditions False")
            return False
    def loseconditions(self):#TODO
        x,y=self.snake.head()
        print(">>Head in lose conditions x={} y={}".format(x,y))
        borders=self.snake.head()[0]>20 or self.snake.head()[0]<0 or self.snake.head()[1]>20 or self.snake.head()[1]<0
        head_eats_tail= len(self.snake.body)>len(set(self.snake.body))
        if borders or head_eats_tail:return True
        else:return False
class Board():
    def createtiles(self,rows,cols):
        '''
        Creates board with rows number of rows and cols number of cols
        '''
        board=[]
        for i in range(rows):
            board.append([])
            for j in range(cols):
                board[i].append(0)
        return board
    def _printboard(self):
        '''
        Pretty prints matrix reprisenting board for DEBUGING 
        '''
        boardasstring=""
        for i in self.board:
            print(i)
            boardasstring+="{} \n".format(i)
        return boardasstring[:-3] #without the last " \n"
    def _str_print_board(self):
        '''
        Board as string
        '''
        listform=self._printboard()
        listform=listform.replace("[","").replace("]","").replace(","," ")
        return listform
    def __init__(self,horizontal,vertical):
        self.horizontal_tiles_num=horizontal
        self.vertical_tiles_num=vertical
        self.board=self.createtiles(horizontal,vertical)


root = tk.Tk()
app = App(root)
root.mainloop()
