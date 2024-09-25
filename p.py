import sys
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1000, 600))

pygame.display.set_caption('Game')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

player = pygame.Surface((40, 40))
player.fill(blue)

x, y = 50, 560

clock = pygame.time.Clock()

gravity = 1.1
jump_strength = 13
y_velocity = 0
is_jumping = False

player_movement = False

y_list = [round(x, 1) for x in [i * 0.1 for i in range(0, 5401)]]

circle_enemy_spawn_delay = 1500
square_enemy_spawn_delay = 1500

last_circle_spawn_time = 0
last_square_spawn_time = 0

pass_key = True

enemy_square_list = []
enemy_circle_list = []

spawn_circles = False


class Square:
    def __init__(self):
        self.x = 1000
        self.y = random.choice(y_list)
        self.length = 50
        self.width = 50
        self.speed = 8
        self.colour = green
        self.surf = pygame.Surface((self.length, self.width))
        self.surf.fill(self.colour)
        self.angle = 0

    def move(self):
        self.x -= self.speed

    def draw(self):
        self.angle += 2
        # Rotate the surface and get a new rotated surface
        new_surf = pygame.transform.rotate(self.surf, self.angle)

        # Get the new rect for the rotated surface and center it at the original position
        new_rect = new_surf.get_rect(center=(self.x + self.length // 2, self.y + self.width // 2))

        # Draw the rotated surface at the updated position
        screen.blit(new_surf, new_rect.topleft)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.length, self.width)


class Circle:
    def __init__(self):
        self.x = 1000
        self.y = random.choice(y_list)
        self.radius = 28
        self.speed = 8
        self.colour = red

    def move(self):
        self.x -= self.speed

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x + 28, self.y + 28), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x + 2.5, self.y + 2.5, 47, 47)


while True:
    time_passed = pygame.time.get_ticks()

    screen.fill(black)

    player_rect = player.get_rect(topleft=(x, y))

    if time_passed >= 750 and pass_key:
        spawn_circles = True
        pass_key = False

    # Spawn circles at regular intervals
    if time_passed - last_circle_spawn_time >= circle_enemy_spawn_delay + 750:
        enemy_circle_list.append(Circle())
        last_circle_spawn_time = time_passed

    # Spawn squares at regular intervals
    if time_passed - last_square_spawn_time >= square_enemy_spawn_delay:
        enemy_square_list.append(Square())
        last_square_spawn_time = time_passed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_movement = True
                y_velocity = -jump_strength
                is_jumping = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_jumping = False

    y_velocity += gravity
    y += y_velocity

    for square in enemy_square_list:
        square.move()
        square.draw()
        if square.x < -60:
            enemy_square_list.remove(square)
        if square.get_rect().colliderect(player_rect):
            enemy_square_list.remove(square)
            pygame.quit()
            sys.exit()

    for circle in enemy_circle_list:
        circle.move()
        circle.draw()
        if circle.x < -60:
            enemy_circle_list.remove(circle)
        if circle.get_rect().colliderect(player_rect):
            enemy_circle_list.remove(circle)
            pygame.quit()
            sys.exit()

    if y >= 560 and not player_movement:
        y = 560
        y_velocity = 0

    if y >= 640 or y < -50:
        print('You died!')
        pygame.quit()
        sys.exit()

    screen.blit(player, player_rect)

    pygame.display.flip()
    clock.tick(60)