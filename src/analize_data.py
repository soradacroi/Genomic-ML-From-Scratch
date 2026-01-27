m = {'a_a_c', 'c_c_g', 'c_t_c', 't_t_c', 't_a_t', 'c_g_c', 'g_c_t', 't_g_c', 'n_g_g', 'n_a_a', 't_a_c', 't_t_t', 'g_t_g', 'n_t_a', 'c_n_n', 'a_g_g', 'a_a_a', 'n_a_g', 'n_g_a', 'a_a_t', 't_t_a', 'c_c_a', 'n_g_c', 'a_c_c', 'c_c_c', 'g_c_a', 'n_n_a', 'g_a_t', 'c_t_a', 'a_t_c', 'n_c_g', 'a_t_n', 'n_t_g', 'g_g_c', 't_n_n', 'c_t_g', 'n_c_c', 't_a_g', 't_g_g', 't_g_t', 'a_t_a', 't_c_a', 'n_n_n', 'a_g_t', 'c_g_n', 't_t_g', 't_n_c', 'a_c_n', 't_c_n', 'g_g_n', 'g_g_g', 'c_c_t', 'g_g_t', 'n_a_c', 'a_c_a', 'a_g_a', 'a_g_c', 't_c_c', 'c_c_n', 'c_g_t', 'a_a_n', 'c_a_a', 'a_t_t', 'g_t_t', 'c_a_t', 'n_n_g', 'a_t_g', 'n_a_t', 'c_n_c', 'g_t_n', 'n_t_t', 'g_a_c', 'g_n_a', 'a_c_t', 'c_n_g', 't_c_t', 't_a_a', 'n_g_t', 'g_a_g', 'g_c_c', 'g_g_a', 'g_a_a', 'c_g_a', 'c_t_t', 'g_n_c', 't_g_n', 'a_n_n', 'g_t_c', 'c_g_g', 'a_a_g', 'n_n_t', 'n_c_a', 'g_t_a', 'g_c_g', 'g_n_n', 'n_c_t', 'c_a_g', 't_c_g', 'a_c_g', 't_g_a', 'c_a_c', 'n_n_c'}

l = []
for i in m:
    if i in l:
        print("wtf")
    else:
        l.append(i)
print(len(l)) # 102 wtf??? 

a = []
for i in m:
    for j in i.split("_"):
        if j not in a:
            a.append(j)
print(a) # i see i see wtf is an "n", it is like unknown ig