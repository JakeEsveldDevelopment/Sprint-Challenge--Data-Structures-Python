import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#Original Runtime complexity O(n*m) since n and m are the same, it is O(n^2)

#After conversion to Hashmap and single iteration, Runtime complexity is O(n + m) since n and m are the same reduced to O(n)

names_1_dict = dict()
for name in names_1:
    names_1_dict[name] = ""

duplicates = []

for name in names_2:
    if name in names_1_dict:
        duplicates.append(name)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

