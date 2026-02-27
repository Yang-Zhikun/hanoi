import pygame


class DisplayEngine:
    """A class to handle the display engine for the Hanoi Tower game."""


    def __init__(self, 
                 window_width: int = 800, 
                 window_height: int = 600,
                 background_color: tuple = (0, 0, 0),
                 caption: str = None):
        """
        Initialize the display engine with the given width and height.
        """
        pygame.init()
        self.surface = pygame.display.set_mode((window_width, window_height))
        self.background_color = background_color
        if caption:
            pygame.display.set_caption(caption)

    def flip(self):
        """Update the display."""
        pygame.display.flip()