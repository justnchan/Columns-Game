import pygame
import gameModule
import sys
from pygame.locals import *
import random

def main():
	#color list for blocks
	colorList = [['Z', Color(53, 206, 69)], ['X', Color(96, 240, 233)], ['Y', Color(29, 1, 166)], ['S', Color(231, 13, 13)], ['V', Color(247, 240, 43)], ['W', Color(0, 0, 0)], ['T', Color(204, 111, 111)]]
	#initialize
	row = 13
	column = 6
	pygame.init()
	screen = pygame.display.set_mode((40 * column, 40 * row))

	#set caption
	pygame.display.set_caption('Pygame testing')
	#set mouse visibility
	pygame.mouse.set_visible(0)
	#set background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	#send everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()
	TICKER = pygame.USEREVENT+1
	pygame.time.set_timer(TICKER, 1000)
	#game object
	game = gameModule.Game()
	while 1:
		for event in pygame.event.get():
			game.remove_faller()
			if event.type == QUIT:
				return
			if event.type == KEYDOWN and event.key == K_LEFT:
				game.move_left()
			if event.type == KEYDOWN and event.key == K_SPACE:
				game.rotate_faller()
			if event.type == KEYDOWN and event.key == K_RIGHT:
				game.move_right()
			if event.type == TICKER:
				if game.faller.size == 0:
					faller_data = generate_new_faller(column, colorList)
					game.new_faller(faller_data[1], faller_data[0], faller_data[2], faller_data[3])
				else:
					game.faller_down()
			
			
			for i in range(row):
				for j in range(column):
					if game.game_board[i][j] != " ":
						if game.game_board[i][j][0] == "[" or game.game_board[i][j][0] == "|":
							block_data = game.game_board[i][j][1]
						else:
							block_data = game.game_board[i][j]
						for k in range(len(colorList)):
							if  (colorList[k][0] == block_data):
								color = colorList[k][1]
								break
						pygame.draw.rect(screen, color, (j * 40, i*40, 40, 40))
						pygame.draw.rect(screen, Color(0, 0, 0), (j * 40, i*40, 40, 40), 1)
					else:
						pygame.draw.rect(screen, Color(255, 255, 255), (j * 40, i*40, 40, 40))
						pygame.draw.rect(screen, Color(0, 0, 0), (j * 40, i*40, 40, 40), 1)
		pygame.display.update()

def generate_new_faller(column, colorList):
	row = 0
	column = random.randint(0, column-1)
	size = 3
	block = []
	for i in range(size):
		block.append(colorList[random.randint(0, len(colorList)-1)][0])
	return [row, column, size, block]

if __name__ == '__main__':
	main()