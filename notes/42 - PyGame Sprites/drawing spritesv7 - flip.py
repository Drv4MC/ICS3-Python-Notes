#TODO ADD KEYBOARD Control to make the character move left and right
#TODO Make the sprite would move when clicked

import pygame
import random
import copy

#Wizard Rect: [130,165,16,28]
class Character():
    
    def __init__(self, imageIn, posIn, imageRectIn):
        """ Create and initialize a wizard at this location on the board """
        self.image = imageIn
        self.imageRect = imageRectIn
        self.pos = posIn
        
        #These are needed for the image animation
        self.origImageRect = copy.copy(self.imageRect)
        self.patchNumber = 0; #Start at the initial patch
        self.numPatches = 4;  #Only use 4 patches
        self.frameCount = 0;  #Start at intial frame
        self.animationFrameRate = 10;
        
        #Now let's control the character
        self.canMove = True
        self.direction = True

    def draw(self, surfaceIn):
        #surfaceIn.blit(self.image, self.pos)
        #Kinda fun to have EVERY Image, but let's just get the patch we need
        tempSurface = pygame.Surface( (self.imageRect[2], self.imageRect[2]) )
        tempSurface.set_colorkey((0,0,0))
        tempSurface.blit(self.image, (0,0),  self.imageRect)
        
        if not self.direction:
            tempSurface = pygame.transform.flip(tempSurface,True,False)
        
        surfaceIn.blit(tempSurface, self.pos)  #Positions found using msPaint

    def updateImageRect(self):
        #update the imageRect to show the next image
        if (self.patchNumber < self.numPatches-1) :
            self.patchNumber += 1
            self.imageRect[0] += self.imageRect[2]
        else:
            self.patchNumber = 0
            self.imageRect = copy.copy(self.origImageRect)
               
        #print(f"Patch Number: {self.patchNumber}   Image Rect: {self.imageRect}  {self.origImageRect}")
        

    def update(self):
        if self.canMove: 
            self.frameCount += 1
            if (self.frameCount % self.animationFrameRate == 0):
                self.updateImageRect()
            
            if self.direction:
                self.move(0.5,0)
            else:
                self.move(-0.5,0)
        
    def move(self, xIn=0, yIn=0):
        self.pos[0] += xIn
        self.pos[1] += yIn
    
    def toggleMovement(self):
        self.canMove = not self.canMove
    
    def toggleDirection(self):
        self.direction = not self.direction
        
    
    
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    wizardImage = pygame.image.load("images/dungeon/frames/wizzard_f_idle_anim_f1.png")
    #spriteSheet = pygame.image.load("images//dungeon//0x72_DungeonTilesetII_v1.3.png")
    spriteSheet = pygame.image.load("images/dino/sheets/doux.png")
    
    spriteSheet = pygame.transform.scale2x(spriteSheet)
    

 
 
 
#     circles = []
#     for i in range(5):
#         circles.append(Ball([random.randrange(surfaceSize),random.randrange(surfaceSize)], 30, (0, 0, 0)) )
#Instead of just having a list for my circles, I will have a list for ALL of my sprites
    allSprites = []
    for i in range(10):
        allSprites.append( Character( spriteSheet, [0,random.randrange(surfaceSize)], [248,0,48,70]) )


    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(allSprites)):
                #allSprites[i].toggleMovement()
                allSprites[i].toggleDirection()
        
        #
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
