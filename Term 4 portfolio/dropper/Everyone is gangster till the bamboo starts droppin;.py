#Everyone is gangster till the bamboo starts droppin
#created by Isaac Arthur
#4/19


#imports
from superwires import games, color
import random



# global variables

games.init(screen_width = 640, screen_height = 480, fps= 60)

LIVES = 3
SCORE = 0


#classes

class  Panda(games.Sprite):
    image = games.load_image("images/panda.png", transparent = True)

    def __init__(self, y = 60, speed = 5, odds_change = 33):
        super(Panda,self).__init__(image = Panda.image,
                                   x = games.screen.width/2,
                                   y = y,
                                   dx = speed)

        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()
        

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_bamboo = Bamboo(x = self.x)
            games.screen.add(new_bamboo)
            self.time_til_drop = random.randint(60, 150)

class Basket(games.Sprite):
    image = games.load_image("images/basket.jpg", transparent = True)

    def __init__(self):
        super(Basket, self).__init__(image = Basket.image,
                                     x = games.mouse.x,
                                     bottom = games.screen.height)
    
    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        global SCORE
        for bamboo in self.overlapping_sprites:
            SCORE += 10
            bamboo.handle_caught()
            
        

class Bamboo(games.Sprite):
    image = games.load_image("images/bamboo.png")
    speed  = 10
    
    def __init__(self, x, y = 90, speed = random.randrange(speed)+1):
        super(Bamboo,self).__init__(image = Bamboo.image,
                                    x = x,
                                    y = y,
                                    dy = speed)
        

    def update(self):
        global LIVES
        if self.bottom > games.screen.height:
            self.destroy()
            LIVES -= 1
        if LIVES == 0:
            self.end_game()

    def end_game(self):
        """end the game"""
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

    def handle_caught(self):
        self.destroy()


class ScText(games.Text):
    def update(self):
        self.value = SCORE




#main
def main():
    
#   load data
    wall_image = games.load_image("images/bambooforest.jpg", transparent = False)


#   create objects
    the_basket = Basket()
    the_panda = Panda()
    the_score = ScText(value = SCORE,
                   size = 60,
                   color = color.black,
                   x = 550,
                   y = 30)


#   draw
    games.screen.background = wall_image
    games.screen.add(the_basket)
    games.screen.add(the_panda)
    games.screen.add(the_score)



#   game setup
    games.mouse.is_visible = False
    games.screen.event_grab = True


#   start loop
    games.screen.mainloop()




#starting point
main()
