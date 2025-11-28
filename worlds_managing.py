import proc_noise

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



def save_world(world, file):
    with open(file, "w") as f:
        for n in world:
            f.write(f"{n.x},{n.y},{n.altitude},{n.biome}\n")
    pass



def load_world(world_dir):
    destination_vector = []
    with open(world_dir, "r") as file:
        dump = file.readlines()
    for i in dump:
        x, y, altitude, biome = i.strip().split(",")
        destination_vector.append(node(int(x), int(y), float(altitude), biome))

    return destination_vector

def populate(nodes_map, x, y):
    for i in range(0, x*10, 10):
        for j in range(0, y*10, 10):
            nodes_map.append(node(i,j,0,"void"))


def generate_biome_distibution(world, noise):
    for i in range(len(world)):
        if world[i].altitude < -80:
            if noise[i] < -100:
                world[i].biome = "ice"
            else:
                world[i].biome = "ocean"
        elif world[i].altitude < 0:
            world[i].biome = "beach"
        elif world[i].altitude < 20:
            world[i].biome = "plains"
        else:
            world[i].biome = "mountain"
'''
test_biomes = []
populate(test_biomes, 108, 72)
gen_terrain(test_biomes, proc_noise.Noise4_2_2)
generate_biome_distibution(test_biomes, proc_noise.Noise4_5)
save_world(test_biomes, "Worlds/testworld2.txt")
'''
