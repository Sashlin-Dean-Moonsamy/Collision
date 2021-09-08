#import modules
import pygame
import random
from pygame.constants import KEYDOWN


#initialize pygame
pygame.init()



#set game window
screen_width  = 1040
screen_height = 680
screen        = pygame.display.set_mode((screen_width, screen_height))



#define background variable
background = pygame.image.load('images/background.jpg')



#set caption and icon
pygame.display.set_caption("Collision")
icon = pygame.image.load('images/astronaut.png')
pygame.display.set_icon(icon)



#Player
player            = pygame.image.load('images/car.png')
player_width      = 64
player_height     = 64
player_x_position = 450
player_y_position = 500



#prize
prize            = pygame.image.load('images/success.png')
prize_width      = 256
prize_height     = 256
prize_X_Position = 400
prize_Y_Position = 0  - prize_height



#ememies
enemy_width  = 256
enemy_height = 256                                                                                         

#enemy1
enemy1            = pygame.image.load('images/enemy1.png')
enemy1_X_Position =  random.randint(0, screen_width - enemy_width)
enemy1_Y_Position = 0 - enemy_height

#enemy2
enemy2            = pygame.image.load('images/enemy2.png')
enemy2_X_Position =  random.randint(0, screen_width - enemy_width)
enemy2_Y_Position = 0 - enemy_height

#enemy3
enemy3            = pygame.image.load('images/enemy3.png')
enemy3_X_Position =  random.randint(0, screen_width - enemy_width)
enemy3_Y_Position = 0 - enemy_height



#velocity
vel       = 1
enemy_vel = 0.5
prize_vel = 0.1



#Main Game Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    #check is any keys are pressed
    keys = pygame.key.get_pressed()

    #if left key is pressed x increment -ive
    if keys[pygame.K_LEFT]:
        player_x_position -= vel

    #if right key is pressed x incriment +ive
    elif keys[pygame.K_RIGHT]:
        player_x_position += vel

    #if up key is pressed y incriment -ive
    elif keys[pygame.K_UP]:
        player_y_position -= vel

    #if down key is pressed
    elif keys[pygame.K_DOWN]:
        player_y_position += vel
                
            
            
    #set boundries

    #player_x_position

    #left
    if player_x_position <= 0:
        player_x_position = 0
    #right
    elif player_x_position >= screen_width - player_width:
        player_x_position   = screen_width - player_width


    #player_y_position

    #top
    if player_y_position <=0:
        player_y_position = 0
    #bottom
    elif player_y_position >= screen_height - player_height:
        player_y_position   = screen_height - player_height



    #set fill screen to create moving even when object is incrimented
    screen.fill((0, 0, 0))


    
    #set background
    screen.blit(background, (0, 0))



    #draw player
    screen.blit(player, (player_x_position, player_y_position, player_width, player_height))


    #Bounding box for the player:
    player_box = pygame.Rect(player.get_rect())

    #update box position to player position
    player_box.top  = player_y_position    - 10
    player_box.left = player_x_position    - 10



    #display enemies and map movements

    #enemy1
    screen.blit(enemy1, (enemy1_X_Position, enemy1_Y_Position, enemy_width, enemy_height))
    enemy1_Y_Position += enemy_vel

    #Bounding box for enemy1:
    enemy1_box        = pygame.Rect(enemy1.get_rect())

    #update box position to enemy1 position
    enemy1_box.top    = enemy1_Y_Position  - 30
    enemy1_box.left   = enemy1_X_Position  - 30
    
    
    #enemy2
    if enemy1_Y_Position >= screen_height:
       screen.blit(enemy2, (enemy2_X_Position, enemy2_Y_Position, enemy_width, enemy_height))
       enemy2_Y_Position += enemy_vel

    #Bounding box for enemy2
    enemy2_box      = pygame.Rect(enemy2.get_rect())

    #update box position to enemy2 positionn
    enemy2_box.top  = enemy2_Y_Position  - 30
    enemy2_box.left = enemy2_X_Position  - 30
    


    #enemy3
    if enemy2_Y_Position >= screen_height:
        screen.blit(enemy3, (enemy3_X_Position, enemy3_Y_Position, enemy_width, enemy_height))
        enemy3_Y_Position += enemy_vel

    #Bounding box for enemy3
    enemy3_box      = pygame.Rect(enemy3.get_rect())

    #update box position to enemy3 positionn
    enemy3_box.top  = enemy3_Y_Position  - 30
    enemy3_box.left = enemy3_X_Position  - 30



    #prize

    #display prize if 3rd enemy has left window and map movements
    if enemy3_Y_Position >= screen_height:
        screen.blit(prize, (prize_X_Position, prize_Y_Position, prize_width, prize_height))
        prize_Y_Position += prize_vel
    
    #if prize leaves window make it appear again
    if prize_Y_Position  >= screen_height:
        prize_Y_Position  = 0 - prize_height
        prize_Y_Position += prize_vel
    
    #bounding box for prize
    prize_box  = pygame.Rect(prize.get_rect())

    #update box position to prize position
    prize_box.top     = prize_Y_Position  - 30
    prize_box.left    = prize_X_Position  - 30



    # Test collision of the boxes:
    if player_box.colliderect(enemy1_box) or player_box.colliderect(enemy2_box) or player_box.colliderect(enemy3_box):
    
        # Display losing status to the user: 
        print("You lose!")
       
        #quite game and exit window: 
        pygame.quit()
        exit(0)

    if player_box.colliderect(prize_box):
        
        #display wining status to the user: 
        print("You win!")
        
        #quite game and exit window: 
        pygame.quit()
        
        exit(0)
    

    #update screen
    pygame.display.update()


# ================The game loop logic ends here. =============