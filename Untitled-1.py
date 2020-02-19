import arcade
import math

SPRITE_SCALING_PIZZA = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ANGLE = 120

SCREEN_TITLE = "Starting Template"

class Pizza(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image,scale)

    def update(self):
        self.angle += self.change_angle


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        self.pizza = arcade.SpriteList()
        self.pizza_sprite = Pizza("F:\AI\pizza.png",SPRITE_SCALING_PIZZA)
        self.pizza_sprite.center_x = SCREEN_WIDTH/2
        self.pizza_sprite.center_y = SCREEN_HEIGHT/2
        self.pizza.append(self.pizza_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.pizza.draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        
        if key == arcade.key.RIGHT:
            self.pizza_sprite.change_angle = ANGLE
            self.pizza.update()
        elif key == arcade.key.LEFT:
            self.pizza_sprite.change_angle = -ANGLE
            self.pizza.update()

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()