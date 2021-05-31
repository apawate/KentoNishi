import math
import pygame
pygame.init()

BLACK = (0, 0, 0)
DARK_GRAY = (64, 64, 64)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
WHITE = (255, 255, 255)

FONT = pygame.font.SysFont("ubuntu", 24)
IMGS = {
    "original": pygame.image.load("images/original.jpg"),
    "face": pygame.image.load("images/face.jpg"),
    "noface": pygame.image.load("images/noface.jpg"),
}
CLOCK = pygame.time.Clock()


class BouncyKento:
    size = 200

    def __init__(self, pos, bounds, x_vel=0, y_vel=0, r_vel=0, gravity=-0.45, restitution=0.95):
        self.pos = list(pos)
        self.bounds = bounds
        self.vel = [x_vel, y_vel, r_vel]
        self.grav = gravity
        self.restitution = restitution

        self.img = pygame.transform.scale(IMGS["original"], (self.size, self.size))

    def sim(self):
        self.vel[1] -= self.grav
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        h = self.size/2
        if self.pos[0] <= self.bounds[0]+h:
            self.vel[0] *= -self.restitution
            self.pos[0] = h
        if self.pos[0] >= self.bounds[1]-h:
            self.vel[0] *= -self.restitution
            self.pos[0] = 1280-h
        if self.pos[1] <= self.bounds[2]+h:
            self.vel[1] *= -self.restitution
            self.pos[1] = h
        if self.pos[1] >= self.bounds[3]-h:
            self.vel[1] *= -self.restitution
            self.pos[1] = 720-h

    def draw(self, surface):
        # offset = abs(math.sin(2*math.radians(self.pos[2]))) * self.size/2
        # loc = (self.pos[0]-self.size/2-offset, self.pos[1]-self.size/2-offset)
        # img = pygame.transform.rotate(self.img, self.pos[2])
        # surface.blit(img, loc)

        surface.blit(self.img, (self.pos[0]-self.size/2, self.pos[1]-self.size/2))


def boot(surface):
    progress = 0

    while True:
        CLOCK.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        surface.fill(WHITE)
        pygame.draw.rect(surface, LIGHT_GRAY, (540, 620, progress*200, 20))
        pygame.draw.rect(surface, GRAY, (540, 620, 200, 20), 2)

        img = IMGS["original"] if (int(progress*10) % 2) == 1 else IMGS["noface"]
        surface.blit(img, (640-img.get_width()//2, 120))

        text = FONT.render("KentOS is booting...", 1, BLACK)
        surface.blit(text, (640-text.get_width()//2, 40))

        progress += 0.003
        if progress > 1:
            break


def talk(surface):
    kento = BouncyKento((640, 500, 0), (0, 1280, 0, 720))

    while True:
        CLOCK.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    kento.vel[1] = -10

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            kento.vel[0] += 0.5
        elif keys[pygame.K_LEFT]:
            kento.vel[0] -= 0.5

        surface.fill(WHITE)
        kento.sim()
        kento.draw(surface)


def main():
    pygame.display.set_caption("KentOS")
    pygame.display.set_icon(IMGS["original"])
    surface = pygame.display.set_mode((1280, 720))
    surface.fill(WHITE)

    boot(surface)
    talk(surface)


main()
