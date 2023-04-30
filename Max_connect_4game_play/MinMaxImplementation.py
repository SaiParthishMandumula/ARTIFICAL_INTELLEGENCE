from MaxConnect4Game import *## we import the maxConnect4Game  file.
import copy## we import  the copy
inf = 99999999

class MinMaxImplementation:## we implement the minmax.

    def FetchResultValue(self,Instance):##it define the results values.
        currentPlayer = self.currentTurn
        if currentPlayer == 1:## for the player1.
            if Instance.player1Score > Instance.player2Score:## to calculate the score for the player1.
                return -inf
            else:
                return (Instance.player1Score * 2) - Instance.player2Score
        if currentPlayer == 2:## for the player2,
            if Instance.player2Score > Instance.player2Score:
                return inf##  it will return the information.
            else:
                return (Instance.player2Score * 2) - Instance.player1Score## it will  make the product of the instance and return the score for the player 2

    def IterateAvailableSlots(self, gameboard):##we need to get the AvailableSlots.
        AvailableSlots = [col for col, val in enumerate(gameboard[0]) if val == 0]##this are the possible moves
        return AvailableSlots## return the availableslot.

    def GetNextPossibleMove(self):##for the game to go for the next decision.
        minValues = []## will create the minvalues.
        AvailableSlots = self.IterateAvailableSlots(self.game.gameBoard)## for the availableslot.
        minValues = [self.FetchMin(self.ComputeBoardInstance(self.game, move),-inf,inf) for move in AvailableSlots]## for the minValues.
        decision = AvailableSlots[minValues.index(max(minValues))]
        return decision## return the game for the decision.

    def ComputeBoardInstance(self, previousGame, column):## for the further board state .
    	PresentGame = copy.deepcopy(previousGame)## the current game status .
    	PresentGame.CurrDepth = 1
    	if previousGame.CurrDepth:
    		PresentGame.CurrDepth += previousGame.CurrDepth

    	for i in range(5, -1, -1):## there is a maximum range .
    		if not PresentGame.gameBoard[i][column]:## if the i is not in the presentgame.
    			PresentGame.gameBoard[i][column] = previousGame.currentTurn
    			PresentGame.pieceCount += 1
    			break;## it will break after it reach the final node.

    	PresentGame.currentTurn = 3 - previousGame.currentTurn
    	PresentGame.checkPieceCount()## we need to check the presentgame piececount.
    	PresentGame.countScore() ## it  will count the present score.
    	return PresentGame## it  will return the presentgame.

    def __init__(self, game, depth):## we need to declare the self ,game and  depth of the game.
    	self.currentTurn = game.currentTurn## to return the current turn.
    	self.game = game
    	self.depth = int(depth)## for the more and further chances of the game.

    def FetchMax(self, Instance, gamma, delta):## to Calculate the maximum value.
    	if Instance.pieceCount == 42 or Instance.CurrDepth == self.depth:##we count the piececount and the current depth.
    		return self.FetchResultValue(Instance)## it will return the  value.
    	currValue = -inf
    	for move in self.IterateAvailableSlots(Instance.gameBoard):
    		newInstance = self.ComputeBoardInstance(Instance,move)
    		currValue = max(currValue,self.FetchMin( newInstance,gamma,delta ))
    		if currValue >= delta:
    			return currValue## for the currValue.
    		gamma = max(gamma, currValue) ## it creates the gamma value.
    	return currValue## it will return the currValue.

    def FetchMin(self, Instance, gamma, delta):## we need to get the min value.
    	if Instance.pieceCount == 42 or Instance.CurrDepth == self.depth:## we count the present instance and the depth value.
    		return self.FetchResultValue(Instance)## it return the fetchresultvalue.
    	currValue = inf
    	for move in self.IterateAvailableSlots(Instance.gameBoard):## it will iterate the slots and that (instance.gameboard)
    		newInstance = self.ComputeBoardInstance(Instance,move)##this  will compute the current board instance.
    	currValue = min(currValue,self.FetchMax(newInstance,gamma,delta ))## we to get the currvalue.
    	if currValue <= gamma:## if the currValue is less than gamma.
    		return currValue## it will return the currvalue.
    	delta = min(delta, currValue)## the another one to Calculate delta.
    	return currValue##it will return the currValue.
