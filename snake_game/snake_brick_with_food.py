'''
Add the food functionality to the snake game

1) A food (yellow square) should appear in a random cell in the board.
2) When a snake's head hits the cell containing the food
	a) The food disappears from that cell
	b) The length of the snake increases by one more square
	c) Another food should appear in a random cell in the board.
	d) Ensure that the random cell in which the food appear is not on the body of the snake or a brick.
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
    brickLog = []

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
        self.brickLog = []
        self.length = length
        self.bodyCoord = []     # A list that holds (row,column) values of top left corner of each of the rectangles that make the snake

        # Initially the snake is the list of length-many squares starting
        # with the head and continuing right.
        for i in range(length):
            sq = GameBoard.squareOn(self.headRow, self.headCol+i, 'white')
            self.bodyCoord.extend([self.headRow,self.headCol+i])                                      # appends first (x,y) values corresponding to first corner to list of corners
            self.body.append(sq)
        self.bodyX = self.bodyCoord[0:len(self.bodyCoord)-1:2]
        self.bodyY = self.bodyCoord[1:len(self.bodyCoord):2]
        print('My bodyx = ',self.bodyX)
        print('My bodyY = ',self.bodyY)


    def funeral(self):
        self.GameBoard.msg = tk.Label(self.GameBoard.gameWindow,text='Game Over',font=('Times',62),bg=self.GameBoard.backGround)     # Function that displays Game over when snake hits a boundary
        self.GameBoard.msg.place(x=self.GameBoard.pixWidth//4,y=self.GameBoard.pixHeight//3)

    def brick(self):                                            # Function to place a brick at a random x,y location and retutn its handle
        MyX = random.randint(1,self.GameBoard.numRows-2)
        MyY = random.randint(1,self.GameBoard.numCols-2)
        print('length of bricklog',len(self.brickLog))
        BrickOnBrick = True
        BrickOnSnake = True
        for i in range(0,len(self.brickLog)-1,2):

            if(self.brickLog[i] == MyX):                        # Checking if new random X already there in brick list
                if(self.brickLog[i+1] == MyY):                  # Chekcing if corresponding Y also there?
                    self.brick()                                # If both yes, find new x,y
                else:
                    BrickOnBrick = False
            else:
                BrickOnBrick = False

        if (MyX in self.bodyX):                                 # check if generated X in body co-rds of snake
            MatchingCoord = []
            for r in range(0,len(self.bodyX)-1):
                if self.bodyX[r] == MyX:
                    MatchingCoord.append(r)
            for t in MatchingCoord:                                         # check if generated Y in body co-rds of snake
                if (self.bodyY[t] == MyY):
                    self.brick()                                # If a matching x and y found, call again
                else:
                    BrickOnSnake = False
        else:
            BrickOnSnake = False                        # else append it to list of bricks

        if(len(self.brickLog) == 0):
            self.brickLog.extend([MyX,MyY]) 
        elif(BrickOnBrick == False and BrickOnSnake == False):
            self.brickLog.extend([MyX,MyY]) 
            BrickHandle = self.GameBoard.squareOn(MyX,MyY,'red')
            return(BrickHandle)    

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

    def PlaceBricks(self):
        self.BrickHandlesList = []
        for i in range(20):
            self.MyHandle = self.brick()                      # calls a fn which place brick at random loc and returns its handle
            self.BrickHandlesList.append(self.MyHandle)
            print('Brick xy is : ',self.brickLog)

    def move(self):
        '''
        Moving is incorporated by dropping one square from the tail and adding
        one square to the next cell based on the current direction of motion.
        '''

        # Find the new location of the head
        self.headRow += self.rowAhead
        self.headCol += self.colAhead
        # Add the new head square 
        newHead = self.GameBoard.squareOn(self.headRow, self.headCol, 'white')
        self.body.insert(0, newHead)
        # Remove the old tail square
        tail = self.body.pop()
        self.GameBoard.remove(tail)

        '''
        If headCol * cellsize = x co-ord of brick or headRow * cellsize = y co-ord of brick; snake has entered brick. Then snake stops moving and calls funeral function

        '''

        print('head col = ',self.headCol)
        print('head row = ',self.headRow)

        if( self.headRow in self.brickLog):             # Finding if any x co-ord of brick matching with X of snake head
            MyXIndex = []
            for l in range(0,len(self.brickLog)-2,2):
                if (self.brickLog[l] == self.headRow):
                    MyXIndex.append(l)

            for h in MyXIndex:
                if(self.headCol == self.brickLog[h+1]):   # Check if Y also same for those x matching
                    self.isAlive = False
                    self.funeral()

        # Schedule the next move after the set delay
        # This is a very confusing thing so read the manual
        if (self.isAlive == True):
            self.GameBoard.gameCanvas.after(self.delay, self.move)

    def accelerate(self):                                       # Increases speed of snake by 2 times
        self.delay //=2

class Game:
    '''
    This is the main class for the Game. This stores all the game
    configurations including those of the board and the snake. This also
    monitors the keyboard and calls the Snake.changeDirection() when one of the
    four arrow keys is pressed.
    '''
    def __init__(self):
        self.boardWidth     = 25
        self.boardHeight    = 35
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
        if not self.Snake.isAlive:
            self.Snake.funeral()
            return

        key = event.keysym
        if key == 'space' and not self.gameOn:
            self.gameOn = True
            self.Snake.PlaceBricks()        # Function to place red brick in random location
            self.Snake.move()
        elif key == 'space' and self.gameOn:
            self.Snake.accelerate()
        elif key in ['Left', 'Right', 'Down', 'Up']:
            self.Snake.changeDirection(key)
        elif key == 'k':
            self.Snake.isAlive = False
        else:
            print(f'{key} not mapped')
            # Any other key will be ignored.
    
if __name__ == "__main__":
    Game()
