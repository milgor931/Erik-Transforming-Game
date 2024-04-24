import pygame
from player import Player

class Game:
    def __init__(self,SCREEN, WIDTH, HEIGHT):
        self.SCREEN = SCREEN
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.level = 0  #0 = hubworld
        self.scene = "hubworld"
        self.scroll_speed = 10
        self.running_scroll_speed = 50
        self.direction = "right"

        #background objects setup
        self.bg_surf1 = pygame.image.load("Images/Background_objects.png").convert_alpha()
        self.bg_surf1 = pygame.transform.scale(self.bg_surf1, (self.WIDTH, self.HEIGHT))
        self.bg_rect1 = self.bg_surf1.get_rect(topleft=(0,5))
        self.bg_surf2 = self.bg_surf1.copy()
        self.bg_rect2 = self.bg_rect1.copy()
        self.bg_rect2.left = self.WIDTH

        #ground setup
        self.floor_surf1 = pygame.image.load("Images/FLOOR.png").convert_alpha()
        self.floor_surf1 = pygame.transform.scale(self.floor_surf1, (self.WIDTH, self.HEIGHT))
        self.floor_rect1 = self.floor_surf1.get_rect(topleft=(0,0))
        self.floor_surf2 = self.floor_surf1.copy()
        self.floor_rect2 = self.floor_rect1.copy()
        self.floor_rect2.left = self.WIDTH
        
        self.floor_leader = self.floor_rect1
        self.floor_follower = self.floor_rect2
        self.bg_leader = self.bg_rect1
        self.bg_follower = self.bg_rect2

        #player stuff
        self.player = Player()

    
    def scroll(self,scrollDirection):

        speed = self.scroll_speed
        bg_offset = 5
        floor_offset = 0

        if self.player.states["running"] and self.player.mode == "car":
            speed = self.running_scroll_speed
            bg_offset = 6
            floor_offset = 10

        #Note: set one background to "leader" and one to follower and reset leader and follower when learder is completely offscreen. 
        # Leader's top right top right pos is followers top left pos.

        "If scroll direction is right"
        "floor1 = leader"
        "floor2 = follower"


        "if leader topleft is at edge"
        "leader topright go to follower topleft"
        "leader = follower"
        "follower = leader"

        
        if scrollDirection == "right":
            #move leader background
            self.bg_leader.move_ip(-speed/2,0)
            self.floor_leader.move_ip(-speed,0)

            #update follower background position
            self.bg_follower.topleft = self.bg_leader.topright
            self.floor_follower.topleft = self.floor_leader.topright

            #reset leader and follower if offscreen
            if self.bg_leader.right <= 0:
                temp_leader = self.bg_leader
                self.bg_leader.topright = self.bg_follower.topleft
                self.bg_leader = self.bg_follower
                self.bg_follower = temp_leader

            if self.floor_leader.right <= 0:
                temp_leader_floor = self.floor_leader
                self.floor_leader.topright = self.floor_follower.topleft
                self.floor_leader = self.floor_follower
                self.floor_follower = temp_leader_floor

            if self.direction != scrollDirection:
                self.bg_leader.topright = self.bg_follower.topleft
                if self.bg_follower.right <= 0:
                    temp_leader = self.bg_leader
                    self.bg_leader.topright = self.bg_follower.topleft
                    self.bg_leader = self.bg_follower
                    self.bg_follower = temp_leader


        if scrollDirection == "left":
            #move leader background
            self.bg_leader.move_ip(speed/2,0)
            self.floor_leader.move_ip(speed,0)

            #update follower background position
            self.bg_follower.topright = self.bg_leader.topleft
            self.floor_follower.topright = self.floor_leader.topleft

            #reset leader and follower if offscreen
            if self.bg_leader.left >= self.WIDTH:
                temp_leader = self.bg_leader
                self.bg_leader.topleft = self.bg_follower.topright
                self.bg_leader = self.bg_follower
                self.bg_follower = temp_leader
                
            if self.floor_leader.left >= self.WIDTH:
                temp_leader_floor = self.floor_leader
                self.floor_leader.topleft = self.floor_follower.topright
                self.floor_leader = self.floor_follower
                self.floor_follower = temp_leader_floor
    

        
        # if scrollDirection == "right":
        #     if self.bg_rect1.right <= 0:
        #         self.bg_rect1.left = self.WIDTH
        #     if self.bg_rect2.right <= 0:
        #         self.bg_rect2.left = self.WIDTH
        #     if self.floor_rect1.right <= 0:
        #         self.floor_rect1.left = self.WIDTH
        #     if self.floor_rect2.right <= 0:
        #         self.floor_rect2.left = self.WIDTH
        #     self.bg_rect1.move_ip((-speed)+bg_offset,0)
        #     self.floor_rect1.move_ip(-speed + floor_offset,0)
        #     self.bg_rect2.move_ip((-speed)+bg_offset,0)
        #     self.floor_rect2.move_ip(-speed+ floor_offset,0)
           
            
        # if scrollDirection == "left":
        #     if self.bg_rect1.left >= self.WIDTH:
        #         self.bg_rect1.right = 0
        #     if self.bg_rect2.left >= self.WIDTH:
        #         self.bg_rect2.right = 0
        #     if self.floor_rect1.left >= self.WIDTH:
        #         self.floor_rect1.right = 0
        #     if self.floor_rect2.left >= self.WIDTH:
        #         self.floor_rect2.right = 0
        #     self.bg_rect1.move_ip((speed)-bg_offset,0)
        #     self.floor_rect1.move_ip(speed- floor_offset,0)
        #     self.bg_rect2.move_ip((speed)-bg_offset,0)
        #     self.floor_rect2.move_ip(speed- floor_offset,0)
        
            
            
           



    def PLAY_DA_GAME(self):
        self.SCREEN.blit(self.floor_surf1,self.floor_rect1)
        self.SCREEN.blit(self.bg_surf1,self.bg_rect1)
        self.SCREEN.blit(self.floor_surf2,self.floor_rect2)
        self.SCREEN.blit(self.bg_surf2,self.bg_rect2)
        

        self.player.update(self.SCREEN)
        
        
        