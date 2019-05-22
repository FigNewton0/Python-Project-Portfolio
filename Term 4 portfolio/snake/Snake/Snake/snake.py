import pygame
import pygame as pg
from superwires import games
import sys
import copy
import random
import time
from os import path
#code from https://github.com/jatinmandav/Gaming-in-Python/blob/master/Snake_2d/snake.pyLinks to an external site.


pygame.init()

width = 500
WIDTH = 500
HEIGHT = 500
height = 500
scale = 10
score = 0
FPS=60

food_x = 10
food_y = 10

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cameron's Snake Game But With Different Sound Effects")
clock = pygame.time.Clock()

background = (0, 0, 0)
snake_colour = (250, 250, 250)
food_colour = (250, 105, 180)
snake_head = (0, 250, 0)
Black=(250,250,250)



class Snake():
    eat_sound = games.load_sound("snd/nomnom.wav")
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = 10
        self.h = 10
        self.length = 1
        self.x_dir = self.length
        self.y_dir = 0
        self.history = [[self.x, self.y]]

        

    def reset(self):
        self.x = width/2-scale
        self.y = height/2-scale
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1
        

    def show(self):
        for i in range(self.length):
            if not i == 0:
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True

    def grow(self):

        Snake.eat_sound.play()
        self.length += 1
        self.history.append(self.history[self.length-2])

    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i-1])
            i -= 1
        self.history[0][0] += self.x_dir*scale
        self.history[0][1] += self.y_dir*scale
        
class Game:
    global score
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Snake")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font("New Times Roman")
        self.load_data()
        
    def load_data(self):       
        # load high score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, "highscore.txt"), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        self.snd_dir = path.join(self.dir, 'snd')

                
    def show_start_screen(self):
        # game splash/start screen
        pg.mixer.music.load(path.join(self.snd_dir, '8-bit Desert Tune.ogg'))
        pg.mixer.music.set_volume(0.2)
        pg.mixer.music.play(loops=-1)
        self.screen.fill(background)
        self.draw_text("Snake", 48, Black, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Use the arrows to move", 22, Black, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play", 22, Black, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("High Score: " + str(self.highscore), 22, Black, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()


    def show_go_screen(self):
        # game over/continue
        self.screen.fill(background)
        self.draw_text("GAME OVER", 48, Black, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(score), 22, Black, WIDTH / 2, HEIGHT / 2)
##        self.draw_text("Press a key to play again", 22, Black, WIDTH / 2, HEIGHT * 3 / 4)
        if score > self.highscore:
            self.highscore = score
            self.draw_text("NEW HIGH SCORE!", 22, Black, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, "highscore.txt"), 'w') as f:
                f.write(str(score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, Black, WIDTH / 2, HEIGHT / 2 + 40)
            pg.display.flip()
##        self.wait_for_key()
        
        

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


                



class Food:
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, width/scale-1)*scale
        food_y = random.randrange(1, height/scale-1)*scale

    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))


def show_score():
    font = pygame.font.SysFont("New Times Roman", 20)
    text = font.render("Score: " + str(score), True, snake_colour)
    display.blit(text, (scale, scale))





def gameLoop():
    g = Game()
    g.show_start_screen()
    

    loop = True

    global score

    snake = Snake(width/2, height/2)
    food = Food()
    food.new_location()

    while loop:
        speed = 1
        if snake.length > 5:
            speed = 1.05
        if snake.length > 10:
            speed = 1.15
        if snake.length > 15:
            speed = 1.10
        if snake.length > 20:
            speed = 1.15
        if snake.length > 25:
            speed = 1.20
        if snake.length > 30:
            speed = 1.25
        if snake.length > 35:
            speed = 1.30
        if snake.length > 40:
            speed = 1.35
        if snake.length > 45:
            speed = 1.40
        if snake.length > 50:
            speed = 1.45
        if snake.length > 55:
            speed = 1.50
        if snake.length > 60:
            speed = 1.55
        if snake.length > 65:
            speed = 1.60
        if snake.length > 70:
            speed = 1.65
        if snake.length > 75:
            speed = 1.70
        if snake.length > 80:
            speed = 1.75
        if snake.length > 85:
            speed = 1.80
        if snake.length > 90:
            speed = 1.85
        if snake.length > 95:
            speed = 1.90
        if snake.length > 100:
            speed = 1.95
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if snake.y_dir == 0:
                    if event.key == pygame.K_UP:
                        snake.x_dir = 0
                        snake.y_dir = speed*-1
                    if event.key == pygame.K_DOWN:
                        snake.x_dir = 0
                        snake.y_dir = speed

                if snake.x_dir == 0:
                    if event.key == pygame.K_LEFT:
                        snake.x_dir = speed*-1
                        snake.y_dir = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_dir = speed
                        snake.y_dir = 0

        display.fill(background)

        snake.show()
        snake.update()
        food.show()
        show_score()

        if snake.check_eaten():
            food.new_location()
            score += 1
            snake.grow()

        if snake.death():
            score = score
            #pygame.display.update()
            #time.sleep(3)
            g.show_go_screen()
            loop = False
            


        if snake.history[0][0] > width:
            snake.history[0][0] = 0
        if snake.history[0][0] < 0:
            snake.history[0][0] = width

        if snake.history[0][1] > height:
            snake.history[0][1] = 0
        if snake.history[0][1] < 0:
            snake.history[0][1] = height

        pygame.display.update()
        clock.tick(10)
       

gameLoop()

