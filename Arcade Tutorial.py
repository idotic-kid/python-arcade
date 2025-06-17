"""
Platformer Game

python -m arcade.examples.platform_tutorial.02_draw_sprites
"""
import arcade
from random import randint
import math

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "slop game"
PLAYER_MOVEMENT_SPEED = 5
TILE_SCALING = 0.5


class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.highscore = 0


        self.background_color = arcade.csscolor.CORNFLOWER_BLUE


    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.dead = 0

                # Variable to hold our texture for our player
        self.player_texture = arcade.load_texture(
            "slpobat.png"
        )
        self.ball_texture = arcade.load_texture(
            "angry bvir.png"
        )

        # Separate variable that holds the player sprite
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_sprite.angle = 45
        self.player_sprite.change_angle = 2

        # variable for slop ball
        self.ball = arcade.Sprite(self.ball_texture)
        self.ball.center_x = 300
        self.ball.center_y = 200
        self.ball.change_x = PLAYER_MOVEMENT_SPEED
        self.ball.change_y = PLAYER_MOVEMENT_SPEED


        # SpriteList for our player
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.player_list.append(self.ball)
        self.score = 0
        self.dead = 0

        # Create a Simple Physics Engine, this will handle moving our
        # player as well as collisions between the player sprite and
        # whatever SpriteList we specify for the walls.
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite
        )

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()
        
        #die
        if self.dead:
            arcade.draw_text("you lose", WINDOW_WIDTH/2, WINDOW_HEIGHT/2, arcade.color.WHITE, 80)    
            self.score = 0
            self.dead += 1



        # Draw our sprites
        self.player_list.draw()
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 1000, WINDOW_HEIGHT-30, arcade.color.WHITE, 24)


    def _point_sprite(self, sprite, target):
        # Calculate the angle between the two sprites
        angle = math.degrees(math.atan2(target.center_y - sprite.center_y, target.center_x - sprite.center_x))
        # Set the sprite's angle
        sprite.angle = angle


    def on_update(self, delta_time):
        """Movement and Game Logic"""
        # Move the player using our physics engine
        self.physics_engine.update()

        #check bounds  

        if self.player_sprite.center_y > WINDOW_HEIGHT/2:
            self.player_sprite.center_y = WINDOW_HEIGHT/2

        # Check   hits
        hitshit = arcade.check_for_collision(self.player_sprite, self.ball)
        if hitshit:
            self.score +=1

            self.ball.angle += randint(160, 200)
            if self.ball.angle > 360:
                self.ball.angle -=360

            h = math.sqrt((self.ball.change_y*self.ball.change_y)+(self.ball.change_x*self.ball.change_x))

            self.ball.change_y = math.sin(self.ball.angle)*h
            self.ball.change_y = math.cos(self.ball.angle)*h
            self.ball.forward(-5)


        # move terrence
        self.ball.center_x += self.ball.change_x
        self.ball.center_y += self.ball.change_y
        self.ball.angle = math.degrees(math.atan((self.ball.change_y/self.ball.change_x)))


        # bounce terance
        if self.ball.left < 0 or self.ball.right > WINDOW_WIDTH:
            self.ball.change_x *= -1  # Reverse horizontal direction
        if self.ball.bottom < 0 or self.ball.top > WINDOW_HEIGHT:
            self.ball.change_y *= -1  # Reverse vertical direction
        
        #die
        if self.ball.bottom < 1:
            self.dead += 1
        
        if self.dead > 30:
            self.setup()



    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
