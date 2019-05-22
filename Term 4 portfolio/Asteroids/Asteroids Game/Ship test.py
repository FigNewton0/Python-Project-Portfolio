
#Read Keys
#Demonstrates readoing the keyboard

from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 60)

class Ship(games.Sprite):
    ship_image =  games.load_image("Images/battlebus.png" , transparent = True)

    def __init__(self):
        super(Ship,self).__init__(image = Ship.ship_image,
                                  x = games.screen.width/2,
                                  y = games.screen.height/2)

    def update(self):
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            self.y -= 5
        if games.keyboard.is_pressed(games.K_s) or games.keyboard.is_pressed(games.K_DOWN):
            self.y += 5
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 5
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 5
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

            
def main():

    #Load Data
    map_image = games.load_image("Images/fortnite map.jpg", transparent = False)
    explosion_files = ["images/explosion1.png",
                       "images/explosion2.png",
                       "images/explosion3.png",
                       "images/explosion4.png",
                       "images/explosion5.png",
                       "images/explosion6.png"]

##    games.music.load("sounds/Wii Sports Theme (8-Bit Remix) - Wii Sports.mp4")
                       

                       
    

    #Create Objects
    the_ship = Ship()
    explosion = games.Animation(images = explosion_files,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                n_repeats = 0,
                                repeat_interval = 10)

    #Draw
    games.screen.background = map_image
    games.screen.add(the_ship)
    games.screen.add(explosion)
##    games.music.play()

    #Game Setup

    #Start Loop
    games.screen.mainloop()


main()




