import pygame
import random
import numpy as np

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

# to initialize pygame
pygame.init()

# to display screen window
screen = pygame.display.set_mode((1280, 720))

# to change title and icon
pygame.display.set_caption("Brick Breaker")
icon = pygame.image.load('brick.png').convert_alpha()
pygame.display.set_icon(icon)

def get_font(size): 
    return pygame.font.Font("font.ttf", size)

def options():
    ballImg = pygame.image.load('ball.png')
    running = True 
    while running:
        mouse_pos = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))

        options_text = get_font(60).render("CHOOSE A BALL", True, (255, 255, 255))
        options_rect = options_text.get_rect(center=(640, 100))
        screen.blit(options_text, options_rect)

        option1_button = Button(image=pygame.image.load("option1.png"), pos=(400,300), 
                            text_input="", font=get_font(50), base_color=(255, 255, 255), hovering_color=None)
        option1_button.update(screen)
        option2_button = Button(image=pygame.image.load("option2.png"), pos=(650, 300), 
                            text_input="", font=get_font(50), base_color=(255, 255, 255), hovering_color=None)
        option2_button.update(screen)
        option3_button = Button(image=pygame.image.load("option3.png"), pos=(900, 300), 
                            text_input="", font=get_font(50), base_color=(255, 255, 255), hovering_color=None)
        option3_button.update(screen)
        option4_button = Button(image=pygame.image.load("option4.png"), pos=(525, 500), 
                            text_input="", font=get_font(50), base_color=(255, 255, 255), hovering_color=None)
        option4_button.update(screen)
        option5_button = Button(image=pygame.image.load("option5.png"), pos=(775, 500), 
                            text_input="", font=get_font(50), base_color=(255, 255, 255), hovering_color=None)
        option5_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option1_button.checkForInput(mouse_pos):
                   ballImg = pygame.image.load('ball1.png')
                   play(ballImg)
                   main_menu()
                elif option2_button.checkForInput(mouse_pos):
                   ballImg = pygame.image.load('ball2.png')
                   play(ballImg)
                   main_menu()
                elif option3_button.checkForInput(mouse_pos):
                   ballImg = pygame.image.load('ball3.png')
                   play(ballImg)
                   main_menu()
                elif option4_button.checkForInput(mouse_pos):
                   ballImg = pygame.image.load('ball4.png')
                   play(ballImg)
                   main_menu()
                elif option5_button.checkForInput(mouse_pos):
                   ballImg = pygame.image.load('ball5.png')
                   play(ballImg)
                   main_menu()
            
        pygame.display.update()
def play(img):
    # positioning the paddle and ball on screen
    playerImg = pygame.image.load('bar.png')
    playerX = 600
    playerY = 600
    playerX_change = 0

    ball_velocity = [0.8, 0.8]
    ballImg = img
    ballX = 550
    ballY = 550

    running = True

    # function for drawing the paddle and ball at new coordinates
    def draw(x, y):
        screen.blit(playerImg, (x, y))
        screen.blit(ballImg, (ballX, ballY))
    
    brick_map = [
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ,5],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
    
    score=[0]
    # function for creating the bricks
    def bricks(box):
        brick_colour = {
            3: (118, 252, 255),
            4: (3, 182, 255),
            5: (0, 51, 145),
            6: (7, 2, 114)
        }

        gap = 2
        brick_height = (550 / 8) - 2
        brick_width = (1280 / 16) - 2

        for row_index, row in enumerate(brick_map):
            for col_index, col in enumerate(row):
                if col != 0:
                    y = row_index * (brick_height + gap) + gap // 2
                    x = col_index * (brick_width + gap) + gap // 2
                    b = pygame.Rect(x, y, brick_width, brick_height)
                    pygame.draw.rect(screen, brick_colour[col], b)
                    if box.colliderect(b):
                        brick_map[row_index][col_index] = 0
                        pygame.draw.rect(screen, (0, 0, 0), b)
                        score[0] += 5
                        ball_velocity[1] *= -1


    # to close window when exit button is pressed
    while running:
        # screen colour, fill(Red, green, blue)
        screen.fill((0, 0, 0))
        # to close window when exit button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -1.5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 1.5
            if event.type == pygame.KEYUP:
                playerX_change = 0
        if playerX <= 0:
            playerX = 0
            playerX_change = 1.5
        if playerX >= 1150:
            playerX = 1150
            playerX_change = -1.5
        pBox = pygame.Rect(playerX - 5, playerY + 55, 140, 25)
        pygame.draw.rect(screen, (0, 0, 0), pBox, 1)
        bBox = pygame.Rect(ballX, ballY , 25, 25)
        pygame.draw.rect(screen, (0, 0, 0), bBox, 1)
        if ballX < 0 or ballX > 1248:
            ball_velocity[0] *= -1
        if ballY < 0:
            ball_velocity[1] = random.choice([-1,1])
        if ballY > 688:
            font1 = get_font(74)
            text1 = font1.render("GAME OVER", 1, (255, 255, 255))
            screen.blit(text1, (300,350))
            font2= pygame.font.Font(None, 50)
            text2 = font2.render("Score: ", 1, (255, 255, 255))
            screen.blit(text2, (470,430))
            score_text = font2.render(str(score[0]), 1, (255, 255, 255))
            screen.blit(score_text, (600,430))
            pygame.time.wait(2000)
        if bBox.colliderect(pBox):
            ball_velocity[1] *= -1
            #ball_velocity[0] = random.randint(-8,8)
        check = np.count_nonzero(brick_map)
        if check==0:
            font = get_font(74)
            text1 = font.render("You Won", 1, (255, 255, 255))
            screen.blit(text1, (400,300))
            pygame.time.wait(3000)
        bricks(bBox)
        ballX += ball_velocity[0]
        ballY += ball_velocity[1]
        playerX += playerX_change
        draw(playerX, playerY)
        pygame.display.update()


def main_menu():
    while True:
        bg = pygame.image.load('Background.png')
        screen.blit(bg, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(90).render("BRICK BREAKER", True, (182, 143, 64))
        menubox = menu_text.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color=(215, 252, 212), hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color=(215, 252, 212), hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color=(215, 252, 212), hovering_color="White")

        screen.blit(menu_text, menubox)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)
        ballImg = pygame.image.load('ball.png')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    play(ballImg)
                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    options()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()

main_menu()
