import pygame

# The car will roll
class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
	def __init__(self, color, width, height):
    	# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

    	# Create an image of the block, and fill it with a color.
    	# This could also be an image loaded from the disk.
		self.image = pygame.Surface([width, height])
		self.image.fill(color)

    	# Fetch the rectangle object that has the dimensions of the image
    	# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()

	def moveRight(self, pixels):
		self.rect.x += pixels
 
	def moveLeft(self, pixels):
		self.rect.x -= pixels

	def moveUp(self, pixels):
		self.rect.y -= pixels
 
	def moveDown(self, pixels):
		self.rect.y += pixels

pygame.init()

# some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
PURPLE = (255, 0, 255)

SCREENWIDTH=2000
SCREENHEIGHT=1000

# open a window
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("mov2Obj")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Cars
playerCar = Block(BLACK, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300
player2Car = Block(RED, 20, 30)
player2Car.rect.x = playerCar.rect.x + 20
player2Car.rect.y = playerCar.rect.y + 30
 
# Add the car to the list of objects
all_sprites_list.add(playerCar)
all_sprites_list.add(player2Car)

carryOn = True
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
	# Quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_x: #Pressing the x Key will quit the game
				carryOn=False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		playerCar.moveLeft(5)
		player2Car.moveLeft(5)
	if keys[pygame.K_RIGHT]:
		playerCar.moveRight(5)
		player2Car.moveRight(5)
	if keys[pygame.K_UP]:
		playerCar.moveUp(5)
		player2Car.moveUp(5)
	if keys[pygame.K_DOWN]:
		playerCar.moveDown(5)
		player2Car.moveDown(5)

	# we update the objects
	all_sprites_list.update()

	# First, clear the screen to white
	screen.fill(WHITE)
	# Then we draw different shapes and line

	#Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
	all_sprites_list.draw(screen)
	# Update the screen with the draw
	pygame.display.flip()

	# Limit to 60 frames
	clock.tick(60)

#Once we have exited the main program loop we can stop the game engine
pygame.quit()