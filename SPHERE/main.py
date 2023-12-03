from sphere import Sphere
from orbiter import Orbiter
import pygame

WIDTH, HEIGHT = 1000, 700
FPS = 100
pygame.display.set_caption("Nitin Sphere")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    sphere1 = Sphere(origin_x = WIDTH/2, origin_y = HEIGHT/2, scale=30)
    sphere2 = Sphere(origin_x = WIDTH/2, origin_y = HEIGHT/2, radius=5, scale=20, rotation_speed=0.001, surface_color=(255, 0, 0))
    orbiter1 = Orbiter(origin_x = WIDTH/2, origin_y = HEIGHT/2, radius=10, scale=20, rotation_speed=0.03, surface_color=(100, 200, 200))
    orbiter2 = Orbiter(origin_x = WIDTH/2, origin_y = HEIGHT/2, radius=9, scale=20, rotation_speed=0.01, surface_color=(100, 200, 200))

    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        screen.fill((0, 0, 0)) #Filling screen with black color

        sphere1.rotateSphere_C()
        sphere2.rotateSphere_AntiC()
        
        orbiter1.rotateSphere_C()
        orbiter2.rotateSphere_C()

        render(sphere1, 1)
        render(sphere2, 1)
        render(orbiter1, 1)
        render(orbiter2, 1)
        
        pygame.display.update()

def render(sphere, size):
    for point in sphere.projected_points:
        pygame.draw.circle(screen, sphere.surface_color, (point[0], point[1]), size)

if __name__ == '__main__':
    main()