import pygame


class Window:
    """Рендер окна с текстом"""

    FPS = 60
    BG_COLOR = (255, 255, 255)
    WINDOW_SIZE = (700, 800)
    WINDOW_CAPTION = 'S7 Downloader'
    FONT_FILE = 'fonts/FiraMonoOT-Regular.otf'

    def __init__(self, text='None text'):
        self.text = text
        pygame.init()
        pygame.display.set_caption(self.WINDOW_CAPTION)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.font = pygame.freetype.Font(self.FONT_FILE, 40)

    def update(self):
        self.clock.tick(self.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        text_tect = self.font.get_rect(self.text)
        self.screen.fill(self.BG_COLOR)
        self.font.render_to(self.screen,
                            text_tect.topleft,
                            self.text,
                            (0, 0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    window = Window()
    while True:
        window.update()
