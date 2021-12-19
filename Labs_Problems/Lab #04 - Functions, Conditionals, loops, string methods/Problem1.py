# You are playing a game of rock/paper/scissors with a friend. The rules are:

#     'rock' beats 'scissors'
#     'scissors' beats 'paper'
#     'paper' beats 'rock'

# However, you have both had quite a lot to drink, so there is a great deal of noise in your input strings. You cannot assume that all characters are lowercase. Worse, there may be garbage characters in the input strings before and/or after the actual move. (Hint: You can use the find() string method here, the details of which can be found at python.org.) You may assume that every input string does contain exactly one valid move somewhere inside it.

# # Write a function called DoIWin() which takes two string parameters. The first string is your move, the second string is your friend's move. Return True if and only if you win that round - if you lose, or if the round is tied, return False.

def DoIWin(move1, move2):
	moves = [move1.lower(),move2.lower()]
	for i in range(len(moves)):
		if(moves[i].find('scissors') != -1):
			moves[i] = 'scissors'
		elif(moves[i].find('paper') != -1):
			moves[i] = 'paper'
		else:
			moves[i] = 'rock'
	return((moves[0] == 'scissors' and moves[1] == 'paper') or (moves[0] == 'rock' and moves[1] == 'scissors') or (moves[0] == 'paper' and moves[1] == 'rock'))
