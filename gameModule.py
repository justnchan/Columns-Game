import sys

class Faller(object):
	def __init__(self, row, column, data, size):
		self.row = row
		self.column = column 
		self.data = data
		self.size = size
	def print_data(self):
		print(self.row)
		print(self.column)
		print(self.data)
		print(self.size)


class Game(object):
	def __init__(self):
		self.row = 13
		self.column = 6
		self.game_type = 'EMPTY'
		self.game_board= [[" "]*self.column for i in range(0, self.row)]
		self.faller = Faller(-1, -1, [], 0)
		
	
	# Not needed in GUI
	def print_board(self) -> None:
		"Prints the columns board"
		return

	def remove_faller(self) -> None:
		"Removes faller with empty space"
		for i in range(self.row):
			for j in range(self.column):
				if self.game_board[i][j][0] == "[":
					self.game_board[i][j] = " "

	def lock_faller(self) -> None:
		"Locks faller in place"
		for i in range(self.row):
			for j in range(self.column):
				if (self.game_board[i][j][0] == "|"):
					self.game_board[i][j] = 	self.game_board[i][j].replace("|", "")
					self.game_board[i][j] = 	self.game_board[i][j].replace("|", "")
		self.prepare_board(False)

	def prepare_board(self, content_mode_prepare) -> None:
		"Waits for input from user"
		while (True):
			self.remove_white_space()
			removed = self.check_completed_row()
			if removed == False:
				break
		self.print_board()

	def remove_white_space(self) -> None:
		"Removes white space"
		for i in range(self.column):
			for j in range(self.row-1):
				if (self.game_board[j][i] != " "):
					if (self.game_board[j+1][i] == " "):
						for k in range(j+1, 0, -1):
							self.game_board[k][i] = self.game_board[k-1][i]
						self.game_board[0][i] = " "

	def check_completed_row(self) -> bool:
		"Checks row to see if it is completed, returns boolean"
		returnData = False
		for i in range(self.row):
			for j in range(self.column-2):
				if self.game_board[i][j] == " ":
					continue
				if (self.game_board[i][j] == self.game_board[i][j+1]) and (self.game_board[i][j] == self.game_board[i][j+2]):
					returnData = True
					data = self.game_board[i][j]
					self.game_board[i][j] = "*" + data + "*"
					self.game_board[i][j+1] = "*" + data + "*"
					self.game_board[i][j+2] = "*" + data + "*"
					for k in range(j+3, self.column, 1):
						if self.game_board[i][k] == data:
							self.game_board[i][k] = "*" + data + "*"
							j = k
						else:
							break

		if (returnData == True):			
			self.print_board()
			for i in range(self.row):
				for j in range(self.column):
					if (self.game_board[i][j][0] == "*"):
						self.game_board[i][j] = 	" "
			self.faller.size = 0
		return returnData


	def rotate_faller(self) -> None:
		"Rotates faller"
		temp = self.faller.data[-1]
		for i in range(self.faller.size -1, -1, -1):
			self.faller.data[i] = self.faller.data[i -1]
		self.faller.data[0] = temp

	def new_faller(self, fcolumn, frow, fsize, fdata) -> None:
		"New faller is added"
		self.faller = Faller(frow, fcolumn, fdata, fsize)
		self.add_faller()
		self.print_board()

	def move_left(self) -> None:
		"Function to move faller to left"
		if self.faller.size == 0:
			return
		moveable = True
		if(self.faller.column != 0):
			moveable= True
			if(self.faller.column != 0):
				for i in range(self.faller.row, self.faller.row - self.faller.size, -1):
					if (self.game_board[i][self.faller.column -1]) != " ":
						moveable = False
						break
			else:
				moveable = False
			if moveable == True:
				self.faller.column = self.faller.column - 1
			self.add_faller()
		self.print_board()

	def move_right(self) -> None:
		"Function to move faller to right"
		if self.faller.size == 0:
			return

		moveable = True
		if (self.faller.column != self.column - 1):
			for i in range(self.faller.row, self.faller.row - self.faller.size, -1):
				if (self.game_board[i][self.faller.column+1]) != " ":
					moveable = False
					break
		else:
			moveable = False
		if moveable == True:	
			self.faller.column = self.faller.column + 1
		self.add_faller()
		self.print_board()

	def rotate_faller_command(self) -> None:
		"Function to rotate faller"
		if self.faller.size == 0:
			return
		self.rotate_faller()
		self.add_faller()
		self.print_board()

	def faller_down(self) -> None:
		"Function to move faller down"
		if self.faller.size == 0:
			return
		if self.faller.row == self.row -1:
			self.add_faller()
			self.faller.size = 0
			self.lock_faller()
		else:
			if self.game_board[self.faller.row  +1][self.faller.column] != " ":
				if (self.faller.row - self.faller.size) < 1:
					self.add_faller()
					print("Game over")
					sys.exit()
				else:
					self.add_faller()
					self.faller.size = 0
					self.lock_faller()
			else:
				self.faller.row = self.faller.row + 1
				self.add_faller()
		self.print_board()



	def add_faller(self) -> None:
		"Function to add faller"
		if (self.faller.size != 0):
			index = self.faller.size - 1
			for i in range(self.faller.row, self.faller.row - self.faller.size, -1):
				if (i < 0):
					break
				if self.faller.row == self.row - 1:
					self.game_board[i][self.faller.column] = "|" + self.faller.data[index] + "|"
				elif self.game_board[self.faller.row+1][self.faller.column] != " ":
					self.game_board[i][self.faller.column] = "|" + self.faller.data[index] + "|"
				else:
					self.game_board[i][self.faller.column] = "[" + self.faller.data[index] + "]"
				index = index - 1

	def initialize_content_mode(self):
		for i in range(self.row):
			rowData = input()
			for j in range(self.column):
				self.game_board[i][j] = rowData[j]
		self.prepare_board(True)
