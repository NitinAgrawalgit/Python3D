from cube import Cube
import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60
pygame.display.set_caption("Nitin Cube")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    cube1 = Cube(WIDTH/2, HEIGHT/2)
    cube2 = Cube(WIDTH/2, HEIGHT/2, size=75, line_color=(200, 0, 200))
    cube3 = Cube(WIDTH/2, HEIGHT/2, size=50, line_color=(0, 200, 200))
    cube4 = Cube(WIDTH/2, HEIGHT/2, size=25, line_color=(200, 200, 0))

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

        cube1.rotatePoints()
        cube2.rotatePoints()
        cube3.rotatePoints()
        cube4.rotatePoints()

        render(cube1)
        render(cube2)
        render(cube3)
        render(cube4)
        
        # for i in range(8):
        #     pygame.draw.line(screen, (255, 255, 255), (cube1.projected_points[i][0], cube1.projected_points[i][1]), (cube2.projected_points[i][0], cube2.projected_points[i][1]))
        #     pygame.draw.line(screen, (255, 255, 255), (cube3.projected_points[i][0], cube3.projected_points[i][1]), (cube4.projected_points[i][0], cube4.projected_points[i][1]))

        pygame.display.update()

def connect_points(i, j, cube):
    pygame.draw.line(screen, cube.line_color, (cube.projected_points[i][0], cube.projected_points[i][1]), (cube.projected_points[j][0], cube.projected_points[j][1]), cube.line_thickness)

def render(cube):
    for p in range(4):
        connect_points(p, (p+1) % 4, cube)
        connect_points(p+4, ((p+1) % 4) + 4, cube)
        connect_points(p, (p+4), cube)    

if __name__ ==  '__main__':
    main()
