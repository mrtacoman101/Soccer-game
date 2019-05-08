

#myfirstPygame
import pygame, sys
pygame.init()
pygame.mixer.music.load('SOCCER ANTHEM OLE OLE OLE.mp3')
pygame.mixer.music.play(-1,  0.0)
img = pygame.image.load('flipped.png')
img1 = pygame.image.load('png-soccer-goal-soccer-goal-post-icon-256.png')
#net
lnet_x = -50
lnet_y = 200
rnet_x = 800
rnet_y = 200
#palyers
#goalkeeper
homegk_x = 50
homegk_y = 350
speed = 5
awaygk_x = 950
awaygk_y = 350
#home
homep1_x = 200
homep1_y = 350
homep2_x = 250
homep2_y = 250
homep3_x = 250
homep3_y = 500
#away
awayp1_x = 750
awayp1_y = 350
awayp2_x = 700
awayp2_y = 250
awayp3_x = 700
awayp3_y = 500
#ball
ball_x = 500
ball_y = 350
#player to control
home_index = 0 #goalie
away_index = 0 #goalie
#variables
FPS = 30
WINDOW_SIZE = (1000, 700)
fps_clock = pygame.time.Clock()
#colors
WHITE = (255, 255, 255)
RED = (222, 17, 17)
BLUE = (0, 8, 250)
GOLD = (17, 30, 222)
GREEN = (84, 193, 52)
BLACK = (0, 0, 0)
LIGHTGREEN = (93, 237, 55)
RUSSIABLUE = (0, 59, 255) 
#set up window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('My Game!')
#defs
def draw_player(x , y, plycolor):
	pygame.draw.circle(screen, plycolor, (x, y), 15)
	rect = pygame.draw.rect(screen, GOLD, (x - 15, y - 15, 30, 30), 1)
	return rect
	
	
"""
This function will check a list of players and see if any of them are
colliding with the ball. If they are approaching from the left it makes
the ball move right. If they kick from the right the ball goes left.
There is no up or down code for this yet.
@param ball will be the hitbox of the ball
@param player_rects is a list of player hitboxes @lam
""" 

def check_ball_collisions(ball, player_rects):
	#loops through all players
	for player in player_rects:
		#checks if the player collides with the ball
		if ball.colliderect(player):
			#checks if ball was kicked from the left
			kick_left = player.right >= ball.right and player.left <= ball.right
			#kicks to right if not left
			kick_right = not kick_left
			#returns negative or positive value to move the ball
			if kick_left:
				return -10
			elif kick_right:
				return 10
	#returns nothing if no player is touching the ball
	return 0
	
#set-up font
my_font = pygame.font.Font('freesansbold.ttf', 12)
text = my_font.render('GER', True, BLACK)
text_rect = text.get_rect()
text_rect.topleft = (50, 100)


my_font = pygame.font.Font('freesansbold.ttf', 12)
text2 = my_font.render('POR', True, BLACK)
text_rect2 = text2.get_rect()
text_rect2.topleft = (100, 100)

"""
we didn't learn this yet...@var players is a list
it allows us to make a list of all players in the game
I use a for loop to put 8 rect objects (0, 0, 0, 0)
These are just placeholders for the real player rects that will
be added during the game loop @lam
"""
players = []
for i in range(8):
	#this adds 8 dummy rects to the list @lam
	players.append((0, 0, 0, 0))

#game loop
while True:
	#draw stuff here!	
	screen.fill(GREEN)
	pygame.draw.line(screen, WHITE, (500,0), (500, 700), 10)
	
	screen.blit(img, (lnet_x, lnet_y))
	screen.blit(img1, (rnet_x, rnet_y))
	players[0] = draw_player(homegk_x , homegk_y, BLACK)
	players[1] = draw_player(awaygk_x , awaygk_y, LIGHTGREEN)
	players[2] = draw_player(homep1_x , homep1_y, RED)
	players[3] = draw_player(awayp1_x , awayp1_y, WHITE)
	players[4] = draw_player(homep2_x , homep2_y, RED) 
	players[5] = draw_player(awayp2_x , awayp2_y, WHITE) 
	players[6] = draw_player(homep3_x , homep3_y, RED) 
	players[7] = draw_player(awayp3_x , awayp3_y, WHITE) 
	pygame.draw.circle(screen, RED, (ball_x, ball_y), 10)
	#hitbox
	ball_rect = pygame.draw.rect(screen, GOLD, (ball_x - 10, ball_y - 10, 20, 20), 1)
	pygame.draw.rect(screen, WHITE, (40,60,100,70))
	screen.blit(text, text_rect)
	screen.blit(text2, text_rect2)
	#player movements
	keystate = pygame.key.get_pressed()
	#select which player to controlg
	if keystate[pygame.K_g]:
		home_index = 0
	if keystate[pygame.K_c]:
		home_index = 1
	
	if keystate[pygame.K_l]:
		away_index = 0
	if keystate[pygame.K_m]:
		away_index = 1
		
	if keystate[pygame.K_w]:
		if home_index == 0:
			homegk_y = homegk_y - speed
		if home_index == 1:
			homep1_y = homep1_y - speed
		if home_index == 2:
			homep2_y = homep2_y - speed
	if keystate[pygame.K_s]:
		if home_index == 0:
			homegk_y = homegk_y + speed
		if home_index == 1:
			homep1_y = homep1_y + speed
		if home_index == 2:
			homep2_y = homep2_y - speed
	if keystate[pygame.K_d]:
		if home_index == 0:
			homegk_x = homegk_x + speed
		if home_index == 1:
			homep1_x = homep1_x + speed
		if home_index == 2:
			homep2_x = homep2_x - speed
	if keystate[pygame.K_a]:
		if home_index == 0:
			homegk_x = homegk_x - speed
		if home_index == 1:
			homep1_x = homep1_x - speed
		if home_index == 2:
			homep2_x = homep2_x - speed
			
	if keystate[pygame.K_UP]:
		if away_index == 0:
			awaygk_y = awaygk_y - speed
		if away_index == 1:
			awayp1_y = awayp1_y - speed
		if away_index == 2:
			awayp2_y = awayp2_y - speed
	if keystate[pygame.K_DOWN]:
		if away_index == 0:
			awaygk_y = awaygk_y + speed
		if away_index == 1:
			awayp1_y = awayp1_y + speed
		if away_index == 2:
			awayp2_y = awayp2_y - speed
	if keystate[pygame.K_RIGHT]:
		if away_index == 0:
			awaygk_x = awaygk_x + speed
		if away_index == 1:
			awayp1_x = awayp1_x + speed
		if away_index == 2:
			awayp2_y = awayp2_y - speed
	if keystate[pygame.K_LEFT]:
		if away_index == 0:
			awaygk_x = awaygk_x - speed
		if away_index == 1:
			awayp1_x = awayp1_x - speed
		if away_index == 2:
			awayp2_y = awayp2_y - speed

	keystate = pygame.key.get_pressed()
	'''
	if keystate[pygame.K_UP]:
		awaygk_y = awaygk_y - speed
	if keystate[pygame.K_DOWN]:
		awaygk_y = awaygk_y + speed
	if keystate[pygame.K_RIGHT]:
		awaygk_x = awaygk_x + speed
	if keystate[pygame.K_LEFT]:
		awaygk_x = awaygk_x - speed
	'''
	ball_x += check_ball_collisions(ball_rect, players)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
	#refresh the screen 
	pygame.display.update()
	fps_clock.tick(FPS)

