# https://github.com/Forajido24/Actividad4

#import pandas as pd

CHUNK_SIZE = 10
CHUNK_RUN = 5

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
        return f"my_data: pos={self.pos}, ref='{''.join(self.ref)}', alt='{''.join(self.alt)}'"

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
        self.cos = self.size // CHUNK_RUN - 1
        self.res = self.size % CHUNK_SIZE
        self.num_chunks = self.cos + (1 if self.res != 0 else 0) # If res != 0, then add 1, else add 0

    def print_chunk(self):
        print("String\n")

        print("Size: ", self.size)
        print("Max numbers of Chunks: ", self.num_chunks)
        print("Last chunk size: ", self.res, end='\n\n')

        print("Runs\n")

        i = 0
        runs = 0

        for runs in range(self.cos):
            print(runs + 1, "\t", i, "-", i + CHUNK_SIZE, "\t", end='')
            for i in range(i, i + CHUNK_SIZE):
                print(self.string[i], end='')
                #print(i)
            i -= CHUNK_RUN
            i += 1
            print("")
            #print("------------------------------------")

        runs += 1

        print(runs + 1, "\t", i, "-", i + self.res , end='\t')

        for i in range(i, i + self.res):
            print(self.string[i], end='')
            #print(i)

        print("\n")

def gen_comb(data, string):
    strings = []
    i = k = n = 0
    j = 1

    strings.append(my_string())

    for i in range(string.cos):
        swapped = False
        for j in range(j, j + CHUNK_SIZE):
            try:
                n = data.pos.index(j) # returns the index of the element j
                strings[k].string[j] = data.alt[n] # makes the swap
                swapped = True
            except ValueError:
                pass


        if swapped:
            if k > 0 and strings[k].string == strings[k-1].string:
                del strings[-1]
            else:
                print(i, j, k)
                k += 1
            strings.append(my_string())
            print("---------------------")

        j += CHUNK_RUN - CHUNK_SIZE
        j += 1

    swapped = False

    for j in range(j, j + string.res):
        try:
            n = data.pos.index(j) # returns the index of the element j
            strings[k].string[j-1] = data.alt[n] # makes the swap
            swapped = True
            #print(i, j, k)
        except ValueError:
            pass
    if swapped:
        k += 1
        #print("---------------------")
    else:
        del strings[-1]

    print("")

    return strings, k

main_string = my_string()
main_string.print_chunk()
print(''.join(main_string.string))

data = my_data(pos, ref, alt)

print("")

print(data, "\n")

combinations, main_string.num_chunks = gen_comb(data, main_string)

j = 0
for i in range (main_string.num_chunks):
    for j in pos:
        print(''.join(combinations[i].string[j]), end='')
    print("")

print("")

for i in range (main_string.num_chunks):
    #combinations[0].print_chunk()
    print(i+1, ''.join(combinations[i].string))
    i += 1

