# SNAKE GAME BY mhtsort 2019
import tkinter as tk

class App():
    def __init__(self,root,width=600,height=400):
        self.root=root
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
        self.debug=tk.Button(self.frame,text="print status",command=self.printstatus)
        self.debug.pack(side="left")
        self.statuslabel=tk.Label(self.frame,text="Status",background="lightgreen")
        self.statuslabel.pack(side="bottom")
        self.board=Board(10,10)

    def restartgame(self):
        pass
    def printstatus(self):
        self.board._printboard()
        self.statuslabel.configure(text="TODO")
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
            boardasstring+="\n {}".format(i)
        print("___________")
        return boardasstring
    def __init__(self,horizontal,vertical):
        self.horizontal_tiles_num=horizontal
        self.vertical_tiles_num=vertical
        self.board=self.createtiles(horizontal,vertical)
        

root = tk.Tk()
app = App(root)
root.mainloop()
