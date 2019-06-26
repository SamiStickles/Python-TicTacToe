#TicTacToe Game
print("Let's play Tic-Tac-Toe!")

#while True loop that contains whole program and is continued on if replay is chosen
while True:

	#global gameover variable, changes when someone wins, which triggers board to stop printing
	gameOver = False
	
	#prints 100 new lines in the console to clear the old game out on replay
	clear = "\n" * 30

	#if either player has all three numbers from any of these sets, they win the game
	winCondition = [set([1,2,3]), set([4,5,6]), set([7,8,9]), set([1,4,7]), set([2,5,8]), set([3,6,9]), set([1,5,9]), set([3,5,7])]

	#these variables store all possible moves and the current value of each game tile
	totalMoves = [1,2,3,4,5,6,7,8,9]
	boardMoves = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

	#function to print the board, is called each turn with updated boardMoves
	def printBoard():
		board = f"""
	       |       |       
	   {boardMoves[7]}   |   {boardMoves[8]}   |   {boardMoves[9]}   
	       |       |       
	-------|-------|-------
	       |       |       
	   {boardMoves[4]}   |   {boardMoves[5]}   |   {boardMoves[6]}   
	       |       |       
	-------|-------|-------
	       |       |       
	   {boardMoves[1]}   |   {boardMoves[2]}   |   {boardMoves[3]}   
	       |       |       
	"""
		print(board)

	#prints empty board once before turns begin
	printBoard()

	#this function checks if playerOne entered X or O, if not, it asks repeatedly until X or O are entered
	def checkForXorO():
		while True:
			playerOneShapeInput = (input("Player one, pick X or O. X goes first. ")).upper()
			if playerOneShapeInput in ("X", "O"):
				return playerOneShapeInput
				break
			print("Invalid answer.")

	#this determines the opposite shape and returns it to be assigned to playerTwo
	def setPlayerTwoShape(shape):
		if shape == "X":
			return "O"
		else:
			return "X"

	#actual variable assignments
	playerOneShape = checkForXorO()
	playerTwoShape = setPlayerTwoShape(playerOneShape)

	#this determines who goes next, it is updated with the player that just went
	lastMove = ""

	#when players choose a box, its number is added to their moves array
	playerOneMoveList = []
	playerTwoMoveList = []
	playerOneMessage = "Player one, which spot do you want? Pick 1-9. "
	playerTwoMessage = "Player two, which spot do you want? Pick 1-9. "

	#function for each move, it gets move input, if chosen space is taken, it asks again until a valid spot is chosen
	#them move is then removed from total moves so it cant be picked again and added to dictionary with corresponding shape
	#lastMove is updated to the player that just went, so other player will go next turn, then prints updated board
	def playerMove(player):
		global lastMove
		if player == "one":
			while True:
				playerOneMoveInput = int(input(playerOneMessage))
				if playerOneMoveInput in totalMoves:
					break
				print("That space is taken.")
			playerOneMoveList.append(playerOneMoveInput)
			totalMoves.remove(playerOneMoveInput)
			boardMoves[playerOneMoveInput] = playerOneShape
			lastMove = playerOneShape
		else:
			while True:
				playerTwoMoveInput = int(input(playerTwoMessage))
				if playerTwoMoveInput in totalMoves:
					break
				print("That space is taken.")
			playerTwoMoveList.append(playerTwoMoveInput)
			totalMoves.remove(playerTwoMoveInput)
			boardMoves[playerTwoMoveInput] = playerTwoShape
			lastMove = playerTwoShape
		printBoard()

	#handles first move where either player could be starting
	if playerOneShape == "X":
		playerMove("one")
	else:
		playerMove("two")

	#while loop that controlls player turns
	while not gameOver:
		if lastMove == playerOneShape:
			playerMove("two")
		else:
			playerMove("one")

		#Checks for win, prints win message, and ends game
		for i in winCondition:
			if i.issubset(playerOneMoveList):
				print("Congrats player one, you win!")
				gameOver = True
			elif i.issubset(playerTwoMoveList):
				print("Congrats player two, you win!")
				gameOver = True
		
		#checks if game has been won and breaks loop so tie checker doesnt also trigger if all spots are filled on win
		if gameOver == True:
			break
		
		#Checks for tie, prints tie message, and ends game
		if len(totalMoves) == 0:
			print("Game ended in a tie.")
			gameOver = True

	#while loop that asks for replay
	while True:
		replayAnswer = input("Do you want to play again? ")
		if replayAnswer.upper() in ("YES", "Y", "N", "NO"):
			break
		print("Invalid answer.")
	if replayAnswer.upper() in ("YES", "Y"):
		print(clear)
		continue
	else:
		print("Powering down...")
		break