import json
import pygame
import math
from .bullet import Bullet


from .carcase import Carcase,rect_addiction
class Player(Carcase):
    def __init__(self, screen, sprite_sheet, num_frames = 10, group = None):
        super().__init__("player/images/WallHang.png")
        self.frames = self.load_frames(pygame.image.load(sprite_sheet), num_frames)
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.screen = screen
        self.last_update = pygame.time.get_ticks()
        self.group = group
        with open("player/properties.json") as info:
            properties = json.load(info)
            self.hp = properties["hp"]
            self.speed = properties["speed"]
            self.name = properties["name"]
            self.speed = properties["speed"][0]
    def update(self):
        mouse = pygame.mouse.get_pos()
        angle = math.atan2(mouse[1] - self.rect.center[1], mouse[0] - self.rect.center[0])
        print(angle)
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.group.add(Bullet(self.rect.center[0], self.rect.center[1], self.speed*0.5, angle))
        keys = pygame.key.get_pressed()
        x, y= 0, 0
        action = False
        if keys[pygame.K_a]:
            x = -1
            action = True
        if keys[pygame.K_d]:
            x = 1
            action = True
        if keys[pygame.K_w]:
            y  = -1
            action = True
        if keys[pygame.K_s]:
            y = 1
            action = True
        if action:
            angle1 = math.atan2(y, x)
            m = self.rect.center
            self.rect.center = (m[0] + self.speed * math.cos(angle1),m[1]+self.speed * math.sin(angle1))
            action = False

    def load_frames(self, sprite_sheet, num_frames):
        frames = []
        SPRITE_HEIGHT = sprite_sheet.get_height()
        SPRITE_WIDTH = sprite_sheet.get_width()/num_frames
        for i in range(num_frames):
            frame = sprite_sheet.subsurface(pygame.Rect(i * SPRITE_WIDTH, 0, SPRITE_WIDTH, SPRITE_HEIGHT))
            frames.append(frame)
        return frames
