#asteroids 1.5
#Isaac Arthur

#imports
from superwires import games, color
import random
import math




#Global info
games.init(screen_width = 640, screen_height = 480, fps = 60)






#classes
class Game(object):
    def __init__(self):
        #set level
        self.level = 0
        #load sound fro level advancement
        self.sound = games.load_sound("sounds/level.wav")
        # create score
        self.score = games.Text(value = 0,
                   size = 30,
                   color = color.white,
                   top = 5,
                   right = games.screen.width - 10,
                   is_collideable = False)
        games.screen.add(self.score)
        #create player's ship
        self.player = Ship(game = self, 
                         x = games.screen.width/2,
                         y = games.screen.height/2)
        games.screen.add(self.player)
    def play(self):
        games.music.load("sounds/Wii Sports Theme (8-Bit Remix) - Wii Sports.ogg")
        games.music.play(-1)

        bg_img = games.load_image("Images/fortnite map.jpg")
        games.screen.background = bg_img

        self.advance()

        games.screen.mainloop()

    def advance(self):
        self.level += 1

        BUFFER = 150

        for i in range(self.level):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.width - y_min)
            x = self.player.x + x_distance
            y = self.player.y + y_distance
            x %= games.screen.width
            y %= games.screen.height
            new_asteroid = Asteroid(game = self, x = x, y = y, size = Asteroid.LARGE)
            games.screen.add(new_asteroid)

        level_message = games.Message(value = "Level " + str(self.level),
                                      size = 40,
                                      color = color.blue,
                                      x = games.screen.width/2,
                                      y = games.screen.height/10,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

        if self.level > 1:
            self.sound.play()

    def end(self):
        end_message = games.Message(value = "Game over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)



        
    


class Wrapper(games.Sprite):
    def update(self):
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.bottom > games.screen.height:
            self.top = 0
        if self.top < 0:
            self.bottom = games.screen.height

    def die(self):
        self.destroy()
        

class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
                
    def die(self):
        #create explosion
        new_explosion = Explosion(x = self.x,  y = self.y)
        #add to screen
        games.screen.add(new_explosion)
        
        self.destroy()

class Asteroid(Wrapper):

    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("images/llama_small.png"),
              MEDIUM : games.load_image("images/llama_med.png"),
              LARGE : games.load_image("images/llama_big.png")}
    SPEED = 2
    SPAWN = 2
    POINTS = 30
    total = 0

    def __init__(self,game, x, y, size):
        Asteroid.total += 1
        super(Asteroid, self).__init__(image = Asteroid.images[size],
                                        x = x,
                                        y = y,
                                        dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                        dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)
                                                           



        self.size = size
        self.game = game
    

    def die(self):
        # if asteroid is not small, replace with two smaller ones
        Asteroid.total -= 1
        #add to score
        self.game.score.value += int(Asteroid.POINTS / self.size)
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game, x = self.x, 
                                        y = self.y,
                                        size = self.size-1)
                games.screen.add(new_asteroid)
        
        if Asteroid.total == 0:
            self.game.advance()
        super(Asteroid, self).die()


class Ship(Collider):
    image = games.load_image("images/battlebus.png")
    sound = games.load_sound("sounds/thrust.wav")
    ROTATION_STEP = 5
    VELOCITY_STEP = 0.03
    MISSILE_DELAY = 25
    VELOCITY_MAX = 3
    LIVES = 2

    def __init__(self, game, x, y):
        super(Ship,self).__init__(image = Ship.image,
                                  x = x,
                                  y = y)
        self.game = game
        self.missile_wait = 0

    def update(self):
        super (Ship, self).update()
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if self.missile_wait > 0:
            self.missile_wait -= 1
                
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
                new_missile = Missile(self.x, self.y, self.angle)
                games.screen.add(new_missile)
                self.missile_wait = Ship.MISSILE_DELAY


    def die(self):
        if self.LIVES == 0:
            asteroids = Game()
            asteroids.end()
        else:
            self.LIVES -= 1
            end_message = games.Message(value = self.LIVES + 1,
                                        size = 90,
                                        color = color.green,
                                        x = games.screen.width - 50,
                                        y = games.screen.height - 50,
                                        is_collideable = False)
            games.screen.add(end_message)
            return self.LIVES
        
            



            









class Missile(Collider):
    image = games.load_image("images/Fortnite_Boogie_Bomb.png.jpg")
    sound = games.load_sound("sounds/Laser Blasts-SoundBible.com-108608437.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40
    def __init__(self, ship_x, ship_y, ship_angle):
        Missile.sound.play()
        angle = ship_angle * math.pi / 180


        # calculate missile's starting position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)

        x = ship_x + buffer_x
        y = ship_y + buffer_y

        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)
        super(Missile,self).__init__(image = Missile.image,
                                     x = x,
                                     y = y,
                                     dx = dx,
                                     dy = dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        super(Missile, self).update()
        self.lifetime -= 1        
        if self.lifetime == 0:
            self.destroy()


        



                                                           



class Explosion(games.Animation):
    sound = games.load_sound("sounds/Explosion.wav")
    expimages = ["images/explosion1.png",
                       "images/explosion2.png",
                       "images/explosion3.png",
                       "images/explosion4.png",
                       "images/explosion5.png",
                       "images/explosion6.png"]
    def __init__(self, x, y):
        super(Explosion, self). __init__(images = Explosion.expimages,
                                         x = x, y = y,
                                         repeat_interval = 4,
                                         n_repeats = 1,
                                         is_collideable = False)
        Explosion.sound.play()
                                         






#main
def main():
    asteroids = Game()
    asteroids.play()


main()

        









                        
