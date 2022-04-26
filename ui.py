import pygame


class Window:
    """Рендер окна с текстом"""

    FPS = 60
    BG_COLOR = (255, 255, 255)
    WINDOW_SIZE = (700, 800)
    WINDOW_CAPTION = 'S7 Downloader'
    FONT_FILE = 'fonts/FiraMonoOT-Regular.otf'
    STATUS = True

    def __init__(self, config_dataclass, text='None text', ):
        self.config = config_dataclass
        self.text = text
        pygame.init()
        pygame.display.set_caption(self.WINDOW_CAPTION)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.font = pygame.freetype.Font(self.FONT_FILE, 40)
        self.settings_font = pygame.freetype.Font(self.FONT_FILE, 10)

    def set_text(self, text):
        self.text = text

    def draw_rect(self):
        points = [(5, 5),
                  (self.WINDOW_SIZE[0] - 10, 100)]
        pygame.draw.rect(self.screen, (0, 0, 0,), points, 1)

    def draw_settings_text(self):
        x, y = 10, 10
        y_add = 11
        self.draw_line_text(self.settings_font,
                            (x, y),
                            f'SERVER: {self.config.server_host}')
        y += y_add
        for folder in self.config.server_folders:
            self.draw_line_text(self.settings_font,
                                (x, y),
                                f'PATH: {folder}')
            y += y_add

    def draw_line_text(self, font, coords, text):
        font.render_to(self.screen, coords, text)

    def update(self):
        self.clock.tick(self.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.STATUS = pygame.get_init()
                exit()

        # text = self.font.get_rect(self.text)
        self.screen.fill(self.BG_COLOR)
        # self.font.render_to(self.screen,
        #                     # text.topleft,
        #                     (10, 10),
        #                     self.text,
        #                     (0, 0, 0))
        self.draw_rect()
        self.draw_settings_text()
        pygame.display.flip()


if __name__ == '__main__':
    from config_parser import Config

    config = Config()
    window = Window(config_dataclass=config)
    while True:
        window.update()
