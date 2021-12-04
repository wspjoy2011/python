import pygame
import os
import random
import json
block_size = 50
block_corector = 2
class Setting:
    def __init__(self,width = 1200, height=800, image = "image/1.jpg", color = (0,0,0)):
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = color
        if image != None:
            self.IMAGE = pygame.image.load(
                                            os.path.join(
                                                os.path.abspath(__file__ + '/..'), image))
            self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
        self.CAPTION = "Love and Logic"

class Game_Sprite(Setting):
    def __init__(self,x,y,width,height,image,color):
        super().__init__(width,height,image,color)
        self.X = x
        self.Y = y
        self.SURFACE = pygame.Surface((self.WIDTH,self.HEIGHT))
        self.SURFACE.fill(self.COLOR)

class Player_Sprite(Game_Sprite):
    def __init__(self, speed, x, y, width, height, image, color):
        super().__init__(x, y, width, height,image,color)
        self.SPEED = speed
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_LEFT = True
        self.SPEED_GRAVITY = 1
        self.GRAVITY_CAN_WORK = True # проверка работы гравитации True - да
        self.JUMP_COUNT = 0 # Счетчик для прыжка 
        self.SPEED_JUMP = 2 # скорость прыжка
        self.FLYING_UP = False # Проверка полета вверх
    # Движение спрайта
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.X + self.WIDTH <= 1200 and self.CAN_MOVE_RIGHT:
            self.X += self.SPEED
        elif keys[pygame.K_LEFT] and self.X >= 0 and self.CAN_MOVE_LEFT:
            self.X -= self.SPEED
    # Взаимодействие игрока при касании с правой стороной блока 
    def collision_right(self):
        for el in list_block_coordinats:
            if self.X + self.WIDTH > el[0] - block_corector and self.X < el[1] and self.Y < el[3] and self.Y + self.HEIGHT > el[2]:
                self.CAN_MOVE_RIGHT = False
                break
            else:
                self.CAN_MOVE_RIGHT = True
    # Взаимодействие игрока при касании с левой стороной блока 
    def collision_left(self):
        for el in list_block_coordinats:
            if self.X + self.WIDTH > el[0] and self.X < el[1] + block_corector and self.Y < el[3] and self.Y + self.HEIGHT > el[2]:
                self.CAN_MOVE_LEFT = False
                break
            else:
                self.CAN_MOVE_LEFT = True
    #
    def gravity(self):
        print(self.FLYING_UP)
        if self.GRAVITY_CAN_WORK and self.FLYING_UP == False:
            self.Y += self.SPEED_GRAVITY
    # Взаимодействие при падении когда блок ниже спрайта              
    def collision_top(self):
        for el in list_block_coordinats:
            if self.X + self.WIDTH > el[0] + block_corector and self.X < el[1] - block_corector and self.Y + self.HEIGHT >= el[2] - self.SPEED_GRAVITY and self.Y + self.HEIGHT <= el[2]:
                self.GRAVITY_CAN_WORK = False
                self.Y = el[2] - self.HEIGHT
                break
            else:
                self.GRAVITY_CAN_WORK = True
    # Взаимодействие при прижке когда блок выше спрайта 
    def collision_bottom(self):
        for el in list_block_coordinats:
            if self.X + self.WIDTH > el[0] + block_corector and self.X < el[1] - block_corector and self.Y <= el[3] + self.SPEED_JUMP // 2 and self.Y >= el[3]:
                self.JUMP_COUNT = 100
                break
    #
    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.GRAVITY_CAN_WORK != True:
            self.FLYING_UP = True
            self.IN_THE_AIR = True
        if self.JUMP_COUNT < 100 and self.FLYING_UP:
            self.JUMP_COUNT += 1
            self.Y -= self.SPEED_JUMP
        if self.JUMP_COUNT == 100:
            self.JUMP_COUNT = 0
            self.FLYING_UP = False
      
list_blocks =  ['########################',
                '#0000000000000000000000#',
                '#0000000000000000000000#',
                '#0####000#####00###00###',
                '#000000000000#000000000#',
                '#0000##000000#000000000#',
                '#000000000000##00000#00#',
                '#000000000000##00000#00#',
                '##0####000000#000####0##',
                '##0#00#####00#000000000#',
                '#000000000000###0000000#',
                '###000000#0###0000##0###',
                '#0000000##00##0000#0000#',
                '#00000000000##000000000#',
                '#00#00#00000##000000000#',
                '####00##################',
            ]
list_surfaces = []
list_block_coordinats = [] # [0-x_left, 1-x_right, 2-y_top, 3-y_bottom]
def create_blocks():
    y = 0
    for row in list_blocks:
        x = 0
        for col in row:
            if col == '#':
                surface = Game_Sprite(x,y,block_size,block_size,None,(225,0,0))
                list_surfaces.append(surface)
                list_block_coordinats.append([x, x + block_size, y, y + block_size])
                
            x += block_size
            
        y += block_size

def run_game():
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))
    pygame.display.set_caption(setting.CAPTION)

    # platform = Game_Sprite(setting.WIDTH//2,setting.HEIGHT//2,40,40,None,(255,0,0))
    create_blocks()
    print(list_block_coordinats)
    
    game = True
    #
    player = Player_Sprite(block_corector, 100,100, block_size, block_size, None, (0,255,0))
    #
    while game:
        
        screen.fill(setting.COLOR)
        screen.blit(setting.IMAGE, (0,0))
        for sur in list_surfaces:
            screen.blit(sur.SURFACE,(sur.X,sur.Y))
        screen.blit(player.SURFACE,(player.X, player.Y))
        
        player.collision_right()
        player.collision_left()
        player.collision_top()
        player.collision_bottom()
        player.move()
        player.gravity()
        player.jump()

        # screen.blit(platform.SURFACE,(platform.X,platform.Y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            # if event.type == pygame.MOUSEMOTION:
            #     print(event.pos[0], event.pos[1])

        pygame.display.flip()

run_game()


