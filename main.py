# https://github.com/Forajido24/Actividad4

#import pandas as pd

CHUNK_SIZE = 5

original_string = "TGTAGTGCAGTGGCGTGATCTTGGCTCACTGCAGCCTCCACCTTAGAGCAATCCTCTTGCCTCATCCTCCCGGGTAGTTGGGACTACATGTGCATGCCACATGCCTGGCTAATTTTTGTATTTTTAGTA"

class my_string:
    def __init__(self, pos, ref, alt, string):
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.string = string

        # Sizes 
        self.size = len(self.string)
        self.cos = self.size // CHUNK_SIZE
        self.res = self.size % CHUNK_SIZE

    def print_chunk(self):
        print("String\n")

        print("Size: ", self.size)
        print("Numbers of Chunks: ", self.cos)
        print("Last chunk size: ", self.res, end='\n\n')

        print("Chunks\n")

        i = 0

        for char in range(self.cos):
            print(i, "\t", end='')
            for i in range(i, i+CHUNK_SIZE):
                print(self.string[i], end='')
                #print(i)
            i += 1
            print("")
            #print("------------------------------------")

        print(i, end='\t')

        for i in range(i, i + self.res):
            print(self.string[i], end='')
            #print(i)

        print()


main_string = my_string(0, "", "", original_string)

main_string.print_chunk()

