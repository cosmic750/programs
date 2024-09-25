import pygame
import sys
import random

pygame.init()

screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('RPS')

white = (255, 255, 255)
black = (0, 0, 0)
light_grey = (150, 150, 150)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

font = pygame.font.SysFont('Trebuchet MS', 30)
font1 = pygame.font.SysFont('Trebuchet MS', 45)

# Score counters
wins_count = 0
draws_count = 0
losses_count = 0

text = font.render('Rock', True, black)
text1 = font.render('Paper', True, black)
text2 = font.render('Scissors', True, black)

surface = pygame.Surface((120, 60))
surface1 = pygame.Surface((120, 60))
surface2 = pygame.Surface((120, 60))

surface.fill(red)
surface1.fill(blue)
surface2.fill(green)

surface_rect = surface.get_rect(midbottom=(60 + surface.get_width() / 2, screen_height - 40))
surface_rect1 = surface1.get_rect(midbottom=(surface_rect[0] * 4 + 60, screen_height - 40))
surface_rect2 = surface2.get_rect(midbottom=(surface_rect[0] * 6 + 120, screen_height - 40))

text_rect = text.get_rect(center=surface_rect.center)
text_rect1 = text1.get_rect(center=surface_rect1.center)
text_rect2 = text2.get_rect(center=surface_rect2.center)

transparency = 255
transparency1 = 255
transparency2 = 255

win_text = font1.render('You won!', True, black)
draw_text = font1.render('You drew!', True, black)
loss_text = font1.render('You lost!', True, black)

win_rect = win_text.get_rect(center=(300, 300))
draw_rect = draw_text.get_rect(center=(300, 300))
loss_rect = loss_text.get_rect(center=(300, 300))

ai_list = ['r', 'p', 's']

ai_choice = None

ai_chose_text = font1.render('The AI chose:', True, black)
ai_chose_rect = ai_chose_text.get_rect(center=(300, 70))

rock = font1.render('Rock', True, black)
paper = font1.render('Paper', True, black)
scissors = font1.render('Scissors', True, black)

rock_rect = rock.get_rect(center=(300, 130))
paper_rect = paper.get_rect(center=(300, 130))
scissors_rect = scissors.get_rect(center=(300, 130))

win = False
draw = False
loss = False

clock = pygame.time.Clock()

player_made_choice = False

while True:
    screen.fill(light_grey)

    screen.blit(ai_chose_text, ai_chose_rect)

    if ai_choice == 'r':
        screen.blit(rock, rock_rect)
    elif ai_choice == 'p':
        screen.blit(paper, paper_rect)
    elif ai_choice == 's':
        screen.blit(scissors, scissors_rect)

    if win:
        screen.blit(win_text, win_rect)
    if draw:
        screen.blit(draw_text, draw_rect)
    if loss:
        screen.blit(loss_text, loss_rect)

    mp = pygame.mouse.get_pos()

    surface.set_alpha(transparency)
    surface1.set_alpha(transparency1)
    surface2.set_alpha(transparency2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if surface_rect.collidepoint(mp) or surface_rect1.collidepoint(mp) or surface_rect2.collidepoint(mp):
                ai_choice = random.choice(ai_list)
                player_made_choice = True

                win = False
                draw = False
                loss = False

                if surface_rect.collidepoint(mp):
                    if ai_choice == 'r':
                        draw = True
                        draws_count += 1
                    elif ai_choice == 'p':
                        loss = True
                        losses_count += 1
                    elif ai_choice == 's':
                        win = True
                        wins_count += 1

                if surface_rect1.collidepoint(mp):
                    if ai_choice == 'r':
                        win = True
                        wins_count += 1
                    elif ai_choice == 'p':
                        draw = True
                        draws_count += 1
                    elif ai_choice == 's':
                        loss = True
                        losses_count += 1

                if surface_rect2.collidepoint(mp):
                    if ai_choice == 'r':
                        loss = True
                        losses_count += 1
                    elif ai_choice == 'p':
                        win = True
                        wins_count += 1
                    elif ai_choice == 's':
                        draw = True
                        draws_count += 1

    if surface_rect.collidepoint(mp):
        transparency = 128
    else:
        transparency = 255

    if surface_rect1.collidepoint(mp):
        transparency1 = 128
    else:
        transparency1 = 255

    if surface_rect2.collidepoint(mp):
        transparency2 = 128
    else:
        transparency2 = 255

    wins_display = font.render(f"Wins: {wins_count}", True, black)
    draws_display = font.render(f"Draws: {draws_count}", True, black)
    losses_display = font.render(f"Losses: {losses_count}", True, black)

    wins_rect = wins_display.get_rect(midleft=(10, screen_height // 2 - 50))
    draws_rect = draws_display.get_rect(midleft=(10, screen_height // 2 - 10))
    losses_rect = losses_display.get_rect(midleft=(10, screen_height // 2 + 30))

    screen.blit(wins_display, wins_rect)
    screen.blit(draws_display, draws_rect)
    screen.blit(losses_display, losses_rect)

    screen.blit(surface, surface_rect)
    screen.blit(surface1, surface_rect1)
    screen.blit(surface2, surface_rect2)

    screen.blit(text, text_rect)
    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)

    pygame.display.flip()
    clock.tick(60)
