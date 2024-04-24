import pygame
import math

animDictionary = {
    "OP RUN": {
        "numFrames": 4,
        "numRows": 3,
        "numCols": 3,
        "allFramesImage": "Images/OPRun.png"
    },
    "OP IDLE": {
        "numFrames": 1,
        "numRows": 3,
        "numCols": 3,
        "allFramesImage": "Images/OPTransform.png"
    },

    "OP TRANSFORM": {
        "numFrames": 9,
        "numRows": 3,
        "numCols": 3,
        "allFramesImage": "Images/OPTransform.png"
    },
     "OP DRIVE": {
        "numFrames": 7,
        "numRows": 3,
        "numCols": 3,
        "allFramesImage": "Images/OPDrive.png"

    },
    "OP DRIVE IDLE": {
        "numFrames": 1,
        "numRows": 3,
        "numCols": 3,
        "allFramesImage": "Images/OPDrive.png"

    },
    "OP GET BLASTER": {
        "numFrames": 7,
        "numRows": 3,
        "numCols": 3,
        "allFramesImage": "Images/OPBlasterGet.png"

    },
    "OP BLASTER RUN": {
        "numFrames": 4,
        "numRows": 3,
        "numCols": 3,
        "allFramesImage": "Images/OPRunWithBlaster.png"

    },
    "OP BLASTER IDLE": {
        "numFrames": 1,
        "numRows": 3,
        "numCols": 3,
        "allFramesImage": "Images/OPBlasterIdle.png"
    },
    
}

class Sprite:
    

    def __init__(self,pos,size,image):
        self.surf = pygame.image.load("Images/"+image).convert_alpha()
        self.surf = pygame.transform.scale(self.surf,size)
        self.rect = self.surf.get_rect(topleft=pos)
        self.frame_num = 0
        self.facing = "right"
        self.size = size

    def draw(self,SCREEN):
        SCREEN.blit(self.surf,self.rect)

    def rotateSprite(self, angle):
        rotated_surf = pygame.transform.rotate(self.surf, angle)
        rotated_surface_rect = rotated_surf.get_rect(center = self.rect.center)
        return (rotated_surf, rotated_surface_rect)
    
    def calculateAngle(self, pos1, pos2):
        dx = pos2[0] - pos1[0]
        dy = pos1[1] - pos2[1]
        angle = math.atan2(dy,dx)
        angle = math.degrees(angle)
        return angle 

    
    def moveLeft(self,speed):
        self.rect.move_ip((-speed),0)
        self.facing = "left"
    
    def moveRight(self,speed):
        self.rect.move_ip((speed),0)
        self.facing = "right"
    
    
    
    
    
    def getAnimFrameRegion(self, row, col):
        w = self.size[0] / self.anim["numCols"]
        h = self.size[1] / self.anim["numRows"]
        x = w * col
        y = h * row
        return (x, y, w, h)

    def updateAnimNumber(self):
        self.frame_num += 1
        if self.frame_num >= self.anim["numFrames"]:
            self.frame_num = 0

    def updateAnimNumberBackwards(self):
        self.frame_num -= 1
        if self.frame_num < 0:
            self.frame_num = self.anim["numFrames"] - 1
        

    def animationChange(self, anim):
        self.anim = animDictionary[anim]
        self.flipSprite()
        self.frame_num = 0
        self.surf = self.rightAnim


    def flipSprite(self):
        allFramesImg = pygame.image.load(
            self.anim["allFramesImage"])
        # .convert_alpha()
        allFramesImg = pygame.transform.scale(allFramesImg,self.size)
        self.rightAnim = []
        self.leftAnim = []
        framesAdded = 0
        for row in range(self.anim["numRows"]):
            for col in range(self.anim["numCols"]):
                if framesAdded < self.anim["numFrames"]:
                    cropped_region = self.getAnimFrameRegion(row, col)
                  
                    croppedSurface = allFramesImg.subsurface(cropped_region)
                    self.rightAnim.append(croppedSurface)
                    flippedSurface = pygame.transform.flip(
                        croppedSurface, True, False)
                    self.leftAnim.append(flippedSurface)
                    framesAdded += 1

#platform1 = Sprite((1,1),(5,5),"OP Run.png")
#platform1.moveLeft(1)
