import random

def main():
    file = open("model.txt", "w")

    file.write("Layer 1:\n\n")

    for i in range(128):
        file.write(str(random.randint(1, 64)))

        file.write(" ")

    file.write("\n\n")

    file.write("Layer 2:\n\n")

    file.write("B")

    for i in range(64):
        file.write(str(random.randint(1, 32)))

        file.write(" ")

    file.write("\n\n")

    file.write("Layer 3:\n\n")

    file.write("C")

    for i in range(32):
        file.write(str(random.randint(1, 16)))

        file.write(" ")

    file.write("\n\n")

    file.write("Layer 4:\n\n")

    file.write("D")

    for i in range(16):
        file.write(str(random.randint(1, 8)))

        file.write(" ")

    file.write("\n\n")

    file.write("Layer 5:\n\n")

    file.write("E")

    for i in range(8):
        file.write(str(random.randint(1, 4)))

        file.write(" ")

    file.write("\n\n")

    file.write("First layer kernels:")

    file.write("F")

    file.write("\n\n")

    for i in range(128):
        for i in range(4):
            file.write(str(random.uniform(-0.1, 0.1)))

            file.write(" ")

        file.write("\n")

    file.write("\n\n")

    file.write("Second layer kernels:")

    file.write("G")

    for i in range(64):
        for i in range(4):
            file.write(str(random.uniform(-0.1, 0.1)))

            file.write(" ")

        file.write("\n")

    file.write("\n\n")

    file.write("Third layer kernels:")

    file.write("H")

    for i in range(32):
        for i in range(4):
            file.write(str(random.uniform(-0.1, 0.1)))

            file.write(" ")

        file.write("\n")

    file.write("\n\n")

    file.write("Fourth layer kernels:")

    file.write("I")

    for i in range(16):
        for i in range(4):
            file.write(str(random.uniform(-0.1, 0.1)))

            file.write(" ")

        file.write("\n")

    file.write("\n\n")

    file.write("Fifth layer kernels:")

    file.write("J")

    for i in range(8):
        for i in range(4):
            file.write(str(random.uniform(-0.1, 0.1)))

            file.write(" ")

        file.write("\n")

    file.write("\n\n")

    file.write("First layer biases:")

    file.write("K")

    file.write("\n\n")

    for i in range(128):
        file.write("0")

        file.write(" ")

    file.write("\n\n")

    file.write("Second layer biases:")

    file.write("L")

    file.write("\n\n")

    for i in range(64):
        file.write("0")

        file.write(" ")

    file.write("\n\n")

    file.write("Third layer biases:")

    file.write("M")

    file.write("\n\n")

    for i in range(32):
        file.write("0")

        file.write(" ")

    file.write("\n\n")

    file.write("Fourth layer biases:")

    file.write("N")

    file.write("\n\n")

    for i in range(16):
        file.write("0")

        file.write(" ")

    file.write("\n\n")

    file.write("Fifth layer biases:")

    file.write("O")

    file.write("\n\n")

    for i in range(8):
        file.write("0")

        file.write(" ")

    file.close()

main()
