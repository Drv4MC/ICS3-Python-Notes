import pygame
import random

class Ball():
    
    def __init__(self, posIn, sizeIn, colorIn):
        """ Create and initialize a ball with the given postision, size and color """

        self.pos = posIn
        self.size = sizeIn
        self.color = colorIn 
        
    def draw(self, surfaceIn):
        pygame.draw.circle(surfaceIn, self.color, self.pos, self.size)
        
    #Add a default behaviour to my ball.  In this case move across the screen
    def update(self):
        self.move(1,0)
        
    def move(self, xIn=0, yIn=0):
        self.pos[0] += xIn
        self.pos[1] += yIn
        
class Wizard():
    
    def __init__(self, imageIn, posIn):
        """ Create and initialize a wizard at this location on the board """
        self.image = imageIn
        self.pos = posIn

    def draw(self, surfaceIn):
        surfaceIn.blit(self.image, self.pos)

    def update(self):
        self.move(1,0)
        
    def move(self, xIn=0, yIn=0):
        self.pos[0] += xIn
        self.pos[1] += yIn
    
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    wizardImage = pygame.image.load("images//dungeon//frames//wizzard_f_idle_anim_f1.png")

 
 
 
#     circles = []
#     for i in range(5):
#         circles.append(Ball([random.randrange(surfaceSize),random.randrange(surfaceSize)], 30, (0, 0, 0)) )
#Instead of just having a list for my circles, I will have a list for ALL of my sprites
    allSprites = []
    for i in range(5):
        allSprites.append(Ball([random.randrange(surfaceSize),random.randrange(surfaceSize)], 30, (0, 0, 0)) )
    ##2#
    allSprites.append( Wizard( wizardImage, [0,random.randrange(surfaceSize)]) )

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))


        #Loop through all of the sprites        
        for i in range(len(allSprites)):
            allSprites[i].update()
            allSprites[i].draw(mainSurface)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
