''' Python game code for Tic Tac Toe
 with the implementation of Minimax Algorthm
 Aarya Rajbhandari
'''
import pygame    # library for creating game using python
import sys  # library to access system functions
import math  # library to use math functions


pygame.init() # initializing pygame

# setting width and height of the game screen
g_width = 450
g_height = 450

# calculating the width of each grid for 3x3 board
w = g_width // 3

# setting colors
white = (255, 255, 255)
teal = (0, 128, 128)

# creating the game screen
screen = pygame.display.set_mode((g_width, g_height))

# setting the title of the game screen
pygame.display.set_caption('Tic-Tac-Toe')

# Seting the offset for the game screen
offset = 40


# Creating a class to store game variables and functions
class MainGame():
    # Initialize game variables and functions
    def __init__(self):
        # Initialize game board as a 2D list
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        # Setting symbols for player
        self.human = 'O'
        self.AI = 'X'
        # Set current player as the computer
        self.currentPlayer = self.AI

    # Function to check if a player has won the game
    def CheckWinner(self):

        # checking wins row wise and column wise
        # and returning true if a player wins
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != '':
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != '':
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != '':
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '':
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != '':
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != '':
            return True

        # Checking for diagonal wins
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != '':
            return True

        return False    # Return False if no player has won the game

    # Finding the winner of the game and returning the winner
    def Winner(self):

        # Checking for wins row wise and column wise
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != '':
            # returning the winner
            return self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != '':
            return self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != '':
            return self.board[2][0]
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '':
            return self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != '':
            return self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != '':
            return self.board[0][2]

        # Checking for wins diagonal wise
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != '':
            return self.board[2][0]



    # Check if the game is over
    def BoardFullCheck(self):
        #checking if a player has won
        if self.CheckWinner():
            #print(self.currentPlayer + ' is the winner!')
            pygame.display.set_caption(self.currentPlayer + ' is the winner!')
            return False
        else:
            # check is board is full / Tie
            c = 0
            for i in self.board:
                if '' not in i: # check empty strings in board list
                    c += 1
            if c > 2:
                #print("Game tied!")
                pygame.display.set_caption('Game tied!')
                return False # board full and it's a tie

            else:
                return True # game has not ended yet

    def CheckSpace(self, i, j):
        #checking if space is available
        if self.board[i][j] == '':
            return True
        return False

    # Minimax Algorithm
    def minimax(self, depth, isMaximizing):

        # evaluating if there is a winner in the current game board state
        result = self.Winner()
        if result != None:
            if result == 'X':
                return 10   #AI wins
            elif result == 'O':
                return -10  #HUMAN wins
            else:
                return 0 # TIE

        if isMaximizing: # AI player
            bestScore = -math.inf
            for i in range(0, 3):
                for j in range(0, 3):
                    # Checking if the spot available
                    if (self.board[i][j] == ''):
                        self.board[i][j] = self.AI
                        score = self.minimax(depth + 1, False) #isMaximizing parameter set to False (indicating that it is now the human player's turn
                        self.board[i][j] = ''
                        bestScore = max(score, bestScore)
            return bestScore

        if not isMaximizing: # for human player
            bestScore = math.inf
            for i in range(0, 3):
                for j in range(0, 3):
                    # Is the spot available
                    if (self.board[i][j] == ''):
                        self.board[i][j] = self.human
                        score = self.minimax(depth + 1, True) # setting value of isMaximiser to true to indicate the turn of ai
                        self.board[i][j] = ''
                        bestScore = min(score, bestScore)
            return bestScore

    #finding best move for AI player using minimax function
    def BestMove(self):
        bestScore = -math.inf
        bestMove = None

        # Returning the best score among all the possible moves
        # and storing the corresponding cell as the bestMove.
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '':
                    self.board[i][j] = self.AI
                    s = self.minimax(0, False)
                    self.board[i][j] = ''
                    if s > bestScore:
                        bestScore = s
                        bestMove = [i, j].copy()

        # Making the best move for the AI player on the game board.
        # and updating the board with players symbol

        self.board[bestMove[0]][bestMove[1]] = self.AI

    # checking if a space on the game board has been clicked by the player and updating the game board accordingly
    def checkMouseEvent(self):

        #getting mouse location if a human player
        if self.currentPlayer == self.human:
            mouseLocation = pygame.mouse.get_pos()

            i = mouseLocation[0] // w
            j = mouseLocation[1] // w

            #checking if clicked on a space

            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.CheckSpace(i, j): #Calling function to checking empty cell
                    # updating the board space with players symbol
                    self.board[i][j] = self.human
                    if self.BoardFullCheck():   # checking if player has won
                        self.currentPlayer = self.AI  # changing the current player

        #calling BestMove function if AI and make a move
        elif self.currentPlayer == self.AI:
            self.BestMove()
            # checking if a player has won and then changing the current player
            if self.BoardFullCheck():
                self.currentPlayer = self.human

    #drawing the players respective symbols on the screen based on the positions chosen by the player and the computer
    def display(self):
        # looping through board
        for i in range(0, 3):
            for j in range(0, 3):
                # checking if a space is occupied by either an 'X' or an 'O'.
                if self.board[i][j] == 'X':
                    # Drawing the appropriate symbol on the screen at the corresponding location.
                    pygame.draw.line(screen, white, ((w * i) + offset, (w * j) + offset),
                                     ((w * (i + 1)) - offset, (w * (j + 1)) - offset), 10)
                    pygame.draw.line(screen, white, ((w * i) + offset, (w * (j + 1)) - offset),
                                     ((w * (i + 1)) - offset, (w * j) + offset), 10)
                elif self.board[i][j] == 'O':
                    cx = (w * i + (w * (i + 1))) // 2
                    cy = (w * j + (w * (j + 1))) // 2
                    pygame.draw.circle(screen, teal, (cx, cy), w // 4, 8)

# Creating instance of a MainGame object
Game = MainGame()

while True:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing the 3x3 game board
    for i in range(0, 2):
        pygame.draw.line(screen, white, (0, w * (i + 1)), (g_width, w * (i + 1)), 4)
        pygame.draw.line(screen, white, (w * (i + 1), 0), (w * (i + 1), g_height), 4)
 #checking if game over
    if Game.BoardFullCheck():
        Game.checkMouseEvent()

    Game.display()
    pygame.display.update() #Updating the game board with the move made by the current player.
