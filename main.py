# https://github.com/Forajido24/Actividad4

CHUNK_SIZE = 10
CHUNK_RUN = 5

original_string = "TGTAGTGCAGTGGCGTGATCTTGGCTCACTGCAGCCTCCACCTTAGAGCAATCCTCTTGCCTCATCCTCCCGGGTAGTTGGGACTACATGTGCATGCCACATGCCTGGCTAATTTTTGTATTTTTAGTA"
pos = [43, 15, 100, 54, 33, 19, 97, 13]
ref = "TTATGCCC" 
alt = "CAGAAGTA"

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

# gen fn's will just generate every set of alterations (chunks)

def gen_chunks(string, data):
    strings = [data.ref]
    i = n = j = m = 0
    k = 1

    strings.append(data.ref)
    strings.append(data.ref)

    for i in range(string.cos):
        swapped = False
        for j in range(j, j + CHUNK_SIZE):
            try:
                n = data.pos.index(j) # returns the index of the element j
                strings[k][n] = data.alt[n] # inserts the founded element
                swapped = True
                print(i, j, k, n)

            except ValueError:
                pass

        strings = ["".join(map(str, inner_array)) for inner_array in strings]

        if swapped:
            if strings[k] == strings[k-1]:
                del strings[-1]
            else:
                #print(i, j, k)
                k += 1
            strings.append(''.join(data.ref))
            print("---------------------")

        j += CHUNK_RUN - CHUNK_SIZE
        j += 1

        strings = [list(string) for string in strings]

    swapped = False

    for j in range(j, j + string.res):
        try:
            n = data.pos.index(j) # returns the index of the element j
            strings[k][n] = data.alt[n] # inserts the founded element
            swapped = True
            print(i, j, k, n)
        except ValueError:
            pass

    if swapped:
        if strings[k] == strings[k-1]:
            del strings[-1]
        else:
            #print(i, j, k)
            k += 1
        print("---------------------")

    print("")

    strings = ["".join(map(str, inner_array)) for inner_array in strings]

    return strings, k

def gen_comb(string, data, arr):
    pass

def gen_var(string, data, arr):
    pass

def get_chunks(string, data, arr): # This will save the generated chunks in an array 
    chunks = []
    k = len(arr)

    for i in range(k):
        chunks.append(string.string)
        for j in data.pos:
            try:
                n = data.pos.index(j) # returns the index of the element j
                strings.string[i] = data.alt[n]
            except:
                pass

    return chunks

main_string = my_string()
main_string.print_chunk()
print(''.join(main_string.string))

data = my_data(pos, ref, alt)
data.bubble_sort()

print("")

print(data, "\n")

chunks, main_string.num_chunks = gen_chunks(main_string, data)

chunks_strings = get_chunks(main_string, data, chunks)

j = 0
for i in range (1, main_string.num_chunks):
    print(i, ''.join(chunks_strings[i]))
print("")

for i in range (main_string.num_chunks):
    #combinations[0].print_chunk()
    print(i, ''.join(chunks[i]))
    i += 1

