'''
An implementation of snake game using Tkinter in Python
'''

import tkinter as tk
import math
import random

class Board:
    ''' 
    This is a class which will present a game board to the user which consists
    of a rectangular grid of cells and methods to shade and clear any selected
    square of this grid. All the tkInter level drawing is to be handled by
    methods inside this class. All external interfaces will interact with the
    Board using row-index and col-index only.  i
    Interface:
        - Intitalization                    :   gB = Board(numRows, numCols)
        - Place a square on a cell          :   sq = gB.squareOn(row, col, <color>)
        - Remove a square from the board    :   gB.remove(sq) 
        - Run the mainloop for the window   :   gB.run()
        - Bind keystrokes to this canvas    :   gB.bindKeysTo(function)
    Some exposed data:
        - Number or rows in the board       :   gB.numRows
        - Number or columns in the board    :   gB.numCols
    '''

    # Parameters for the Board not exposed to the user
    cellSize = 30               # Width and Height of each cell (in pixels)
    backGround = '#638b27'      # Moss Green
    sleepTime = 400             # Time between movements

    def __init__(self, numRows:int, numCols:int):
        self.numRows     = numRows 
        self.numCols     = numCols
        self.pixHeight   = numRows * self.cellSize
        self.pixWidth    = numCols * self.cellSize

        self.gameWindow = tk.Tk()
        self.gameWindow.title('Snake 5.107')

        self.gameCanvas = tk.Canvas(
                self.gameWindow, 
                width=self.pixWidth, height=self.pixHeight, 
                background=self.backGround)
        self.gameCanvas.pack()

        for i in range(0,self.numRows):
            self.squareOn(i,0,'red')
            self.squareOn(i,self.numCols-1,'red')

        for i in range(0,self.numCols):
            self.squareOn(0,i,'red')
            self.squareOn(self.numRows-1,i,'red')

    def squareOn(self, row:int, col:int, color='white'):
        '''
        Places a square on a specified cell of the board and 
        returns a handle to square.
        '''
        size = self.cellSize
        return self.gameCanvas.create_rectangle(col * size, row * size, 
                (col+1) * size, (row+1) * size, fill=color)

    def remove(self, objID):
        '''
        Removes the square (specified by the handle) from the board
        '''
        self.gameCanvas.delete(objID)

    def bindKeysTo(self, function):
        '''
        A tkinter way of saying that whenever a key on the keyboard is pressed
        this function should be called. The function will get the key pressed
        as an argument.
        '''
        self.gameCanvas.bind_all("<Key>", function)
        
    def run(self):
        '''
        After all the setup is done, this brings live the window created 
        '''
        self.gameWindow.mainloop()
        
class Snake:
    '''
    Snake is a self-aware list of squares (represented by their handles)
    arranged in the head to tail order. The self-awareness include:
        - The game board it is on: `self.GameBoard`
        - Whether it is alive: `self.isAlive`
        - The cell where its head is: `self.headRow, self.headCol`
        - Whether is head is on brick or food
        - The direction of its motion: `self.Direction`
        - The off-set to next cell for its head: `self.rowAhead, self.colAhead` 
        - The squares that makes up its body: `self.body`
    Interface:
        1. initialize with the game board and length of snake
        2. Change direction : `changeDirection(direction)` where
            direction in ['Left', 'Right', 'U[', 'Down']
        3. Increase speed : `accelerate()`
        4. `move()` : A recursive call using tkinter's after method 
    '''
    def __init__(self, GameBoard, length:int):
        self.GameBoard = GameBoard

        # Initial condition of the snake
        self.isAlive = True
        self.delay = 256 # milliseconds between each move
        self.headRow = GameBoard.numRows // 2
        self.headCol = GameBoard.numCols // 2
        self.direction = 'Left'
        self.rowAhead = 0
        self.colAhead = -1
        self.body = []
        self.snakeCoords = []
        self.snake_ate = False
        self.length = length
        # Initially the snake is the list of length-many squares starting
        # with the head and continuing right.
        for i in range(length):
            sq = GameBoard.squareOn(self.headRow, self.headCol+i, 'white')
            self.body.append(sq)
            self.snakeCoords.append([self.headRow,self.headCol+i])
        
    def changeDirection(self, direction):
        '''
        Change the direction and the offset to next cell based on the given
        direction unless the given direction is the exact opposite of the
        current direction.
        '''
        if direction == 'Left' and self.direction != 'Right': 
            self.direction  = 'Left'
            self.rowAhead = 0
            self.colAhead = -1
        elif direction == 'Right' and self.direction != 'Left': 
            self.direction  = 'Right'
            self.rowAhead = 0
            self.colAhead = +1
        elif direction == 'Down' and self.direction != 'Up': 
            self.direction  = 'Down'
            self.rowAhead = +1
            self.colAhead = 0
        elif direction == 'Up' and self.direction != 'Down': 
            self.direction  = 'Up'
            self.rowAhead = -1
            self.colAhead = 0

    def food(self):
        self.foodRow = random.randint(1,self.GameBoard.numRows-2)
        self.foodCol = random.randint(1,self.GameBoard.numCols-2)
        if ([self.foodRow,self.foodCol] in self.snakeCoords):
            self.food()
        else:
            self.foodHandle = self.GameBoard.squareOn(self.foodRow,self.foodCol,'yellow')
        return

    def has_eaten(self):
        self.snake_ate = False
        if (self.headRow == self.foodRow and self.headCol == self.foodCol):
            newTailRow = self.headRow+(self.rowAhead*self.length)+self.rowAhead
            newTailCol = self.headCol+(self.colAhead*self.length)+self.colAhead
            newTail = self.GameBoard.squareOn(newTailRow,newTailCol,'white')
            self.body.append(newTail)
            self.snakeCoords.append([newTailRow,newTailCol])
            self.snake_ate = True
            self.GameBoard.remove(self.foodHandle)
        return    

    def move(self):
        '''
        Moving is incorporated by dropping one square from the tail and adding
        one square to the next cell based on the current direction of motion.
        '''

        if ( (self.headRow == 1 and self.rowAhead == -1) or (self.headRow == self.GameBoard.numRows-2 and self.rowAhead == 1)):
            self.isAlive = False
            self.funeral()
            return
        elif ((self.headCol == 1 and self.colAhead == -1) or (self.headCol == self.GameBoard.numCols-2 and self.colAhead == 1)):
            self.isAlive = False
            self.funeral()
            return

        if (self.snake_ate == True):
              self.GameBoard.gameCanvas.after(self.delay, self.food)

        self.has_eaten()

        # Find the new location of the head
        self.headRow += self.rowAhead
        self.headCol += self.colAhead
        # Add the new head square 
        newHead = self.GameBoard.squareOn(self.headRow, self.headCol, 'white')
        self.body.insert(0, newHead)
        # Remove the old tail square
        tail = self.body.pop()
        self.GameBoard.remove(tail)

        self.snakeCoords.insert(0,[self.headRow,self.headCol])
        self.snakeCoords.pop()

        # Schedule the next move after the set delay
        # This is a very confusing thing so read the manual
        if(self.isAlive == True):
            self.GameBoard.gameCanvas.after(self.delay, self.move)

    def funeral(self):
        self.GameBoard.msg = tk.Label(self.GameBoard.gameWindow,text='Game Over',font=('Times',62),bg=self.GameBoard.backGround)     # Function that displays Game over when snake hits a boundary
        self.GameBoard.msg.place(x=self.GameBoard.pixWidth//4,y=self.GameBoard.pixHeight//3)

class Game:
    '''
    This is the main class for the Game. This stores all the game
    configurations including those of the board and the snake. This also
    monitors the keyboard and calls the Snake.changeDirection() when one of the
    four arrow keys is pressed.
    '''
    def __init__(self):
        self.boardWidth     = 21
        self.boardHeight    = 30
        self.snakeLen       =  5
        self.gameOn         = False
        
        # Initialize the board
        self.GameBoard  = Board(self.boardHeight, self.boardWidth)
        
        # Initialize the snake
        self.Snake      = Snake(self.GameBoard, self.snakeLen)

        # Bind all keyboard events from the gameWindow to a method here
        self.GameBoard.bindKeysTo(self.onKeyPress)

        # Start the game
        self.GameBoard.run()

    def onKeyPress(self, event):
        '''
        This is the ear of the game. It listens to the keystroke and takes 
        appropriate action.
            1. Space Bar starts the game 
            2. Arrow keys change the direction of the snake
        '''

        key = event.keysym
        if key == 'space' and not self.gameOn:
            self.gameOn = True
            self.Snake.food()
            self.Snake.move()
        if key == 'space' and self.gameOn:
            self.Snake.delay //=2
        if key == 'k':
            self.Snake.isAlive = False
            self.Snake.funeral()
        elif key in ['Left', 'Right', 'Down', 'Up']:
            self.Snake.changeDirection(key)
        # else:
        #     print(f'{key} not mapped')
        #     # Any other key will be ignored.
    
if __name__ == "__main__":
    Game()
