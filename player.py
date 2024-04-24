import pygame
from sprite import Sprite
from blaster import Blaster

class Player(Sprite):

    def __init__(self):
        Sprite.__init__(self,(0,180),(800, 800), "OPRun.png")
        self.blaster = Blaster()
        self.animationChange("OP IDLE")
        self.mode = "robot"
        self.blaster_visable = False
       
        self.states = {
            "running": False,
            "idle": True,
            "transforming": False,
            "driving": False,
            "shooting": False,
            "gettingBlaster": False,
            "blasterPutAway": False,



        }
    
    def resetStates(self):
        if self.states["transforming"] == False and self.states["gettingBlaster"] == False and self.states["blasterPutAway"] == False:
            for state in self.states:
                self.states[state] = False
            if self.mode == "robot":
                self.states["idle"] = True 
                if self.blaster_visable == False:
                    self.animationChange("OP IDLE") 
                else:
                    self.animationChange("OP BLASTER IDLE")
                    print(self.states)
            if self.mode == "car":
                self.states["driving"] = True 
                self.animationChange("OP DRIVE IDLE")
    def update(self,screen):
        self.handlekeypress()

        if self.states["transforming"] == True:
            if self.mode == "car" and self.frame_num > 7: self.states["transforming"] = False
            elif self.mode == "robot" and self.frame_num == 0: self.states["transforming"] = False

        if self.states["gettingBlaster"] == True:
            if self.frame_num > 5: 
                self.states["gettingBlaster"] = False
                self.blaster_visable = True
                self.resetStates()
                print("getting blaster done")

        if self.states["blasterPutAway"] == True:
            if self.frame_num < 1: 
                self.states["blasterPutAway"] = False
               
            
            

    

        
        #keep playing animation by indexing from animation list.
        
        
        self.surf = self.rightAnim if self.facing == "right" else self.leftAnim
        screen.blit(self.surf[self.frame_num], self.rect.topleft)

        if self.blaster_visable == True:
            self.blaster.draw(screen, self.states, self.frame_num, self.facing)

        if (self.mode == "robot" and self.states["transforming"]) or self.states["blasterPutAway"]:
            self.updateAnimNumberBackwards()
        else:
            self.updateAnimNumber()
        

        print(self.states)
        # print(self.blaster_visable)
        

    def handlekeypress(self):
        pressed_keys = pygame.key.get_pressed()

        #running
        if not self.states["transforming"] and not self.states["gettingBlaster"] and not self.states["blasterPutAway"]:
            if pressed_keys[pygame.K_d]:
                self.facing = "right"
                if not self.states["running"]:
                    if self.mode == "robot":
                        if self.blaster_visable == False:
                            self.animationChange("OP RUN") 
                        else:
                            self.animationChange("OP BLASTER RUN")
                    elif self.mode == "car":
                        self.animationChange("OP DRIVE") 
                    self.states["running"] = True
                    print("running is true")
                    print(self.states["running"])
                    
            elif pressed_keys[pygame.K_a]:
                self.facing = "left"
                if not self.states["running"]:
                    if self.mode == "robot":
                        if self.blaster_visable == False:
                            self.animationChange("OP RUN") 
                        else:
                            self.animationChange("OP BLASTER RUN") 
                    elif self.mode == "car":
                        self.animationChange("OP DRIVE") 
                    self.states["running"] = True
            elif pressed_keys[pygame.K_s]:
                if not self.states["transforming"]:
                    self.states["transforming"] = True
                    self.states["running"] = False
                    self.animationChange("OP TRANSFORM")
                    if self.mode == "robot":
                        self.mode = "car"
                    else:
                        self.mode = "robot"
                        self.frame_num = 8
                        print(self.mode, self.frame_num)
            else:
                self.resetStates()

            if pressed_keys[pygame.K_z]:
                if not self.states["gettingBlaster"] and self.blaster_visable == False:
                    self.states["gettingBlaster"] = True
                    print(self.states)
                    self.animationChange("OP GET BLASTER")
            elif not pressed_keys[pygame.K_z] and not self.states["blasterPutAway"] and self.blaster_visable:
                    self.states["blasterPutAway"] = True
                    self.blaster_visable = False
                    self.animationChange("OP GET BLASTER")
                    self.frame_num = 6
                    
                
                   
            
                
        #idle
            elif not self.states["running"]:
                self.resetStates()


             



    


        