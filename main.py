# https://github.com/Forajido24/Actividad4

#import pandas as pd

CHUNK_SIZE = 5

original_string = "TGTAGTGCAGTGGCGTGATCTTGGCTCACTGCAGCCTCCACCTTAGAGCAATCCTCTTGCCTCATCCTCCCGGGTAGTTGGGACTACATGTGCATGCCACATGCCTGGCTAATTTTTGTATTTTTAGTA"
pos = [15, 100, 54, 33, 19, 97, 13]
ref = "TATGCCC" 
alt = "AGAAGTA"

class my_data:
    def __init__(self, pos, ref, alt):
        self.pos = pos
        self.ref = ref
        self.alt = alt

    def __str__(self):
        return f"my_data: pos={self.pos}, ref='{self.ref}', alt='{self.alt}'"

    def bubble_sort(self):
        self.ref = list(self.ref)
        self.alt = list(self.alt)

        n = len(self.pos)

        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if self.pos[j] > self.pos[j+1]:
                    self.pos[j], self.pos[j+1] = self.pos[j+1], self.pos[j]
                    self.ref[j], self.ref[j+1] = self.ref[j+1], self.ref[j]
                    self.alt[j], self.alt[j+1] = self.alt[j+1], self.alt[j]
                    swapped = True
            if not swapped:
                self.ref = ''.join(self.ref)
                self.alt = ''.join(self.alt)
                break

class my_string:
    def __init__(self, string):
        self.string = string
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

main_string = my_string(original_string)

main_string.print_chunk()

data = my_data(pos, ref, alt)
data.bubble_sort()

print(data)
