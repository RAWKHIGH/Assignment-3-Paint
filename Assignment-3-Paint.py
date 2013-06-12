# https://github.com/RAWKHIGH/Slot_Machine.git
# Name: Stephen McArthur
# Assinment 2
# Paint

import time, random, pygame
from pygame.locals import *

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

pygame.init()

# Set the width and height of the screen [width,height]
size = [660,600]
screen = pygame.display.set_mode(size)

# Caption
pygame.display.set_caption("Stephen's Paint")

# Loop until the user clicks the exit button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font=pygame.font.Font(None,30)

# Background Image
background_image = pygame.image.load("Paint-Layout.png").convert()


# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            done = True			

	# Tracking mouse position and comparing it to where i want buttons
	if event.type == pygame.MOUSEBUTTONDOWN:
		print ('Mouse Clicked')

						

	
	# Putting Background Image On Screen
	screen.blit(background_image, [0,0])
	
	
    pygame.display.flip()
 
    clock.tick(30) # Limit to 30 frames per second

pygame.quit()