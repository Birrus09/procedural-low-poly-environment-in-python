import proc_noise


file1 = open("Worlds/World1.txt", "w")

for i in range(108*72):
    file1.write(str(proc_noise.Noise4_1_2[i]) + "\n")

file1.close()
