import pygame
from physics import Particle

def main():
    pygame.init()
    width, height = 960, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Gravity Lab")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 26)
    particles = []
    gravity = 450
    anchor = None
    running = True
    while running:
        dt = min(clock.tick(60) / 1000, 0.03)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    particles.clear()
                elif event.key == pygame.K_UP:
                    gravity = min(1500, gravity + 50)
                elif event.key == pygame.K_DOWN:
                    gravity = max(0, gravity - 50)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                anchor = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and anchor:
                x, y = anchor
                mx, my = event.pos
                particles.append((Particle(x, y, (x-mx)*3, (y-my)*3), []))
                particles = particles[-30:]
                anchor = None
        screen.fill((15, 23, 42))
        for particle, trail in particles:
            particle.step(dt, gravity, width, height)
            point = (int(particle.x), int(particle.y))
            trail.append(point)
            del trail[:-90]
            if len(trail) > 1:
                pygame.draw.lines(screen, (56, 110, 140), False, trail, 2)
            pygame.draw.circle(screen, (94, 234, 212), point, int(particle.radius))
        if anchor:
            pygame.draw.line(screen, (250, 204, 21), anchor, pygame.mouse.get_pos(), 3)
        screen.blit(font.render(f"GRAVITY LAB  |  Gravity: {gravity} px/s²", True, (240, 248, 255)), (20, 18))
        screen.blit(font.render("Drag and release to launch  |  Up/Down: gravity  |  R: reset", True, (160, 180, 200)), (20, 48))
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
