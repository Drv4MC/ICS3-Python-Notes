import pygame
import random
     
class Character():
    
    def __init__(self, imageIn, posIn):
        """ Create and initialize a wizard at this location on the board """
        self.image = imageIn
        self.pos = posIn

    def draw(self, surfaceIn):
        #surfaceIn.blit(self.image, self.pos)
        #Kinda fun to have EVERY Image, but let's just get the patch we need
        surfaceIn.blit(self.image, self.pos, [130,165,16,28])  #Positions found using msPaint
        

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
    spriteSheet = pygame.image.load("images//dungeon//0x72_DungeonTilesetII_v1.3.png")

 
 
 
#     circles = []
#     for i in range(5):
#         circles.append(Ball([random.randrange(surfaceSize),random.randrange(surfaceSize)], 30, (0, 0, 0)) )
#Instead of just having a list for my circles, I will have a list for ALL of my sprites
    allSprites = []
    for i in range(5):
        allSprites.append( Character( spriteSheet, [0,random.randrange(surfaceSize)]) )

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
