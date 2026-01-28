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
n = 4

def make_str(n=n, G={"A", "G", "C", "T", "N"}):
    if n == 1:
        return G
    output = []
    combos = make_str(n-1, G)
    for item in combos:
        for char in G:
            output.append(item + char)  
    return output
g_s = make_str()

k_h = {}
k_d = {}


for i in g_s:
    k_h[i], k_d[i] = 0, 0

print(len(k_h))

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
            k_h[i] += 1
            h += 1
    elif i[1] == "dog":
        for i in s_g:
            k_d[i] += 1  
            d += 1 


d_x_h = {}
d_x_d = {}
for i in k_h:
    d_x_h[i] = (k_h[i])/(h)
    d_x_d[i] = (k_d[i])/(d) 

d_x_h = dict(sorted(d_x_h.items(), key=lambda x: x[1], reverse=True))
d_x_d = dict(sorted(d_x_d.items(), key=lambda x: x[1], reverse=True))
print(d_x_h)
print(d_x_d)

# human
#['CTG', 'CAG', 'TGG', 'CCA', 'GGA', 'AGA', 'CCT', 'GCC', 'CCC', 'GAG', 'GAA', 'AAG', ...
# ...
# ... 'NGN', 'NNN', 'NCN', 'CAN', 'CTN', 'CGN', 'CNA', 'CNT', 'CNG', 'CNN', 'CNC', 'CCN']

# dog
#['CTG', 'CAG', 'TGG', 'CCA', 'GGA', 'GCC', 'CCC', 'AGA', 'CCT', 'GAG', 'GAA', 'AAG', ...
# ...
# ... 'NTA', 'NTG', 'NTN', 'NTC', 'NGN', 'NNA', 'NNT', 'NCN', 'CAN', 'CTN', 'CNA', 'CNT']

def test(data):
    k_t = {}
    for i in g_s:
        k_t[i] = 0
    k = split_g(data)
    l = 0
    for i in k:
        k_t[i] += 1
        l += 1
    
    k_x_t = {}
    for i in k_t:
        k_x_t[i] = k_t[i]/l

    for_h = 0
    for_d = 0
    
    for i in list(d_x_h.keys())[20:50]:
        for_h += (k_x_t[i] - d_x_h[i])**2
    for i in list(d_x_d.keys())[20:50]:
        for_d += (k_x_t[i] - d_x_d[i])**2
    
    x_h = for_h**0.5
    x_d = for_d**0.5

    if x_h < x_d:
        return "human"
    elif x_d < x_h:
        return "dog"

print()
c = 0
for i in test_data:
    p = test(i[0])
    print(p, i[1])
    if p == i[1]:
        c += 1
print(c/len(test_data))
