import pygame
import math
import random
import pygame_menu

pygame.init() # inicijuoti pygame module

DIFFICULTY = [1]
clock = pygame.time.Clock()
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 600
surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))# surface yra screen
GREEN = 0,255,0
RED = 255,0,0
BLUE = 0,0,255
YELLOW = 240,220,0
WHITE = 255,255,255
BLACK = 0,0,0

#------------------------------------------ZAIDEJO, PRIESU ir dalinai KULKU KLASE----------------------------------------------------

class Square:
    def __init__(self, color, x, y, width, height, speed):
        #myRect.left The int value of the X-coordinate of the left side of the rectangle.
        #myRect.right The int value of the X-coordinate of the right side of the rectangle.
        #myRect.top The int value of the Y-coordinate of the top side of the rectangle.
        #myRect.bottom The int value of the Y-coordinate of the bottom side.
        self.rect = pygame.Rect(x,y,width,height) #iš pygame x = Left, y = right,w - top, h - bottom
        self.color = color
        self.direction = 'E'
        self.speed = speed

    def move(self):
        if self.direction == 'E': #jeigu judama i desine
            self.rect.x = self.rect.x+self.speed # objekto x pozicija = objekto x pozicija + objekto greitis pixeliais
        if self.direction == 'W':
            self.rect.x = self.rect.x-self.speed
        if self.direction == 'N':
            self.rect.y = self.rect.y-self.speed # objektio y pozicija = objekto y pozicija - objekto greitis pixeliais
        if self.direction == 'S':
            self.rect.y = self.rect.y+self.speed

    def movedirection(self, direction):
        if direction == 'E':
            self.rect.x = self.rect.x+self.speed
        if direction == 'W':
            self.rect.x = self.rect.x-self.speed
        if direction == 'N':
            self.rect.y = self.rect.y-self.speed
        if direction == 'S':
            self.rect.y = self.rect.y+self.speed

    def collided(self, other_rect):
        #Return True if self collided with other_rect
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
#---------------------------------------------------------------------------------------------------------------------

class Bullet(Square):
    def __init__(self, color, x, y, width, height, speed, targetx, targety):# Kulkos parametrai, target y 
        super().__init__(color, x, y, width, height, speed)# super() init padaro taip, kad nereiktu rasyt viso kodo esancio square klaseje
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians, archtangent
        print('atspausdinti kampa laipsniais:', int(angle*180/math.pi))
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y

    #Override
    def move(self):
		
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

#------------------------------------------------IS MENU LOOP'O-------------------------------------------------------
 
def set_difficulty(value, difficulty):
	selected, index = value
	print(f'Selected difficulty: "{selected}" ({difficulty}) at index {index}')
	DIFFICULTY[0] = difficulty
		
		
#------------------------------------------Zaidimo pagrindinis LOOP'as------------------------------------------------
def start_the_game():

	DIFFICULTY

	score = 0
	square_speed = 10
	freq_l,freq_h = (1,60)

	if DIFFICULTY == [1]:
		square_speed = 10
		freq_l,freq_h = (1,60)
		size_x,size_y = (60,60)

	if DIFFICULTY == [2]:
		square_speed = 20
		freq_l,freq_h = (1,30)
		size_x,size_y = (40,40)

	if DIFFICULTY == [3]:
		square_speed = 30
		freq_l,freq_h = (1,4)
		size_x,size_y = (20,20)
		

	done = False
	while not done:
		#Get user input
		input = ''
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				done = True

			elif event.type == pygame.KEYDOWN:
				print(event.key) #Print value of key press
				"""if event.key==119: #w
					sq.direction = 'N'
				if event.key==97: #a
					sq.direction = 'W'
				if event.key==115: #s
					sq.direction = 'S'
				if event.key==100: #d
					sq.direction = 'E'"""
				
				if event.key==32: #bullet(K_SPACE)
					#Fire a bullet
					spawnx = sq.rect.x + sq.rect.width/2 - 10
					b = Square(RED, spawnx,sq.rect.y, 20,20, 20)
					b.direction = 'N'
					bullets.append(b)

			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y = pygame.mouse.get_pos()
				#print(x,y)
				b = Bullet(RED, sq.rect.centerx, sq.rect.centery, 20,20, 20, x,y)
				bullets.append(b)

		#Handle held down keys
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_w]:
			sq.movedirection('N')
		if pressed[pygame.K_a]:
			sq.movedirection('W')
		if pressed[pygame.K_s]:
			sq.movedirection('S')
		if pressed[pygame.K_d]:
			sq.movedirection('E')	
		#Update game objects
		for b in bullets:
			b.move()
		for e in enemies:
			e.move()
		#spawn enemies on the top of the screen and tell them to move down
		if  random.randint(freq_l,freq_h) == 2: #kaip daznai iskrenta
			x = random.randint(0,SCREEN_WIDTH-40)#random spawnas ant x asies#
			e = Square(YELLOW, x,-40, size_x,size_y, square_speed)
			e.direction = 'S'# South - i apacia
			enemies.append(e)# i enemies []
			
		#Check for collisions
		'''for b in bullets:
			for e in enemies:
				if b.collided(e.rect):
					#e.color = WHITE #TESTING
					enemies.remove(e)
					bullets.remove(b)'''
		for i in reversed(range(len(bullets))): #kiekvienam nariui
			for j in reversed(range(len(enemies))):
				if bullets[i].collided(enemies[j].rect):
					#e.color = WHITE #TESTING
					score += 1# score = score+1
					del enemies[j]
					del bullets[i]
					break
				
		#All the drawing
		surface.fill(BLACK) #fill surface with BLACK
		for b in bullets: #kiekvienai kulkai bullets[] liste 
			b.draw(surface) # piesti kulkas ant ekrano
		for e in enemies: # kiekvienam priesui enemies[] liste
			e.draw(surface) # p
		sq.draw(surface)

		font = pygame.font.Font(None, 74)
		text = font.render(str(score), 1, GREEN)
		surface.blit(text, (20,10))

		pygame.display.flip()
		clock.tick(30) #30 FPS
	pygame.quit()
	exit()

#---------------------------------------------------------------------------------------------------------------------

sq = Square(GREEN,200,200,100,100, 10)
bullets = []
enemies = []


#----------------------------------------------PYGAME MENU LOOPA'S----------------------------------------------------
menu = pygame_menu.Menu('Sveiki', 600, 400,
theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Vardas :', default='zaidejas')
menu.add.selector('Lygis :', [('Lengva', 1), ('Vidutiniska', 2), ('Sunku', 3)], onchange=set_difficulty)
menu.add.button('Pradėti', start_the_game)
menu.add.button('Baigti', pygame_menu.events.EXIT)
menu.mainloop(surface)

