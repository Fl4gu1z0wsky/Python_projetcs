import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('background.png')

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyMove = []
num_of_enemies = 6

for i in range(num_of_enemies):
	enemyImg.append(pygame.image.load('enemy.png'))
	enemyX.append(random.randint(0, 736))
	enemyY.append(random.randint(20, 50))
	enemyMove.append(-2)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = playerY
bulletY_change = 10
bullet_state = "ready" # You can't see the bullet on the screen - Fire, the bullet is currently moving

# Score
score = 0

def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y, i):
	screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt((math.pow((enemyX - bulletX), 2)) + (math.pow((enemyY - bulletY), 2)))
	if distance < 27:
		return True
	else:
		return False

# Game loop
running = True

while running:

	screen.blit(background, (0, 0))

	# Quit the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Key events
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			playerX -= 5
		if event.key == pygame.K_RIGHT:
			playerX += 5
		if event.key == pygame.K_SPACE:
			if bullet_state == "ready":
				bulletX = playerX
				fire_bullet(bulletX, playerY)

	# Not going out !
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	# Bullet reset
	if bulletY <= -10:
		bullet_state = "ready"
		bulletY = playerY

	# Bullet Movement
	if bullet_state == "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change

	

	# Enemy movements
	for i in range(num_of_enemies):
		enemyX[i] += enemyMove[i]
		if enemyX[i] <= 0:
			enemyX[i] = 0
			enemyY[i] += 40
			enemyMove[i] *= -1
		elif enemyX[i] >= 736:
			enemyX[i] = 736
			enemyY[i] += 40
			enemyMove[i] *= -1

		# Collision
		collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision:
			bulletY = 480
			bullet_state = "ready"
			score += 1
			enemyX[i] = random.randint(0, 736)
			enemyY[i] = random.randint(20, 50)

		enemy(enemyX[i], enemyY[i], i)

	player(playerX, playerY)
	
	pygame.display.update()


'''
https://stackoverflow.com/questions/21598872/how-to-create-multiple-class-objects-with-a-loop-in-python/21598969
objs = [MyClass() for i in range(10)]
for obj in objs:
    other_object.add(obj)

objs[0].do_sth()
'''