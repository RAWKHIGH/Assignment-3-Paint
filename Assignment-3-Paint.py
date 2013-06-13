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

# Pen Tool Image
pen_tool_image = pygame.image.load("pen.png").convert()
pen_tool_image.set_colorkey(white)

# Straight line Image
straight_line_image = pygame.image.load("line.png").convert()
straight_line_image.set_colorkey(white)

# Rectangle Image
rectangle_image = pygame.image.load("rectangle.png").convert()
rectangle_image.set_colorkey(white)

# Fill Image
fill_image = pygame.image.load("fill.png").convert()
fill_image.set_colorkey(white)

# Save Image
save_image = pygame.image.load("save.png").convert()
save_image.set_colorkey(white)

# Load Image
load_image = pygame.image.load("load.png").convert()
load_image.set_colorkey(white)

# Eraser Image
eraser_image = pygame.image.load("eraser.png").convert()
eraser_image.set_colorkey(white)







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
	
	# Putting Drawing Canvas On Screen
	drawing_rect = pygame.Surface((600,600))    # the size of the rect
	drawing_rect.fill(white)            		# this fills the entire surface
	screen.blit(drawing_rect, (60,0))		    # draw the drawking screen rectangle
	
	# Putting Pen Tool Image
	screen.blit(pen_tool_image, [0,0])			# image
	pen_rect = pygame.Surface((60,60))  		# the size of the rect
	pen_rect.set_alpha(0)               		# alpha level
	screen.blit(pen_rect, (0,0))				# draw invisible rectangle
	
	# Putting Straight line Image
	screen.blit(straight_line_image, [0,61])	# image
	line_rect = pygame.Surface((60,60))  		# the size of the rect
	line_rect.set_alpha(0)               		# alpha level
	screen.blit(line_rect, (0,61))				# draw invisible rectangle
	
	# Putting Rectangle Image
	screen.blit(rectangle_image, [0,122])		# image
	rectangle_rect = pygame.Surface((60,60))  	# the size of the rect
	rectangle_rect.set_alpha(0)               	# alpha level
	screen.blit(rectangle_rect, (0,122))		# draw invisible rectangle
	
	# Putting Fill Image
	screen.blit(fill_image, [0,427])			# image
	fill_rect = pygame.Surface((60,60))  		# the size of the rect
	fill_rect.set_alpha(0)               		# alpha level
	screen.blit(fill_rect, (0,427))				# draw invisible rectangle
	
	# Putting Fill Colour Image
	fill_colour_rect = pygame.Surface((15,15))  # the size of the rect
	fill_colour_rect.fill(red)            		# this fills the entire surface
	screen.blit(fill_colour_rect, (44,472))		# draw colour rectangle
	
	# Putting Save Image
	screen.blit(save_image, [0,549])			# image
	save_rect = pygame.Surface((30,60))  		# the size of the rect
	save_rect.set_alpha(0)               		# alpha level
	screen.blit(save_rect, (0,183))				# draw invisible rectangle
	
	# Putting Load Image
	screen.blit(load_image, [31,549])			# image
	load_rect = pygame.Surface((30,60))  		# the size of the rect
	load_rect.set_alpha(0)               		# alpha level
	screen.blit(load_rect, (0,183))				# draw invisible rectangle
	
	# Putting eraser Image
	screen.blit(eraser_image, [0,244])			# image
	eraser_rect = pygame.Surface((60,60))  		# the size of the rect
	eraser_rect.set_alpha(0)               		# alpha level
	screen.blit(eraser_rect, (0,244))			# draw invisible rectangle
	
	
	
	
	
	
    pygame.display.flip()
 
    clock.tick(30) # Limit to 30 frames per second

pygame.quit()