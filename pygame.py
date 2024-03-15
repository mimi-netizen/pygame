import pygame
# line 1: import pygame and let it serve us

run = True #the program will run as long as the run variable is True
width = 400 #determine the window's size
height = 100 #determine the window's size
pygame.init() #initialize the pygame environment
screen = pygame.display.set_mode((width, height)) #prepare the application window and set its size
font = pygame.font.SysFont(None, 48) #make an object representing the default font of size 48 points
text = font.render("Welcome to pygame", True, (255, 255, 255)) 
  #make an object representing a given text – the text will be anti-aliased (True) and white (255,255,255)
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
  #insert the text into the (currently invisible) screen buffer
pygame.display.flip() #flip the screen buffers to make the text visible
while run: #the pygame main loop starts here
  for event in pygame.event.get(): #get a list of all pending pygame events
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    #lines 17 through 19: check whether the user has closed the window or clicked somewhere inside it or pressed any key
    run = False #if yes, stop executing the code.