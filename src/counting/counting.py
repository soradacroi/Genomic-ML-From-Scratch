import csv
import random as r
from decimal import Decimal, getcontext
getcontext().prec = 5

files = {'data/human.csv': 'human', 'data/dog.csv': 'dog'}
training_data = []
test_data = []
for f, species in files.items():
    with open(f, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        all_rows = list(reader) 
        r.shuffle(all_rows)
        training_data += [((row['sequence']), species) for row in all_rows[:810]]
        test_data += [((row['sequence']), species) for row in all_rows[810:820]]


G = {"A", "G", "C", "T", "N"}
n = 3

def make_str(n=n, G={"A", "G", "C", "T", "N"}):
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

for i in make_str():
    d_h[i], d_d[i] = 0, 0

print(len(d_h))

def split_g(g, n = n):
    i = len(g)
    j = 0
    m = []
    while j + n != i:
        m.append(g[j:n+j])
        j += 1
    return m
    
            
h, d = 0, 0
for i in training_data:
    s_g = ((split_g(i[0])))
    
    if i[1] == "human":
        for i in s_g:
            d_h[i] += 1
            h += 1
    elif i[1] == "dog":
        for i in s_g:
            d_d[i] += 1  
            d += 1 


d_x_h = {}
d_x_d = {}
for i in d_h:
    d_x_h[i] = (d_h[i])/(h)
for i in d_h:
    d_x_d[i] = (d_d[i])/(d) 

print(d_x_h)
print(d_x_d)


    