import pygame
import proc_noise


# Screen dimensions
SCREEN_WIDTH = 330
SCREEN_HEIGHT = 330

class node():
    def __init__(self, x, y, altitude, biome):
        self.x = x
        self.y = y
        self.altitude = altitude
        self.biome = biome



def gen_terrain(map_nodes, noise):
    if len(noise) >= len(map_nodes):
        for i in range(len(map_nodes)):
            map_nodes[i].altitude = noise[i]
    else:
        print("World too big!")



nodes_World1 = []

for i in range(0,SCREEN_WIDTH, 10):
    for j in range(0,SCREEN_HEIGHT, 10):
        nodes_World1.append(node(i,j,0,"none"))

gen_terrain(nodes_World1, proc_noise.Noise3)


def show_map(map):
    for n in map:
        a = int(n.altitude)
        r = max(0, min(255, 128 + a))
        g = 0
        b = max(0, min(255, 127 - a))
        pygame.draw.rect(screen, (r, g, b), (n.x, n.y, 10, 10))





# Initialize Pygame
pygame.init()



# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Procedural Terrain")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Main game loop
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with black
    screen.fill((0, 0, 0))
    show_map(nodes_World1)
    
    # Update display
    pygame.display.flip()

pygame.quit()
