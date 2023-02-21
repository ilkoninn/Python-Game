import pygame
from sys import exit
from random import randint

#GAME FUNCTIONS
def displayScore():
    current_time = int(pygame.time.get_ticks()/1000) - start_time

    #SCORE 
    score_surf = test_font.render('Score: ' + str(current_time), False, (64,64,64))
    default_image_size5 = (200, 50)
    score_surf = pygame.transform.scale(score_surf, default_image_size5)
    score_rect = score_surf.get_rect(topleft = (0, 200))
    screen.blit(score_surf, score_rect)

    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 7
            if obstacle_rect.bottom == 720:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 720:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

def snail_animation():
    global snail_surf, snail_index

    snail_index += 0.1
    if snail_index > len(snail_frames):
        snail_index = 0
    snail_surf = snail_frames[int(snail_index)]

def fly_animation():
    global fly_surf, fly_index

    fly_index += 0.1
    if fly_index > len(fly_frames):
        fly_index = 0
    fly_surf = fly_frames[int(fly_index)]

def displayMaxScore():
    global game_data

    game_data.append(score)

    max_score_surf = test_font.render(f'Max Score: {max(game_data)}', False, (64,64,64))
    default_image_size5 = (280, 50)
    max_score_surf = pygame.transform.scale(max_score_surf, default_image_size5)
    max_score_rect = max_score_surf.get_rect(topleft = (0, 100))
    screen.blit(max_score_surf, max_score_rect)



pygame.init()

screen = pygame.display.set_mode((1280,960))
pygame.display.set_caption('Fuad Müəllim')
clock = pygame.time.Clock()

test_font = pygame.font.Font('Font/prstart.ttf', 50)

game_activate = False
start_time = 0
score = 0

#DISPLAY
sky_surface = pygame.image.load('Graphics/fotos/Sky.png').convert()
default_image_size1 = (1280, 720)
sky_surface = pygame.transform.scale(sky_surface, default_image_size1)

ground_surface = pygame.image.load('Graphics/fotos/ground.png').convert()
default_image_size2 = (1280, 240)
ground_surface = pygame.transform.scale(ground_surface, default_image_size2)

text_surface = test_font.render("FUAD GAME", False, 'Black')

counter = 0

jump_sound = pygame.mixer.Sound('Audio/audio_jump.mp3')
game_sound = pygame.mixer.Sound('Audio/game_sound.mp3')

game_data = []


#OBSTACLES
#SNAILS VARIABLES
snail_frame_1 = pygame.image.load('Graphics/Mobs/snail/snail1.png').convert_alpha()
default_image_size3 = (90, 50)
snail_frame_1 = pygame.transform.scale(snail_frame_1, default_image_size3)

snail_frame_2 = pygame.image.load('Graphics/Mobs/snail/snail2.png').convert_alpha()
default_image_size3 = (90, 50)
snail_frame_2 = pygame.transform.scale(snail_frame_2, default_image_size3)

snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0

snail_surf = snail_frames[snail_index]

#FLIES VARIABLES
fly_frame_1 = pygame.image.load('Graphics/Mobs/fly/Fly1.png').convert_alpha()
default_image_size6 = (90, 50)
fly_frame_1 = pygame.transform.scale(fly_frame_1, default_image_size6)

fly_frame_2 = pygame.image.load('Graphics/Mobs/fly/Fly2.png').convert_alpha()
default_image_size6 = (90, 50)
fly_frame_2 = pygame.transform.scale(fly_frame_2, default_image_size6)

fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0

fly_surf = fly_frames[fly_index]

obstacle_rect_list =  []


#PLAYER VARİABLE
player_walk_1 = pygame.image.load('Graphics/Player/Movements/player_walk_1.png').convert_alpha()
default_image_size4 = (100, 140)
player_walk_1 = pygame.transform.scale(player_walk_1, default_image_size4)
player_rect = player_walk_1.get_rect(midbottom = (160,730))

player_walk_2 = pygame.image.load('Graphics/Player/Movements/player_walk_2.png').convert_alpha()
default_image_size4 = (100, 140)
player_walk_2 = pygame.transform.scale(player_walk_2, default_image_size4)
player_rect = player_walk_2.get_rect(midbottom = (160,720))

player_walk = [player_walk_1, player_walk_2]

player_index = 0

player_jump = pygame.image.load('Graphics/Player/Movements/jump.png').convert_alpha()
default_image_size4 = (100, 140)
player_jump = pygame.transform.scale(player_jump, default_image_size4)
player_rect = player_jump.get_rect(midbottom = (160,720))

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (160,720))


player_gravity = 0

#INTRO SCREEN
player_stand = pygame.image.load('Graphics/Player/Movements/player_stand.png').convert_alpha()
player_stand_scaled = pygame.transform.scale(player_stand, (320, 400))
player_stand_rect = player_stand_scaled.get_rect(center = (640,480))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (640, 200))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (640, 780))

#TIMER
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)

while True:
    #GAME MAIN CODES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_activate:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 720: 
                    player_gravity = -25
                    jump_sound.play()

            if event.type == pygame.KEYDOWN and player_rect.bottom >= 720:
                if event.key == pygame.K_SPACE:
                    player_gravity = -25
                    jump_sound.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_activate = True
                start_time = int(pygame.time.get_ticks()/1000)
        
        if event.type == obstacle_timer and game_activate:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(1300, 1400), 720)))      
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(1300, 1400), 520)))      
    
    #DISPLAY
    if game_activate:

        counter += 1

        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,720))
        screen.blit(text_surface, (360, 0))
        score = displayScore()
        max_score = displayMaxScore()

        #PLAYER    
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 730:
            player_rect.bottom = 730 
        screen.blit(player_surf, player_rect)

        #PLAYER ANIMATION
        player_animation()
        snail_animation()
        fly_animation()

        #OBSTACLE MOVEMENT
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #COLLISION
        game_activate = collisions(player_rect, obstacle_rect_list)

    else:
        #START SECTION
        screen.fill((94, 129, 162))
        screen.blit(player_stand_scaled, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (130, 720)
        player_gravity = 0
        game_sound.play()

        #LOSE SECTION
        if counter > 1:
            info_message = test_font.render('Press space to continue', False, (111, 196, 169))
            info_message_rect = info_message.get_rect(center = (640, 880))
            screen.blit(info_message, info_message_rect)
        
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (640, 780))
        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
        
       
    
    pygame.display.update()
    clock.tick(60)
