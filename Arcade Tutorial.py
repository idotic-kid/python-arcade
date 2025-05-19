"""
Platformer Game

python -m arcade.examples.platform_tutorial.02_draw_sprites
"""
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "slop game"
PLAYER_MOVEMENT_SPEED = 10


class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        # Variable to hold our texture for our player
        self.player_texture = arcade.load_texture(
            "angry bvir.png"
        )

        # Separate variable that holds the player sprite
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128

        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        self.physics_engine = arcade.PhysicsEngineSimple(
        self.player_sprite
        )

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw our sprites
        arcade.draw_sprite(self.player_sprite)

    def on_update(self, delta_time):
        """Movement and Game Logic"""
        # Move the player using our physics engine
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
            """Called whenever a key is pressed."""

            if key == arcade.key.UP or key == arcade.key.W:
                self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()