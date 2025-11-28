import worlds_managing
import proc_noise


Worldsine = []
worlds_managing.populate(Worldsine, 108, 72)
worlds_managing.gen_terrain(Worldsine, proc_noise.Noise5)
worlds_managing.save_world(Worldsine, "Worlds/worldsine.txt")

while True:
    print("Options: 1) create world, 2) see worlds directory 3) see available noises 4) quit")
    choice = int(input("command: "))
    if choice == 1:
        width = int(input("width: "))
        height = int(input("height: "))
        world_dir = input("world name: ")
        world_dir = "Worlds/" + world_dir + ".txt"
        world_noise = input("noise: ")
        new_world = []
        worlds_managing.populate(new_world, width, height)
        worlds_managing.gen_terrain(new_world, getattr(proc_noise, world_noise))
        worlds_managing.save_world(new_world, world_dir)
        print("world created!")
    elif choice == 2:
        print("Worlds directory:")
        print("")
        for file in os.listdir("Worlds"):
            if file.endswith(".txt"):
                print(file - ".txt")
    elif choice == 3:
        print("Available noises:")
        for attr in dir(proc_noise):
            if not attr.startswith("__"):
                print(attr)
    else:
        break
