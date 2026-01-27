import csv
import random as r

files = {'data/human.csv': 'human', 'data/dog.csv': 'dog'}
train_data = []
test_data = []
for f, species in files.items():
    with open(f, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        all_rows = list(reader) 
        r.shuffle(all_rows)
        train_data += [((row['sequence']), species) for row in all_rows[:810]]
        test_data += [((row['sequence']), species) for row in all_rows[810:820]]


G = {"A", "G", "C", "T", "N"}
n = 3

def make_str(n=3, G={"A", "G", "C", "T", "N"}):
    if n == 1:
        return G
    output = []
    combos = make_str(n-1, G)
    for item in combos:
        for char in G:
            output.append(item + char)
            
    return output

d_h = {}
d_d = {}

for i in make_str(3):
    d_h[i], d_d[i] = 0, 0


def split_g(g, n = 3):
    i = len(g)
    j = 0
    m = []
    while j + n != i:
        m.append(g[j:n+j])
        j += 1
    return m
    
            

for i in train_data:
    s_g = ((split_g(i[0])))
    if i[1] == "human":
        for i in s_g:
            d_h[i] += 1
    elif i[1] == "dog":
        for i in s_g:
            d_d[i] += 1   

print(d_h)
print()
print(d_d)
        


    

