import pygame
import sys

pygame.init()

width = 1920
height = 1080
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tron Game")
clock = pygame.time.Clock()

background = (82, 45, 7)
white = (236, 240, 241)
green = (0,128,0)
darkGreen = (0,100,0)
red = (231, 76, 60)
darkRed = (241, 148, 138)
darkBlue = (40, 116, 166)

font = pygame.font.SysFont(None, 80)

w = 10


def startScreen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return True

        display.fill(background)
        # Größere Schrift für "TRON GAME"
        title_font = pygame.font.Font(None, 200)
        title_text = title_font.render("TRON GAME", True, white)
        title_rect = title_text.get_rect(center=(width/2, height/2 - 300))
        display.blit(title_text, title_rect)

        # Kleinerer Text für "Spiel Starten" mit Rahmen
        button_font = pygame.font.Font(None, 60)
        button_text = button_font.render("Spiel Starten", True, white)
        button_rect = button_text.get_rect(center=(width/2, height/2 + 100))

        # Rahmen zeichnen
        pygame.draw.rect(display, white, button_rect, 2)  # Dritte Parameter ist die Dicke des Rahmens

        # Text auf den Rahmen zeichnen
        display.blit(button_text, button_rect)

        # Text für den Namen
        name_font = pygame.font.Font(None, 40)
        name_text = name_font.render("Samuel Pucher | Claudius Berner", True, white)  # Ändern Sie "Ihr Name" entsprechend
        name_rect = name_text.get_rect(center=(width/2, height/2 + -200))  # Anpassen der Position nach Bedarf
        display.blit(name_text, name_rect)

        pygame.display.update()
        clock.tick(60)



def close():
    pygame.quit()
    sys.exit()

startScreen()

# Tron Bike Class
class tronBike:
    def __init__(self, number, color, darkColor, side):
        self.w = w
        self.h = w
        self.x = abs(side - 100)
        self.y = height/2 - self.h
        self.speed = 10
        self.color = color
        self.darkColor = darkColor
        self.history = [[self.x, self.y]]
        self.number = number
        self.length = 1

    # Draw / Show the Bike
    def draw(self):
        for i in range(len(self.history)):
            if i == self.length - 1:
                pygame.draw.rect(display, self.darkColor, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:    
                pygame.draw.rect(display, self.color, (self.history[i][0], self.history[i][1], self.w, self.h))

    # Move the Bike
    def move(self, xdir, ydir):
        self.x += xdir*self.speed
        self.y += ydir*self.speed
        self.history.append([self.x, self.y])
        self.length += 1
        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            gameOver(self.number)

    # Check if Bike Collides with Route
    def checkIfHit(self, opponent):
        if abs(opponent.history[opponent.length - 1][0] - self.history[self.length - 1][0]) < self.w and abs(opponent.history[opponent.length - 1][1] - self.history[self.length - 1][1]) < self.h:
            gameOver(0)
        for i in range(opponent.length):
            if abs(opponent.history[i][0] - self.history[self.length - 1][0]) < self.w and abs(opponent.history[i][1] - self.history[self.length - 1][1]) < self.h:
                gameOver(self.number)

        for i in range(len(self.history) - 1):
            if abs(self.history[i][0] - self.x) < self.w and abs(self.history[i][1] - self.y) < self.h and self.length > 2:
                gameOver(self.number)

def gameOver(number):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Neustart des Spiels bei Drücken der Leertaste
                    return True
                if event.key == pygame.K_ESCAPE:
                    close()

        display.fill(background)
        if number == 0:
            text = font.render("Spieler zusammenstoß", True, white)
        else:
            text = font.render("Spieler %d hat verloren!" % number, True, white)

        text_rect = text.get_rect(center=(width/2, height/2 - 50))
        display.blit(text, text_rect)

        if number != 0:
            prompt_font = pygame.font.Font(None, 40)
            prompt_text = prompt_font.render("Drücke Leertaste, um das Spiel neu zu starten oder ESCAPE, um zu verlassen", True, white)
            prompt_rect = prompt_text.get_rect(center=(width/2, height/2 + 100))
            display.blit(prompt_text, prompt_rect)

        pygame.display.update()
        clock.tick(60)


def drawGrid():
    squares = 50
    for i in range(int(width/squares)):
        pygame.draw.line(display, darkBlue, (i*squares, 0), (i*squares, height))
        pygame.draw.line(display, darkBlue, (0, i*squares), (width, i*squares))

def close():
    pygame.quit()
    sys.exit()


def tron():
    loop = True

    bike1 = tronBike(1, red, darkRed, 0)
    bike2 = tronBike(2, green, darkGreen, width)

    x1 = 1
    y1 = 0
    x2 = -1
    y2 = 0
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_UP:
                    if not (x2 == 0 and y2 == 1):
                        x2 = 0
                        y2 = -1
                if event.key == pygame.K_DOWN:
                    if not (x2 == 0 and y2 == -1):
                        x2 = 0
                        y2 = 1
                if event.key == pygame.K_LEFT:
                    if not (x2 == 1 and y2 == 0):
                        x2 = -1
                        y2 = 0
                if event.key == pygame.K_RIGHT:
                    if not (x2 == -1 and y2 == 0):
                        x2 = 1
                        y2 = 0
                if event.key == pygame.K_w:
                    if not (x1 == 0 and y1 == 1):
                        x1 = 0
                        y1 = -1
                if event.key == pygame.K_s:
                    if not (x1 == 0 and y1 == -1):
                        x1 = 0
                        y1 = 1
                if event.key == pygame.K_a:
                    if not (x1 == 1 and y1 == 0):
                        x1 = -1
                        y1 = 0
                if event.key == pygame.K_d:
                    if not (x1 == -1 and y1 == 0):
                        x1 = 1
                        y1 = 0
                if event.key == pygame.K_SPACE:  # Neustart des Spiels bei Drücken der Leertaste
                    return True

        display.fill(background)
        #drawGrid()
        bike1.draw()
        bike2.draw()

        bike1.move(x1, y1)
        bike2.move(x2, y2)

        bike1.checkIfHit(bike2)
        bike2.checkIfHit(bike1)
        
        pygame.display.update()
        clock.tick(10)




tron()
