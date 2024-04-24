import pygame
from sprite import Sprite

class Blaster(Sprite):
    
    def __init__(self):
        Sprite.__init__(self,(125,305), (34,17), "OPBlaster.png")
        self.angle = 0
        self.facing = "right"
        self.starting_pos = self.rect.bottomleft
      

    def draw(self,SCREEN, player_state, player_frame_num, playerfacing):
        print(self.angle)
        r_surf, r_rect = self.rotateSprite(self.angle)
        SCREEN.blit(r_surf, r_rect)
        mouse_pos = pygame.mouse.get_pos()
        self.angle = self.calculateAngle(self.rect.topleft, mouse_pos)
        if playerfacing == "right": 
            if self.angle > 90:
                self.angle = 90
            if self.angle < -90:
                self.angle = -90
        # else:
        #     if self.angle < 90:
        #         self.angle = 90
        #     if self.angle > -90:
        #         self.angle = -90
       
        if self.angle < 25 and player_state["running"] == False:
            self.rect.topleft = (125,305)
        else:
            self.rect.topleft = (125,295)
        
        if player_state["running"]:
            if player_frame_num % 2 == 0:
                self.rect.move_ip((0,-8)) 
            else:
                self.rect.move_ip((0,8)) 
            

    def flipBlaster(self):
        self.surf = pygame.transform.flip(self.surf, False, True)
