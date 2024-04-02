import pygame
import random

#initializing pygame
pygame.init()
#display screen

WIDTH,HEIGHT=8000,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

#loading the images

rock_img=pygame.image.load("rock.png")
paper_img=pygame.image.load("paper.png")
scissors_img=pygame.image.load(scissors.png")

#resizing the images
IMAGE_SIZE=150
rock_img=pygame.transform.scale(rock_img,(IMAGE_SIZE,IMAGE_SIZE))
paper_img=pygame.transform.scale(paper_img,(IMAGE_SIZE,IMAGE_SIZE))
scissors_img=pygame.transform.scale(scissors_img,(IMAGE_SIZE,IMAGE_SIZE))

#Colors
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(200,200,200)

#Font
font=pygame.font.Font(None,36)

#Main game loop
running=True
clock=pygame.time.Clock()

user_choice=None
computer_choice=None
result=None
animation_counter=0
user_wins=0
computer_wins=0

#Function to display text with shadow

def draw_text(surface,text,font,color,x,y,shadow=True):
  if shadow:
    shadow_text=font.render(text,True,BLACK)
    surface.blit(shadow_text,(x+2,y+2))
  text_surface=font.render(text,True,color)
  surface.blit(text_surface,(x,y))

#Button click animation
def animate_button(button_rect):
  for i in range(10,0,-1):
      button_color=(i*20,i*20,i*20)
      pygame.draw.rect(screen,button_color, button_rect)
      pygame.display.flip()
      pygame.time.delay(10)
while running:
  screen.fill(WHITE)
  #Display images for the user

  user_buttons=[screen.blit(rock_img,(100,50)),
                screen.blit(paper_img,(300,50)),
                screen.blit(scissors_img,(500,50))
                ]

  #Display images for the computer
  computer_buttons = [
        screen.blit(rock_img, (100, 400)),
        screen.blit(paper_img, (300, 400)),
        screen.blit(scissors_img, (500, 400))
    ]
# Display win counters
    draw_text(screen, f"User Wins: {user_wins}", font, BLACK, 20, 20)
    draw_text(screen, f"Computer Wins: {computer_wins}", font, BLACK, 20, 550)
 # Display result animation
    if result:
        draw_text(screen, result, font, BLACK, WIDTH // 2 - 50, HEIGHT // 2)
 # Increment animation counter
    animation_counter += 1
 # Reset after 3 seconds
    if animation_counter >= 100:
            user_choice = None
            computer_choice = None
            result = None
            animation_counter = 0

# Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not result:
            mouse_pos = pygame.mouse.get_pos()
            
            
            for i, button_rect in enumerate(user_buttons):
                if button_rect.collidepoint(mouse_pos):
                    user_choice = ["rock", "paper", "scissors"][i]
                    animate_button(button_rect)

                    # Computer choice
                    computer_choice = random.choice(["rock", "paper", "scissors"])

                    # Determine winner
                    if user_choice == computer_choice:
                        result = "It's a tie!"
                    elif (user_choice == "rock" and computer_choice == "scissors") or \
                         (user_choice == "paper" and computer_choice == "rock") or \
                         (user_choice == "scissors" and computer_choice == "paper"):
                        result = "You won!"
                        user_wins += 1
                    else:
                        result = "Computer won!"
                        computer_wins += 1
                    animate_button(computer_buttons[["rock","paper","scissors"].index(computer_choice)])

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
