#asteroids 1.0
#Isaac Arthur

#imports
from superwires import games
import random
import math




#Global info
games.init(screen_width = 640, screen_height = 480, fps = 60)






#classes

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("images/llama_small.png"),
              MEDIUM : games.load_image("images/llama_med.png"),
              LARGE : games.load_image("images/llama_big.png")}
    SPEED = 2

    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(image = Asteroid.images[size],
                                        x = x,
                                        y = y,
                                        dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                        dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)
                                                           



        self.size = size
    def update(self):
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.bottom > games.screen.height:
            self.top = 0
        if self.top < 0:
            self.bottom = games.screen.height


class Ship(games.Sprite):
    image = games.load_image("images/battlebus.png")
    sound = games.load_sound("sounds/thrust.wav")
    ROTATION_STEP = 5
    VELOCITY_STEP = 0.03

    def __init__(self):
        super(Ship,self).__init__(image = Ship.image,
                                  x = games.screen.width/2,
                                  y = games.screen.height/2)

    def update(self):
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP


        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.bottom > games.screen.height:
            self.top = 0
        if self.top < 0:
            self.bottom = games.screen.height

                                                           










#main
def main():


    #load data
    bg_img = games.load_image("Images/fortnite map.jpg")
                                    
                                


    #Create objects
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x = x, y = y, size = size)
        games.screen.add(new_asteroid)

    #create ship
        player = Ship()
    



    #draw objects
    games.screen.background = bg_img
    games.screen.add(player)
                                                       








    #game setup











    #start main loop
    games.screen.mainloop()

main()

        









                        
