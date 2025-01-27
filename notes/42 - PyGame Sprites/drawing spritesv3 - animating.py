import pygame
import random
import copy

#Wizard Rect: [130,165,16,28]
class Character():
    
    def __init__(self, imageIn, posIn, imageRectIn):
        """ Create and initialize a wizard at this location on the board """
        self.image = imageIn #The entire image file
        self.imageRect = imageRectIn #The current part of image to display
        self.pos = posIn #The x and y position of the character
        
        #These are needed for the image animation
        self.origImageRect = copy.deepcopy(self.imageRect)
        self.patchNumber = 0; #Start at the initial patch
        self.numPatches = 4;  #Only use 4 patches
        self.frameCount = 0;  #Start at intial frame
        self.animationFrameRate = 10;

    def draw(self, surfaceIn):
        #surfaceIn.blit(self.image, self.pos)
        #Kinda fun to have EVERY Image, but let's just get the patch we need
        surfaceIn.blit(self.image, self.pos,  self.imageRect)  #Positions found using msPaint
        
        
        #update the imageRect to show the next image
        if (self.patchNumber < self.numPatches-1) :
            self.patchNumber += 1
            self.imageRect[0] += self.imageRect[2]
        else:
            self.patchNumber = 0
            self.imageRect = copy.copy(self.origImageRect)
        
        
        
        print(f"Patch Number: {self.patchNumber}   Image Rect: {self.imageRect}  {self.origImageRect}")
        

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
    #spriteSheet = pygame.image.load("images//dungeon//0x72_DungeonTilesetII_v1.3.png")
    spriteSheet = pygame.image.load("images//dino//sheets//doux.png")
    

 
 
 
#     circles = []
#     for i in range(5):
#         circles.append(Ball([random.randrange(surfaceSize),random.randrange(surfaceSize)], 30, (0, 0, 0)) )
#Instead of just having a list for my circles, I will have a list for ALL of my sprites
    allSprites = []
    for i in range(1):
        allSprites.append( Character( spriteSheet, [0,random.randrange(surfaceSize)], [124,0,24,35]) )

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
        
        clock.tick(5) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
