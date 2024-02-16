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
        self.ref = list(ref)
        self.alt = list(alt)

    def __str__(self):
        return f"my_data: pos={self.pos}, ref='{self.ref}', alt='{self.alt}'"

    def bubble_sort(self):
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
                break

class my_string:
    def __init__(self):
        self.string = list(original_string)
        self.size = len(self.string)
        self.cos = self.size // CHUNK_SIZE
        self.res = self.size % CHUNK_SIZE
        self.num_chunks = self.cos + (1 if self.res != 0 else 0) # If res != 0, then add 1, else add 0

    def print_chunk(self):
        print("String\n")

        print("Size: ", self.size)
        print("Numbers of Chunks: ", self.num_chunks)
        print("Last chunk size: ", self.res, end='\n\n')

        print("Chunks\n")

        i = 0

        for char in range(self.cos):
            print(i, "\t", end='')
            for i in range(i, i + CHUNK_SIZE):
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

def gen_comb(data, string):
    strings = []
    j = 0

    for i in range(string.num_chunks):
        strings.append(my_string())
        try:
            n = data.pos.index(j)
            print(i, j, n)
            strings[i].string[j] = data.alt[n]
        except ValueError:
            pass
        j += CHUNK_SIZE
    i += 1


    return strings

main_string = my_string()
#main_string.print_chunk()
print(''.join(main_string.string))

data = my_data(pos, ref, alt)
data.bubble_sort()

print(data)
    
combinations = gen_comb(data, main_string)


for i in range(main_string.cos):
    #combinations[0].print_chunk()
    print(i, ''.join(combinations[i].string))
