import pygame
import random

pygame.init()

# 게임 화면 크기
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("벽돌깨기")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, radius, color):
        super().__init__()
        self.pos = pos
        self.radius = radius
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=tuple(pos))
        self.speed = [0, 0]
        self.acceleration = [0, 0]
    
    def update(self):
        self.rect.move_ip(self.speed)

        '''
        # 화면 경계 처리
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
        if self.rect.bottom > screen_height:
            self.kill()  # 공이 화면 밖으로 나가면 제거됨'''

clock = pygame.time.Clock()
sprites = pygame.sprite.Group()

ball_size = 3

text = f"공 개수: {len(sprites.sprites())}        현재 공 크기: {ball_size}"
font = pygame.font.Font("./ddag.ttf", 36)
text_surface = font.render(text, True, WHITE)
text_rect = text_surface.get_rect()
text_rect.topright = (screen_width - 175, 10)

special_mode = False
game_end = False
while game_end == False:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sprites.empty()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            ball_size += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            if ball_size != 1: ball_size -= 1
        elif pygame.mouse.get_pressed()[0] == True:
            nb = Ball(pygame.mouse.get_pos(), ball_size, WHITE)
            sprites.add(nb)
        elif pygame.mouse.get_pressed()[2] == True:
            for sprite in sprites:
                if ((sprite.pos[0] - pygame.mouse.get_pos()[0])**2 + (sprite.pos[1] - pygame.mouse.get_pos()[1])**2)**1/2 <= (ball_size**2)/2:
                    sprite.kill()
        elif pygame.mouse.get_pressed()[1] == True:
            if special_mode == False:
                special_mode = True
            elif special_mode == True:
                special_mode = False
    text = f"공 개수: {len(sprites.sprites())}        현재 공 크기: {ball_size}"
    text_surface = font.render(text, True, WHITE)

    for ball in sprites:
        ball.update()
    if special_mode:
        bg_random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        text_random_color = (255 - bg_random_color[0], 255 - bg_random_color[1], 255 - bg_random_color[2])
        SPECIAL = ["S", "P", "E", "C", "I", "A", "L"]; random.shuffle(SPECIAL)
        text = ''.join(SPECIAL)
        text_surface = font.render(text, True, text_random_color)
        screen.fill(bg_random_color)
        # 게임 프레임 설정
        clock.tick(5)
    else:
        text = f"공 개수: {len(sprites.sprites())}        현재 공 크기: {ball_size}"
        text_surface = font.render(text, True, WHITE)
        screen.fill(BLACK)
        # 게임 프레임 설정
        clock.tick(-2048)

    screen.blit(text_surface, text_rect)
    sprites.draw(screen)
    pygame.display.update()

pygame.quit()