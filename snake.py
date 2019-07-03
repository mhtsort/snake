# SNAKE GAME BY mhtsort 2019
import tkinter as tk

class App():
    def __init__(self,root,width=600,heigth=400):
        self.width=width
        self.heigth=heigth
        self.root=root
        self.root.geometry("{}x{}".format(self.width,self.heigth))
        self.frame=tk.Frame (self.root)
        self.frame.pack(fill="x")
        self.restart=tk.Button(self.frame,text="restart",command=self.restartgame)
        self.restart.pack()
        self.debug=tk.Button(self.frame,text="restart",command=self.printstatus)
        self.debug.pack()
        self.statuslabel=tk.Label(self.frame,text="Status",background="lightgreen")
        self.statuslabel.pack(side="bottom")
        self.board=Board(10,10)

    def restartgame(self):
        pass
    def printstatus(self):
        self.board._printboard()
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
        for i in self.board:
            print(i)
        
    def __init__(self,horizontal,vertical):
        self.horizontal_tiles_num=Null
        self.vertical_tiles_num=Null
        self.tiles=[(i,j) for i in horizontal_tiles ]
        self.board=self.createtiles(horizontal,vertical)
        

root = tk.Tk()
app = App(root)
root.mainloop()
